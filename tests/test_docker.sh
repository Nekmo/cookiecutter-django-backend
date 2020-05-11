#!/bin/sh
set -e

mkdir -p .tests/docker
cd .tests/docker

cookiecutter ../../ --no-input --overwrite-if-exists $@
cd my-project-name
sudo rm -rf data

docker-compose -f docker-compose.develop.yml up -d --build

sleep 5
curl http://127.0.0.1:8000 > /dev/null
