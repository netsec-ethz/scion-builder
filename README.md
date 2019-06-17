# scion-builder

Scripts and tools to build SCION

## Usage

This repo currently uses GitLab CI and artifacts to store the output. Each commit triggers a job which will store built packages for 24 hours.

## Configuration

CI process relies on some variables defined below. They can be configured using `Settings / CICD / Environment variables`.

* `CI_DOCKER_IMAGE`
* `CI_SCION_REPO`
* `CI_ZLOG_REPO`

## Origins

https://github.com/netsec-ethz/scion-debian-packager/
