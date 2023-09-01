#!/bin/sh
set -e

mkdir -p .tests/docker
cd .tests/docker

sudo rm -rf my-project-name/data my-project-name/conf
cookiecutter ../../ --no-input --overwrite-if-exists $@
cd my-project-name

openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
        -subj "/C=ES/ST=Madrid/L=Madrid/O=Example/CN=www.example.com" \
        -keyout conf/nginx/ssl/example.com.key  -out conf/nginx/ssl/example.com_chained.crt

echo "Testing develop environment"
docker-compose -f docker-compose.develop.yml up -d --build
sleep 10
curl http://127.0.0.1:8000 > /dev/null
docker-compose down

echo "Testing production environment"
docker-compose -f docker-compose.yml up -d --build
sleep 10
curl -k -H "Host: example.com" https://127.0.0.1 > /dev/null
docker-compose down
