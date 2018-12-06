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
iot module subscribing to alerts from the AI powered analyzer.
responsible for responding to detected threats.



## discussion
different parts are designed to work and communicate separately, this is not the most efficient way of building this system but it would allow total separation of task plus would let us use different languages and technologies and mix and match easily.

## configuration
use `config.ini` files in to setup the communication (in `edge/communication/`) and the server app (in `server/`)

## installation
### general
we use [pipenv](https://pipenv.readthedocs.io/en/latest/) for managing python environments. Use pipenv to handle, install and run the python parts of the framework

whereever you see a `Pipfile` you'll need to run `pipenv install` to install the dependencies. Then use `pipenv run python PYTHONFILEHERE` to execute a python script

### pubsub broker
run the following command to start a "mosquitto" broker in docker.
`docker run -d --name mqtt-broker -p 1883:1883 -p 9001:9001 eclipse-mosquitto`
don't forget to open ports 1883 and 9001 to the publishers and subscribers



## TODO
- [x] implement and test different components separately
- [x] scheduled image capturing
- [x] integration tests
- [ ] Ansible support
- [ ] performance and timing analysis (cloud vs fog setup)
- [ ] better ML powered threat detection: Google's quickdraw doodle classifier?
- [ ] use a logger instead of print statements

