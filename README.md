# be.ENERGISED

Open
Charge
Point
Protocol

## Setup

    pipenv install

## Usage

    pipenv run python server.py

## TLS

Generate server certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

Generate client certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt
