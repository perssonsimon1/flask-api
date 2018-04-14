# Flask API



## About

A simple restful api using flask


## Setup
All of the dependencies can easily be installed with pip. Used dependencies are and should be specified in the requirements.txt file.

All specified dependencies can be installed using:

`python3 setup.py install`

## Hosting it locally

First make sure you have all dependencies installed

The following environment variable has to be exported:
```
FLASK_APP=app
```

Then to host it locally use:
```
python3 -m flask run
```

The following parameters are used by default:
```
Address: 127.0.0.1
Port: 5000
Debug Mode: True
```

## Testing
...


## Firebase

The environment key should be located at `etc/firebase.json`
