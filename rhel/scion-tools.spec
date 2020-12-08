Name: scion-tools
Version: devel
Release: 1
Summary: SCION Tools
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scion-tools-bin.tar

Requires: scion-daemon
Requires: scion-dispatcher

%description
SCION Tools

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%prep
ls -l bazel-out/k8-fastbuild/bin/

%build
tar xvf bazel-out/k8-fastbuild/bin/scion-tools-bin.tar

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/scion %{buildroot}%{_bindir}/scion
install -m 755 ./usr/bin/scion-pki %{buildroot}%{_bindir}/scion-pki
install -m 755 ./usr/bin/pathdb_dump %{buildroot}%{_bindir}/pathdb_dump

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/scion
%attr(0755, root, root) %{_bindir}/scion-pki
%attr(0755, root, root) %{_bindir}/pathdb_dump
