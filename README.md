# Flask API



## About

A simple restful api using flask


## Methods

### [accidents](https://h4s-api.herokuapp.com/api/accidents/2017)
This returns all accidents that occured in traffic in Sweden for a given year, in this case 2017.

### [accidents/info](https://h4s-api.herokuapp.com/api/accidents/info/2017)
This returns extra information about the accidents described above.

### [accidents/count](https://h4s-api.herokuapp.com/api/accidents/count/2017)
This returns the number of accidents for every city in a given year, in this case 2017.

### [roads](https://h4s-api.herokuapp.com/api/roads/2017)
This returns the number of accidents for every road in a given year, in this case 2017.

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
