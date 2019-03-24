#!/bin/sh
set -e

mkdir -p .tests/docker
cd .tests/docker

cookiecutter ../../ --no-input --overwrite-if-exists $@
cd my-project-name
sudo rm -rf data

docker-compose build
docker-compose up -d
