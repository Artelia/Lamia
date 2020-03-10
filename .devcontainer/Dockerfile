# debian stable base image
FROM ubuntu:bionic

ARG work_dir="/usr/src/docker_install/"
ENV http_proxy=http://10.1.3.48:3128
ENV https_proxy=http://10.1.3.48:3128

# setup dpkg front-end
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
# general dependancies
RUN apt-get update && apt-get install apt-utils dialog sudo dos2unix wget -y

# Add a user (sudoer)
RUN useradd -m docker && \
    echo "docker:docker" | chpasswd && \
    adduser docker sudo 

COPY .devcontainer/etc/sudoers /etc/sudoers
# fetch the repo dependancies
WORKDIR $work_dir

COPY .devcontainer/install_qgis.sh ./requirements.txt  $work_dir

# Assert that the windows GIT version did not mess up the EOL
RUN dos2unix --quiet /etc/sudoers
RUN find . -type f | xargs dos2unix --quiet

USER docker
RUN bash ./install_qgis.sh



# ENV PYTHONPATH="usr/share/qgis/python:/usr/share/qgis/python/plugins:/usr/lib/python36.zip:/usr/lib/python3.6:/usr/lib/python3.6/lib-dynload:/home/docker/.local/lib/python3.6/site-packages:/usr/local/lib/python3.6/dist-packages:/usr/lib/python3/dist-packages:$PYTHONPATH"
# ENV DISPLAY=10.20.75.139:0.0

CMD ["bash"]
