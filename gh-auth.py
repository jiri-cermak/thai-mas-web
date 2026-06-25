import os, json, urllib.request

# Read token from environment - set by sourcing .env
token = os.environ.get('GITHUB_TOKEN', '')
if not token:
    print("NO TOKEN")
    # Try reading from .env directly
    try:
        for line in open(os.path.expanduser('~/.hermes/.env')):
            if line.startswith('GITHUB_TOKEN='):
                token = line.split('=', 1)[1].strip().strip('"').strip("'")
                print(f"Read from file, len={len(token)}")
                break
    except Exception as e:
        print(f"Cannot read file: {e}")
        exit(1)

if not token:
    print("Still no token")
    exit(1)

req = urllib.request.Request('https://api.github.com/user')
req.add_header('Authorization', f'Bearer {token}')
req.add_header('Accept', 'application/vnd.github+json')
req.add_header('X-GitHub-Api-Version', '2022-11-28')

try:
    with urllib.request.urlopen(req) as resp:
        user = json.loads(resp.read())
        print(f"AUTH OK: {user.get('login')}")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body[:200]}")
