import os, json, urllib.request, sys

token = os.environ.get('GH_TOKEN', '')
if not token:
    print("FAIL: GH_TOKEN not set")
    sys.exit(1)

req = urllib.request.Request('https://api.github.com/user')
req.add_header('Authorization', f'Bearer {token}')
req.add_header('Accept', 'application/vnd.github+json')
req.add_header('X-GitHub-Api-Version', '2022-11-28')

try:
    with urllib.request.urlopen(req) as resp:
        user = json.loads(resp.read())
        print(f"OK: {user.get('login')}")
except Exception as e:
    body = e.read().decode() if hasattr(e, 'read') else str(e)
    print(f"FAIL: {body[:200]}")
