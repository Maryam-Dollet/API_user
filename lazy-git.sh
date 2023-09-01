#!/bin/bash
set -e
black .
git add .

echo Type message
read -p "Message: " message

git commit -m "$message"
git push