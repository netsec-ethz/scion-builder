Name: scionlab
Version: devel
Release: 1
Summary: SCIONLab
URL: https://www.scion-architecture.net
License: Apache License, v2.0

Source0: bazel-out/k8-fastbuild/bin/scionlab.tar.gz

Requires: scion-border-router = CI_PKG_VERSION_SCION_BORDER_ROUTER
Requires: scion-beacon-server = CI_PKG_VERSION_SCION_BEACON_SERVER
Requires: scion-certificate-server = CI_PKG_VERSION_SCION_CERTIFICATE_SERVER
Requires: scion-path-server = CI_PKG_VERSION_SCION_PATH_SERVER
Requires: scion-daemon = CI_PKG_VERSION_SCION_DAEMON
Requires: scion-dispatcher = CI_PKG_VERSION_SCION_DISPATCHER
Requires: scion-tools = CI_PKG_VERSION_SCION_TOOLS

Requires: openssl
Requires: python3 >= 3.5

Recommends: openvpn

%description
SCIONLab

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%build
tar xvf bazel-out/k8-fastbuild/bin/scionlab.tar.gz

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
install -m 755 ./usr/bin/scionlab-config %{buildroot}%{_bindir}/scionlab-config

#mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}/lib/systemd/system/
cp ./lib/systemd/system/scionlab.target %{buildroot}/lib/systemd/system/scionlab.target

%clean
rm -rf %{buildroot}

%post
# check gen-certs/tls.{pem,key}
if [ ! -e "/etc/scion/gen-certs/tls.pem" -o ! -e "/etc/scion/gen-certs/tls.key" ]; then
    echo "SCIONLab: Generating TLS cert"
    mkdir -p "/etc/scion/gen-certs"

    pushd "/etc/scion/gen-certs"
    openssl genrsa -out "tls.key" 2048
    chmod 600 "tls.key"
    openssl req -new -x509 -key "tls.key" -out "tls.pem" -days 3650 -subj /CN=scion_def_srv
    popd

    chown -R scion.scion "/etc/scion/gen-certs"
fi

# refresh the configuration and restart services (systemctl restart scionlab.target must be called in scionlab-config)
if [ -e "/etc/scion/gen/scionlab-config.json" ]; then
    scionlab-config --force || true
fi

%files
%attr(0755, root, root) %{_bindir}/scionlab-config
%attr(0644, root, root) /lib/systemd/system/scionlab.target
