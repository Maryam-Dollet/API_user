#!/bin/bash
set -e
black .
git add .
git commit -m "$1"
git push