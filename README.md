# be.ENERGISED

Open  
Charge  
Point  
Protocol

## Disclaimer

This is the result of two talks at Barcamp Salzburg 2019
* be.ENERGISED in 40 minutes (tag: day1)
* be.ENERGISED security in 20 minutes (tag: day2)

## Setup

    pipenv install

## Usage

    pipenv run python server.py

## TLS

Generate server certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

Generate client certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt
