FROM ubuntu:focal

# set work directory
WORKDIR /usr/src/app

# uncomment for install behind artelias proxy
# ARG http_proxy=http://10.1.3.48:3128
# ARG https_proxy=http://10.1.3.48:3128

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # general dependancies
# RUN apt-get update && apt-get install apt-utils sudo dialog dos2unix wget -y
# # skipping prompt for keyboard conf
# RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration -y
# # needed for adding web repo in ubuntu
# RUN apt-get install gnupg software-properties-common -y

COPY arteliasite ./arteliasite
COPY Lamia ./Lamia
COPY requirements.txt ./requirements.txt