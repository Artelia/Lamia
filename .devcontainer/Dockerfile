# ubuntu stable base image
FROM ubuntu:focal

ARG work_dir="/usr/src/dev_env/"

# uncomment for install behind artelias proxy
# ARG http_proxy=http://10.1.3.48:3128
# ARG https_proxy=http://10.1.3.48:3128

# general dependancies
RUN apt-get update && apt-get install apt-utils sudo dialog dos2unix wget -y
# skipping prompt for keyboard conf
RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration -y
# needed for adding web repo in ubuntu
RUN apt-get install gnupg software-properties-common -y


#copying install files
WORKDIR $work_dir
COPY .devcontainer/install_qgis.sh ./requirements.txt  $work_dir

# install dev env
RUN bash ./install_qgis.sh

ENV VIRTUAL_ENV=$work_dir/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["bash"]
