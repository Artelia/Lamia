# debian stable base image
FROM ubuntu:bionic

ARG work_dir="/usr/src/dev_env/"
# ARG http_proxy=http://10.1.3.48:3128
# ARG https_proxy=http://10.1.3.48:3128

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

RUN chown -R docker:docker $work_dir

# Assert that the windows GIT version did not mess up the EOL
RUN dos2unix --quiet /etc/sudoers
RUN find . -type f | xargs dos2unix --quiet

USER docker
RUN bash ./install_qgis.sh


ENV VIRTUAL_ENV=$work_dir/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["bash"]
