#!/bin/bash
set -e

cd /opt/student-mlops

docker build -t student-app .

docker rm -f student-app 2>/dev/null || true

docker run -d 
  --name student-app 
  --restart unless-stopped 
  -p 80:5000 
  student-app