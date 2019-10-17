Name: scion-daemon
Version: devel
Release: 1
Summary: SCION Daemon
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scion-daemon.tar.gz

Requires: shadow-utils
Requires: systemd
Requires: scion-systemd-wrapper

%description
SCION Daemon

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%prep
ls -l bazel-out/k8-fastbuild/bin/

%build
tar xvf bazel-out/k8-fastbuild/bin/scion-daemon.tar.gz

%pre
getent group scion >/dev/null || groupadd -r scion
getent passwd scion >/dev/null || \
    useradd -r -g scion -M -s /sbin/nologin \
    -c "SCION Internet Architecture" scion
exit 0

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/sciond %{buildroot}%{_bindir}/sciond

#mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}/lib/systemd/system/
cp ./lib/systemd/system/scion-daemon@.service %{buildroot}/lib/systemd/system/scion-daemon@.service

mkdir -p %{buildroot}%{_sysconfdir}/scion
mkdir -p %{buildroot}%{_var}/log/scion
mkdir -p %{buildroot}%{_var}/lib/scion
mkdir -p %{buildroot}/run/shm/sciond

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/sciond
%attr(0644, root, root) /lib/systemd/system/scion-daemon@.service
%dir %attr(0755, scion, scion) %{_sysconfdir}/scion
%dir %attr(0755, scion, scion) %{_var}/log/scion
%dir %attr(0755, scion, scion) %{_var}/lib/scion
%dir %attr(0777, scion, scion) /run/shm/sciond
