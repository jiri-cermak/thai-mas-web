#!/bin/bash
TOKEN=***
echo "Token length: ${#TOKEN}"
curl -s -H "Authorization: token  ***!" --write-out '\n%{http_code}' "https://api.github.com/user" | tail -1
