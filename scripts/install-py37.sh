#!/bin/bash

sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y


# install python3.7
cd /tmp
wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
tar -xzvf Python-3.7.1.tgz
cd Python-3.7.1
./configure
make -j 4
sudo make altinstall

# pip3 install --user pipenv
