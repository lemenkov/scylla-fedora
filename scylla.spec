Name:		scylla
Version:        3.3.0
Release:	1%{?dist}
Summary:	A highly scalable, eventually consistent, distributed, partitioned row database.
License:	AGPLv3
URL:            https://github.com/scylladb/%{name}
#Source0:       https://github.com/scylladb/%{name}/archive/%{name}-%{version}.tar.gz
Source0:	https://github.com/penberg/scylla/archive/penberg/fedora.tar.gz
#Source1:	https://github.com/scylladb/%{name}-seastar/archive/%{name}-%{version}/%{name}-seastar-%{version}.tar.gz
Source1:        https://github.com/scylladb/seastar/archive/master.tar.gz#/seastar.tar.gz
Source2:	https://github.com/scylladb/libdeflate/archive/master.tar.gz#/libdeflate.tar.gz
Source3:	https://github.com/scylladb/zstd/archive/v1.4.2.tar.gz#/zstd.tar.gz
BuildRequires:	lua-devel
BuildRequires:	ninja-build
BuildRequires:	rapidjson-devel

%description
Scylla is a highly scalable, eventually consistent, distributed,
partitioned row database.

%prep
%autosetup -n scylla-penberg-fedora
tar xvf %SOURCE1
tar xvf %SOURCE2
tar xvf %SOURCE3

%build
# FIXME: change to "release"
%define mode	dev

./configure.py \
  --mode=%{mode} \
  --with-seastar=seastar-master \
  --with-libdeflate=libdeflate-master \
  --with-zstd=zstd-1.4.2

ninja-build build/%{mode}/scylla
