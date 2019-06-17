#!/usr/bin/env bash

# This helper script builds libzlog for different architectures and
# installs the built packages locally to ensure the scion code will build correctly.

set -ex

mkdir /buildroot
cd /buildroot
if [ ! -d "$(pwd)/zlog" ]
then
	git clone "$CI_ZLOG_REPO"
fi
cd zlog
git checkout 1.2.12/debian
debuild -us -uc -b -aamd64 -tc
debuild -us -uc -b -aarm64 -tc
debuild -us -uc -b -aarmhf -tc
cd /buildroot
mkdir debs
cp *.deb debs
echo "Installing libzlog."
dpkg -i *.deb
