#!/bin/bash

# (kmateusz)
# This is a modification of scionproto/scion/env/debian/deps removing
# sudo and interactive session when apt-get

set -e

BASE=$(dirname "$0")
. $(dirname "$BASE")/common.sh

APTARGS=${APTARGS:---no-remove}

pkgs="$($BASE/check)"
[ -z "$pkgs" ] && exit

DEBIAN_FRONTEND=noninteractive apt-get -y install $APTARGS --no-install-recommends $pkgs
