%define tag	scylla-%{version}

Name:		scylla-jmx
Version:	4.0.0
Release:	1%{?dist}
Summary:	A highly scalable, eventually consistent, distributed, partitioned row database.
License:	AGPLv3
URL:		https://github.com/scylladb/%{name}
Source0:	https://github.com/scylladb/%{name}/archive/%{tag}.tar.gz#scylla-jmx-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  maven
BuildRequires:  systemd-units
Requires:	scylla-server java-1.8.0-openjdk-headless

%description
Scylla is a highly scalable, eventually consistent, distributed,
partitioned row database.

%prep
%autosetup -n %{name}-%{tag}

%build
mvn --quiet --file scylla-jmx-parent/pom.xml package

%install
install -d -m 755 %{buildroot}/%{_libexecdir}/scylla-jmx
install -d -m 755 %{buildroot}/%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}/%{_unitdir}
install -p -m 755 ./dist/common/sysconfig/scylla-jmx %{buildroot}/%{_sysconfdir}/sysconfig
install -p -m 755 ./dist/common/systemd/scylla-jmx.service %{buildroot}/%{_unitdir}
install -p -m 755 scripts/scylla-jmx %{buildroot}/%{_libexecdir}/scylla-jmx
install -p -m 755 target/scylla-jmx-1.0.jar %{buildroot}/%{_libexecdir}/scylla-jmx

%files
%defattr(-,root,root)

%config(noreplace) %{_sysconfdir}/sysconfig/scylla-jmx
%{_unitdir}/scylla-jmx.service
%{_libexecdir}/scylla-jmx/scylla-jmx
%{_libexecdir}/scylla-jmx/scylla-jmx-1.0.jar
