#!/bin/bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PYTHON_ENV="${DIR}/venv"

## Build virtual environment
echo 
echo 'Building python virtual environment ...'
sudo apt-get update
sudo apt-get install python3-pip -y

if [ ! -z ${VIRTUAL_ENV} ]; then
    echo "leaving env ${VIRTUAL_ENV}"
    deactivate
fi
sudo -H pip3 install --upgrade pip 
sudo -H pip3 install --upgrade setuptools 
sudo -H pip3 install virtualenv

# creates a blank environnement
if [ ! -d ${PYTHON_ENV} ]; then
    echo 'creating env:' ${PYTHON_ENV}
    #PVR
    #python3 -m virtualenv -p `which python3` ${PYTHON_ENV}
    python3 -m virtualenv -p `which python3` ${PYTHON_ENV} --system-site-packages
fi
source ${PYTHON_ENV}/bin/activate

## install qgis
sudo apt-get install software-properties-common -y
sudo add-apt-repository "deb https://qgis.org/ubuntu-ltr bionic main"
# sudo add-apt-repository ppa:ubuntugis/ppa
wget -O - https://qgis.org/downloads/qgis-2019.gpg.key | gpg --import
gpg --export --armor 51F523511C7028C3 | sudo apt-key add -
sudo apt-get update
# sudo apt-get install qgis=3.4.11+dfsg-2~bionic1 python3-qgis=3.4.11+dfsg-2~bionic1 -y
sudo apt-get install qgis=1:3.10.* python3-qgis=1:3.10.* -y


#Requirement
sudo apt-get install python3-pip -y
sudo -H pip3 install --upgrade pip 
sudo -H pip3 install --upgrade setuptools 
pip3 install -r ./requirements.txt

#for spatialite working on unbuntu 18.04
sudo ln -s /usr/lib/x86_64-linux-gnu/mod_spatialite.so /usr/lib/x86_64-linux-gnu/mod_spatialite