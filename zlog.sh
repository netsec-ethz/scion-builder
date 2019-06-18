#!/usr/bin/env bash

# This helper script builds libzlog for different architectures and
# installs the built packages locally to ensure the scion code will build correctly.

set -ex

mkdir -p /buildroot
cd /buildroot
git clone -b "$CI_ZLOG_BRANCH" "$CI_ZLOG_REPO"
cd zlog

debuild -us -uc -b -a"$CI_TARGET_ARCHITECTURE" -tc

cd /buildroot
mkdir -p debs
cp *.deb debs

echo "Installing libzlog."
dpkg -i *.deb
