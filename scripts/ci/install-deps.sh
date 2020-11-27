#!/bin/bash
set -e

distro=$1

# install required packages
if [ "$distro" == "ubuntu" ]; then
    apt update -y
    apt install -y python3-pip python3-setuptools git wget
fi

# install python deps
pip3 install dataclasses
pip3 install git+https://github.com/antmicro/tuttest
