Name: scion-dispatcher
Version: devel
Release: 1
Summary: SCION Dispatcher
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scion-dispatcher.tar.gz

Requires: shadow-utils
Requires: systemd
Requires: scion-systemd-wrapper

%description
SCION Dispatcher

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%prep
ls -l bazel-out/k8-fastbuild/bin/

%build
tar xvf bazel-out/k8-fastbuild/bin/scion-dispatcher.tar.gz

%pre
getent group scion >/dev/null || groupadd -r scion
getent passwd scion >/dev/null || \
    useradd -r -g scion -M -s /sbin/nologin \
    -c "SCION Internet Architecture" scion
exit 0

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/godispatcher %{buildroot}%{_bindir}/godispatcher

#mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}/lib/systemd/system/
cp ./lib/systemd/system/scion-dispatcher.service %{buildroot}/lib/systemd/system/scion-dispatcher.service

mkdir -p %{buildroot}%{_sysconfdir}/scion
mkdir -p %{buildroot}%{_var}/log/scion
mkdir -p %{buildroot}%{_var}/lib/scion
mkdir -p %{buildroot}/run/shm/dispatcher

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/godispatcher
%attr(0644, root, root) /lib/systemd/system/scion-dispatcher.service
%dir %attr(0755, scion, scion) %{_sysconfdir}/scion
%dir %attr(0755, scion, scion) %{_var}/log/scion
%dir %attr(0755, scion, scion) %{_var}/lib/scion
%dir %attr(0777, scion, scion) /run/shm/dispatcher
