# ovpnWebman

[![Build Status](https://travis-ci.org/alanplatt/ovpnWebman.svg)](https://travis-ci.org/alanplatt/ovpnWebman)

Python flask web user cert manager container for kylemanna/openvpn

To use, setup your kylemanna/openvpn container and then run this container pointing it to the same docker data volume


## Run locally for dev
```
virtualenv .venv
pip install -r requirements.txt
pip install --editable .
FLASK_DEBUG=1 FLASK_APP=ovpnWebman flask run
```

## Run with docker
```
docker-compose up
```

## Test & Lint
```
test.sh
```
