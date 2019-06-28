#!/usr/bin/env bash

# This helper script installs all the dependencies required to build SCION packages

set -ex

mkdir -p /data
mkdir -p output-$CI_TARGET_ARCHITECTURE

cp apt.sources.list /etc/apt/sources.list
cp apt.prefs /etc/apt/preferences.d/pcap.pref

dpkg --add-architecture $CI_TARGET_ARCHITECTURE

apt update
apt install -yq \
libpcap0.8:$CI_TARGET_ARCHITECTURE \
linux-libc-dev:$CI_TARGET_ARCHITECTURE \
libc6:$CI_TARGET_ARCHITECTURE \
uthash-dev:$CI_TARGET_ARCHITECTURE \
libpcap0.8-dev:$CI_TARGET_ARCHITECTURE \
build-essential \
gcc \
gcc-aarch64-linux-gnu \
gcc-arm-linux-gnueabihf \
g++ \
g++-aarch64-linux-gnu \
g++-arm-linux-gnueabihf \
dpkg-dev \
golang-1.10-go \
capnproto \
bash \
git \
debhelper \
debianutils \
debootstrap \
dh-make \
gnupg2 \
devscripts \
build-essential \
lintian

cp zlog.sh /bin/zlog.sh
cp build-in-tmp.sh /data/build-in-tmp.sh
cp scion.sh /bin/scion.sh
cp -r debian /data/debian