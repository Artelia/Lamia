#!/bin/bash


## install qgis
sudo apt-get install software-properties-common -y
sudo add-apt-repository "deb https://qgis.org/ubuntu-ltr bionic main"
# sudo add-apt-repository ppa:ubuntugis/ppa
wget -O - https://qgis.org/downloads/qgis-2019.gpg.key | gpg --import
gpg --export --armor 51F523511C7028C3 | sudo apt-key add -
sudo apt-get update
# sudo apt-get install qgis=3.4.11+dfsg-2~bionic1 python3-qgis=3.4.11+dfsg-2~bionic1 -y
sudo apt-get install qgis=1:3.10.3+28bionic python3-qgis=1:3.10.3+28bionic -y

#nano geany
sudo apt-get install nano geany xdg-utils -y

#Requirement
sudo apt-get install python3-pip -y
sudo -H pip3 install --upgrade pip 
sudo -H pip3 install --upgrade setuptools 
pip3 install -r ./requirements.txt