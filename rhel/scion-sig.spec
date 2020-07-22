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
install -m 755 ./usr/bin/sig %{buildroot}%{_bindir}/sig

mkdir -p %{buildroot}/usr/share/doc/scion-ip-gateway/templates
cp ./usr/share/doc/scion-ip-gateway/templates/sig.config %{buildroot}/usr/share/doc/scion-ip-gateway/templates/sig.config
cp ./usr/share/doc/scion-ip-gateway/templates/rules.json %{buildroot}/usr/share/doc/scion-ip-gateway/templates/rules.json
cp ./usr/share/doc/scion-ip-gateway/templates/extra-topology-sig.json %{buildroot}/usr/share/doc/scion-ip-gateway/templates/extra-topology-sig.json

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/sig

%attr(0644, scion, scion) /usr/share/doc/scion-ip-gateway/templates/sig.config
%attr(0644, scion, scion) /usr/share/doc/scion-ip-gateway/templates/rules.json
%attr(0644, scion, scion) /usr/share/doc/scion-ip-gateway/templates/extra-topology-sig.json

%dir %attr(0755, scion, scion) /usr/share/doc/scion-ip-gateway/templates
