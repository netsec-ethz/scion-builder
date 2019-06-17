#!/usr/bin/env bash

# This helper script builds libzlog for different architectures and
# installs the built packages locally to ensure the scion code will build correctly.

set -ex

mkdir -p /buildroot
cd /buildroot
git clone "$CI_SCION_REPO"
cd scion

cp -R /data/debian .
cp /data/build-in-tmp.sh .

debuild -us -uc -b -aamd64 -tc
debuild -us -uc -b -aarm64 -tc
debuild -us -uc -b -aarmhf -tc

cd /buildroot
mkdir -p debs
for x in *.deb
do
	cp "${x}" debs
done
