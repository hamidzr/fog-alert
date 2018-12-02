# Intrusion Detector

CC Project


## components
### edge device
captures and transfers camera feed to the server for further processing

### AI powered analyzer
analyzes and classifies the camera feed from the edge camera device


### pubsub broker
facilitates pub sub communication in the system


### intrusion response
nodemcu / raspberry pi module subscribing to alerts from the ai powered analyzer.
responsible for responding to detected threats.



## discussion
different parts are designed to work and communicate separately, this is not the most efficient way of building this system but it would allow total separation of task plus would let us use different languages and technologies and mix and match easily.

## configuration
use `config.ini` files in to setup the communication (in `edge/communication/`) and the server app (in `server/`)

## installation
we use [pipenv](https://pipenv.readthedocs.io/en/latest/) for managing python environments.

whereever you see a `Pipfile` you'll need to run `pipenv install` to install the dependencies. Then use `pipenv run python PYTHONFILEHERE` to execute a python script
