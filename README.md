# scion-builder

Scripts and tools to build SCION

## Configuration

CI process relies on some variables defined below. They can be configured using `Settings / CICD / Environment variables`.

### Upstream repositories

* `CI_SCION_REPO`
* `CI_SCION_BRANCH`
* `CI_SCIONLAB_REPO`
* `CI_SCIONLAB_BRANCH`

### Builder configuration

* `CI_DOCKER_IMAGE`
* `CI_BAZEL_URL`

### DEB repository configuration

* `CI_SCP_TARGET`
* `CI_SSH_PRIVATE_KEY`
* `CI_DEB_CODENAME`

## Usage

For every commit GitLab CI and its artifacts are used to store the output. Each commit triggers a job which will store built packages for 1 hour in the GitLab Artifactory.

### Manual trigger

Pipeline can be run manually in order to build packages (without releasing them) using `CICD / Pipelines / Run Pipeline`. For a run containing deployment step please read the next chapter.

### Releasing packages

In order to release a package to the DEB repository a tag `release/0.0.0` should be created (obviously changing `0.0.0` to a desired version). This will trigger an additional step in the pipeline responsible for uploading and releasing the generated packages.

Overwriting an already existing version is not allowed and will fail either at the level of pushing a tag to the git repository or at the moment of uploading packages to the hosting server.

### Versioning and backtracing

If it is ever needed to check which commit a selected version of DEB package is based on, it is possible to extract this information from the log of the pipeline. Every job in the `Build` stage (e.g. `all-deb-amd64`) at the very end outputs the latest commit in every git repository which was used to generate the packages.

## Schedule

The builder is configured to run twice per day in order to check whether the packages can be still created successfuly, but without releasing them. The last step has to be invoked manually by the operator as described above (by pushing a proper tag).

## Upstream projects

* https://github.com/scionproto/scion
* https://github.com/netsec-ethz/netsec-scion
* https://github.com/netsec-ethz/scionlab/

## Origins

https://github.com/netsec-ethz/scion-debian-packager/
