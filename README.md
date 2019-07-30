# scion-builder

Scripts and tools to build SCION

## Usage

This repo currently uses GitLab CI and artifacts to store the output. Each commit triggers a job which will store built packages for 24 hours.

## Configuration

CI process relies on some variables defined below. They can be configured using `Settings / CICD / Environment variables`.

* `CI_DOCKER_IMAGE`
* `CI_SCION_REPO`
* `CI_SCION_BRANCH`
* `CI_BAZEL_URL`

As the last step uploads generated packages to the online repository, an SSH private key is required so that GitLab CI can automatically upload files to the destination server. This configuration is stored in the following variables

* `CI_SSH_PRIVATE_KEY`
* `CI_SCP_TARGET`

## Upstream project

* https://github.com/scionproto/scion
* https://github.com/netsec-ethz/netsec-scion

## Origins

https://github.com/netsec-ethz/scion-debian-packager/
