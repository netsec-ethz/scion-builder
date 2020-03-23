# scion-builder

Scripts and tools to build SCION

## Configuration

CI process relies on some variables defined below. They can be configured using `Settings / CICD / Environment variables`.

### DEB repository configuration

* `CI_SSH_PRIVATE_KEY`

## Usage

For every commit GitLab CI and its artifacts are used to store the output. Each commit triggers a job which will store built packages for 1 hour in the GitLab Artifactory.

### Manual trigger

Pipeline can be run manually in order to build packages (without releasing them) using `CICD / Pipelines / Run Pipeline`. For a run containing deployment step please read the next chapter.

### Releasing packages

Bump the version of the packages you want to release in RELEASE.
This can be done directly on master or as part of a merge request.

The version of the umbrella package scionnlab *always* needs to be bumped when releasing any package.
The reason for this is that scionlab package depends on the exact versions of the other packages -- this seems fairly dumb, but is done by choice to reduce the number of possible ways for the expected users to screw up.

### Versioning and backtracing

If it is ever needed to check which commit a selected version of DEB package is based on, it is possible to extract this information from the log of the pipeline. Every job in the `Build` stage (e.g. `all-deb-amd64`) at the very end outputs the latest commit in every git repository which was used to generate the packages.

## Schedule

The builder is configured to run twice per day in order to check whether the packages can be still created successfuly, but without releasing them. The last step has to be invoked manually by the operator as described above (by bumping the versions in RELEASE).

## Package installation

Based on the current configuration, packages can be installed in one of the following ways

### Debian-based
```bash
echo "deb [trusted=yes] http://packages.netsec.inf.ethz.ch/debian all main" >> /etc/apt/sources.list.d/scionlab.list
```

```bash
apt install -y apt-transport-https
echo "deb [trusted=yes] https://packages.netsec.inf.ethz.ch/debian all main" >> /etc/apt/sources.list.d/scionlab.list
```

### RH-based
Not yet available.

## Staging repository

For branches matching the pattern `^staging.*`, packages are deployed to the staging package repository `https://packages-test.netsec.inf.ethz.ch/debian`.

The repository does not allow re-deploying the same package version multiple times.
To work around this we can manually **remove all packages in the test repository**:

`ssh` to the repository machine `packages-test.netsec.inf.ethz.ch` and run

```bash
sudo /home/reprepro/wipe-test-reprepro.sh
```

## Upstream projects

* https://github.com/scionproto/scion
* https://github.com/netsec-ethz/scion
* https://github.com/netsec-ethz/scionlab/

## Origins

https://github.com/netsec-ethz/scion-debian-packager/
