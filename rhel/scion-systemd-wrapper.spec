Name: scion-systemd-wrapper
Version: devel
Release: 1
Summary: SCION systemd wrapper
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scion-systemd-wrapper-bin.tar

%description
SCION systemd wrapper

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%build
tar xvf bazel-out/k8-fastbuild/bin/scion-systemd-wrapper-bin.tar

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/scion-systemd-wrapper %{buildroot}%{_bindir}/scion-systemd-wrapper

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) %{_bindir}/scion-systemd-wrapper
