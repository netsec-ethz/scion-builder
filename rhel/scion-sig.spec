Name: scion-sig
Version: devel
Release: 1
Summary: SCION IP Gateway
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scion-sig.tar.gz

Requires: libcap
Requires: scion-daemon
Requires: scion-dispatcher

%description
SCION IP Gateway

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%prep
ls -l bazel-out/k8-fastbuild/bin/

%build
tar xvf bazel-out/k8-fastbuild/bin/scion-sig.tar.gz

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/scion-ip-gateway %{buildroot}%{_bindir}/scion-ip-gateway

mkdir -p %{buildroot}/etc/scion/
cp ./etc/scion/sig.toml %{buildroot}/etc/scion/sig.toml
cp ./etc/scion/sig.json %{buildroot}/etc/scion/sig.json

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/scion-ip-gateway

%attr(0644, scion, scion) /etc/scion/sig.toml
%attr(0644, scion, scion) /etc/scion/sig.json

%dir %attr(0755, scion, scion) /etc/scion/
