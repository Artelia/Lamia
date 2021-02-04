# ubuntu stable base image
FROM ubuntu:focal

ARG work_dir="/usr/src/dev_env/"

# uncomment for install behind artelias proxy
ARG http_proxy=http://10.1.3.48:3128
ARG https_proxy=http://10.1.3.48:3128

# general dependancies
RUN apt-get update && apt-get install apt-utils sudo dialog dos2unix wget -y
# skipping prompt for keyboard conf
RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration -y
# needed for adding web repo in ubuntu
RUN apt-get install gnupg software-properties-common -y

RUN wget -qO - https://qgis.org/downloads/qgis-2020.gpg.key | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import
RUN chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg
# RUN add-apt-repository "deb https://qgis.org/debian-ltr `lsb_release -c -s` main"
RUN add-apt-repository "deb https://qgis.org/ubuntu-ltr `lsb_release -c -s` main"
RUN apt-get update
RUN apt-get install qgis=1:3.10.* -y

RUN apt-get install python3-pip python3-sphinx python3-stemmer  -y

#copying install files
WORKDIR $work_dir
# COPY .devcontainer/install_qgis.sh ./requirements.txt  $work_dir
COPY ./requirements.txt  $work_dir

RUN pip3 install -r requirements.txt


# install dev env
# RUN bash ./install_qgis.sh






# ENV VIRTUAL_ENV=$work_dir/venv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["bash"]
