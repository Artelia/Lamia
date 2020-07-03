#!/bin/bash

# rem : >/dev/null change the output from standard output (terminal) to None 
# and 2>&1 make it also for error message
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PYTHON_ENV="${DIR}/venv"

echo 'Installing qgis ... '
## install qgis

if true ; then
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key 51F523511C7028C3
    add-apt-repository "deb https://qgis.org/ubuntu-ltr `lsb_release -c -s` main"
    # add-apt-repository "deb     https://qgis.org/ubuntu `lsb_release -c -s` main"
    apt-get update
    apt-get install qgis=1:3.* python3-qgis=1:3.* -y
fi

# preparing venv install
apt-get install python3-pip -y
pip3 install --upgrade pip 
pip3 install --upgrade setuptools 
pip3 install virtualenv

# creates a blank environnement - to do after qgis and his pythonics things
echo 'creating env:' ${PYTHON_ENV}
python3 -m virtualenv -p `which python3` ${PYTHON_ENV} --system-site-packages
source ${PYTHON_ENV}/bin/activate

#Requirements
echo 'Installing python requirement ... '
pip3 install -r ./requirements.txt

#for spatialite working on unbuntu 18.04
# ln -s /usr/lib/x86_64-linux-gnu/mod_spatialite.so /usr/lib/x86_64-linux-gnu/mod_spatialite