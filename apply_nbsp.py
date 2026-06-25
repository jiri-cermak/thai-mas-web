#!/usr/bin/env python3
"""
Task 10: Apply Czech typography rule — non-breakable space (&nbsp;)
after single-character words in visible text content.

Rule: In body and heading text, replace regular space with &nbsp;
after all single-character words (a, i, o, u, s, k, v, z).

Scope: Only visible text nodes inside <body>. Excludes:
  - <script>, <style>, <noscript> content
  - HTML attributes (alt, title, aria-label, etc.)
  - <meta>, <link>, comments
  - URLs, email addresses, phone numbers, file paths

Files processed: index.html, cenik.html, gallery.html
Output: In-place modification with .backup timestamp.
"""

import re
import shutil
from pathlib import Path
from datetime import datetime

# ── Configuration ──
FILES = [
    "index.html",
    "cenik.html",
    "gallery.html",
]

# Single-character Czech words that need &nbsp; after them
SINGLE_CHAR_WORDS = {"a", "i", "o", "u", "s", "k", "v", "z"}

# HTML tags whose content we skip entirely
SKIP_TAGS = {"script", "style", "noscript"}


def protect_special_patterns(text: str) -> tuple[str, list[str]]:
    """
    Temporarily replace URLs, emails, tel: links, file paths
    with placeholders so we don't inject &nbsp; inside them.
    Returns (masked_text, list_of_originals).
    """
    placeholders = []
    counter = [0]

    def make_placeholder(original: str) -> str:
        token = f"\x00PROTECTED_{counter[0]}\x00"
        counter[0] += 1
        placeholders.append(original)
        return token

    # tel: links
    text = re.sub(r'tel:\+?[\d\s\*]+', lambda m: make_placeholder(m.group()), text)

    # mailto: links
    text = re.sub(r'mailto:[^"\'\s<>]+', lambda m: make_placeholder(m.group()), text)

    # http/https URLs
    text = re.sub(r'https?://[^"\'\s<>]+', lambda m: make_placeholder(m.group()), text)

    # file paths (e.g., gallery/medium/142_medium.jpg)
    text = re.sub(r'[\w\-]+/[\w\-/.]+\.[a-zA-Z]{2,5}', lambda m: make_placeholder(m.group()), text)

    # HTML tags and attributes (e.g., <a href="..." class="a b">)
    text = re.sub(r'<[^>]+>', lambda m: make_placeholder(m.group()), text)

    return text, placeholders


def restore_special_patterns(text: str, placeholders: list[str]) -> str:
    """Restore protected patterns from placeholders."""
    for i in reversed(range(len(placeholders))):
        text = text.replace(f"\x00PROTECTED_{i}\x00", placeholders[i])
    return text


def apply_nbsp_to_text(text: str) -> str:
    """
    Apply &nbsp; after single-character words.
    Handles both plain text and text containing inline HTML tags.
    """
    # Pattern: word boundary + single char word + space + next word
    # We need to match: (space or > or start)(single_char)(space)(word_char)
    # But simpler: find all occurrences of single-char words followed by space
    # and not inside HTML tags.

    def replace_match(m):
        before = m.group(1)  # space or > or start of string
        word = m.group(2)    # the single-char word
        return f"{before}{word}&nbsp;"

    # Match: (space or >|^ or &nbsp;)([aiouskvzAIOUSKVZ])(space)(word character or digit)
    # Using lookahead so consecutive single-char words are both matched
    # Loop handles chains like "v a z" where each replacement creates &nbsp; prefix
    pattern = r'(^|>|\s|&nbsp;)([aiouskvzAIOUSKVZ]) (?=[\w\d])'
    prev = None
    while prev != text:
        prev = text
        text = re.sub(pattern, replace_match, text)

    return text


def process_html_file(filepath: Path) -> tuple[int, int]:
    """
    Process a single HTML file.
    Returns (replacements_done, lines_changed).
    """
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Split into lines for reporting
    lines = content.split('\n')
    new_lines = []
    total_replacements = 0
    lines_changed = 0

    in_skip_tag = None  # track which skip tag we're inside

    for line in lines:
        # Track skip tags (simple state machine)
        # This handles tags that may span lines
        if in_skip_tag:
            if f"</{in_skip_tag}>" in line.lower():
                in_skip_tag = None
            new_lines.append(line)
            continue

        # Check if line opens a skip tag — but only if it's not a self-closing tag
        skip_opened = False
        for tag in SKIP_TAGS:
            # Match opening tag but not self-closing (e.g., <script ...> but not <script ... />)
            if re.search(rf'<{tag}\b[^\u003e]*(?<!/)\s*\u003e', line, re.IGNORECASE):
                # Check if closing tag is also on this line
                if f"</{tag}>" not in line.lower():
                    in_skip_tag = tag
                skip_opened = True
                break
        if skip_opened:
            new_lines.append(line)
            continue

        # Process this line
        masked, placeholders = protect_special_patterns(line)
        processed = apply_nbsp_to_text(masked)
        restored = restore_special_patterns(processed, placeholders)

        if restored != line:
            lines_changed += 1
            # Count replacements by comparing
            count = restored.count('&nbsp;') - line.count('&nbsp;')
            total_replacements += max(0, count)

        new_lines.append(restored)

    new_content = '\n'.join(new_lines)

    if new_content != original:
        # Backup
        backup_path = filepath.with_suffix(f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        shutil.copy2(filepath, backup_path)
        filepath.write_text(new_content, encoding='utf-8')

    return total_replacements, lines_changed


def main():
    base_dir = Path(__file__).parent
    print("Task 10: Applying Czech non-breakable spaces")
    print("=" * 50)

    for filename in FILES:
        filepath = base_dir / filename
        if not filepath.exists():
            print(f"SKIP: {filename} not found")
            continue

        replacements, lines = process_html_file(filepath)
        status = f"{replacements} replacements in {lines} lines" if replacements > 0 else "no changes"
        print(f"  {filename}: {status}")

    print("=" * 50)
    print("Done. Backup files created with .backup_* suffix.")


if __name__ == "__main__":
    main()
