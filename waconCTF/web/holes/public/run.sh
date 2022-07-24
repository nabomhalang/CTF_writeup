#!/bin/sh

docker build . -t deep_holes
docker kill deep_holes 2>/dev/null
docker run -p 9000:9000 -p 8000:8000 --rm --name deep_holes deep_holes
