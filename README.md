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

### OCPP Messages

    > [2,1,"BootNotification",{"chargePointModel":"charge2019","chargePointVender":"has.to.be"}]
    > [2,2,"Authorize",{"idTag":"barCamp2019"}]
    > [2,3,"StartTransaction",{"connectorId":1,"idTag":"barCamp2019","meterStart":1234567,"timestamp":"2019-04-05T10:00:00"}]
    > [2,4,"StopTransaction",{"transactionId":0,"meterStop":1235678,"timestamp":"2019-04-05T12:00:00"}]

## TLS

Generate server certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

Generate client certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt
