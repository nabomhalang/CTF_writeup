#!/bin/bash

socat tcp-l:9000,reuseaddr,fork EXEC:"/app/cli.py",pty,stderr &
cd /app
chmod +x ./*.py
./app.py