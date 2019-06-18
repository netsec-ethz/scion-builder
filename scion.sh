#!/usr/bin/env bash

# This helper script builds scion for different architectures

set -ex

mkdir -p /buildroot
cd /buildroot
git clone -b "$CI_SCION_BRANCH" "$CI_SCION_REPO"
cd scion

cp -R /data/debian .
cp /data/build-in-tmp.sh .

debuild -us -uc -b -a"$CI_TARGET_ARCHITECTURE" -tc

cd /buildroot
mkdir -p debs
cp *.deb debs
