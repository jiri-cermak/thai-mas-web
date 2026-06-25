#!/bin/bash
# Write token to a temp file to avoid shell escaping issues
echo -n "***>/tmp/gh-token.txt
RESP=$(curl -s -w "%{http_code}" -o /tmp/gh-user.json -H "Authorization: token $(cat /tmp/gh-token.txt)" "https://api.github.com/user")
echo "HTTP: $RESP"
python3 -c "
import json
d=json.load(open('/tmp/gh-user.json'))
print('User:', d.get('login', d.get('message', str(d))))
"
rm -f /tmp/gh-token.txt /tmp/gh-user.json
