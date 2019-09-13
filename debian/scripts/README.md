> This doc is meant to be read by any future developer who ever asks himself the question "who and where controls systemd interactions?"

### Background

In SCIONLab we want to have a full control over which services are configured on the machines belonging to the network. This means the responsability of enabling specific SCION services is offloaded to the operators of the network so the admin operations required from the end user are as small as possible.

### Basics

The current deployment model is as follows
* every SCION service provides a systemd service unit (sometimes templated) responsible for starting this and only this service
* `scionlab` umbrella package provides a systemd target which is supposed to collect all the SCION services

### Intermediaries

Every systemd service unit has a hardcoded link to the `scionlab.target` in its `[Install]` section what means it is not possible to enable the service without having `scionlab.target` present in the system.

A direct implication of this is that to have a fully functional setup the installation should be performed by installing `scionlab` package, not the specific packages for SCION services itself.

### Advanced

Packages for every SCION service are installing systemd units when package is installed and are removing them when the package is removed from the operating system. However, this is not a soft removal - there is no graceful `systemctl disable` or `systemctl stop`.

The only package interacting with systemd is `scionlab` where the following principles apply
* Before installation of the scionlab package there is a check confirming whether systemd is available. As scionlab package has lots of dependencies (i.e. SCION services) but the check is not performed in any of them, it may happen there will be a very late rollback in a scenario when systemd is not available (dependencies have already been installed but preinst of scionlab fails).
* Installation (but not upgrade) of the package will invoke `systemctl enable` against `scionlab.target`. Please note at this moment there will be no any real service installed inside `scionlab.target`, however it does block the possiblity of enabling the target. It is linked with `multi-user.target` so will be starting very late in the chain of the services started after restarting the operating system.
* Removal of the scionlab package will invoke `systemctl disable` and `systemctl stop` against `scionlab.target`. As at this moment there are services installed in this target, they will all be stopped.

In a general scenario that would be a very bad practice not do stop and disable systemd services for SCION services when removing their respective packages. In our deployment model however this is acceptable because of the following reasoning
* It is always expected to install the scionlab package which will take care of all the dependencies, i.e. SCION services' packages.
* Because scionlab package requires all SCION services' packages to be present, removal of any of them will cause removal of the scionlab package. At this moment the chain described above will happen causing the `scionlab.target` to be stopped what will cascade into all the services belonging there.

### Issues

> https://gitlab.inf.ethz.ch/OU-PERRIG/scionlab/scion-builder/issues/1

There are some scenarios in which systemd may be left in a dirty state
* Installation of a specific SCION service package without installing scionlab, followed by `systemctl start`, followed by removal of this package. In this scenario none of prerm nor postinst interacted with systemd.
