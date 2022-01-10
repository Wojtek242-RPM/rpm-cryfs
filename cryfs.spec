%global _hardened_build 1

# This file is encoded in UTF-8.  -*- coding: utf-8 -*-
Summary:       Cryptographic filesystem for the cloud
Name:          cryfs
Epoch:         1
Version:       0.11.1
Release:       1%{?dist}
License:       LGPLv3
URL:           https://www.cryfs.org/
Source0:       https://github.com/cryfs/cryfs/archive/%{version}.tar.gz
Source1:       check-and-update.sh

BuildRequires: boost-devel
BuildRequires: boost-static
BuildRequires: cmake
BuildRequires: fuse-devel
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python-unversioned-command
BuildRequires: python3
BuildRequires: python3-pip

Provides:      cryfs(bin) = %{epoch}:%{version}-%{release}
Provides:      cryfs-unmount(bin) = %{epoch}:%{version}-%{release}

%description
CryFS encrypts your files, so you can safely store them anywhere. It works well together with cloud
services like Dropbox, iCloud, OneDrive and others.

%prep
pip3 install conan --user
%autosetup

%build
%set_build_flags
mkdir cmake && cd cmake
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=off -DCRYFS_UPDATE_CHECKS=off
%make_build
cd ..

%install
%make_install -C cmake

%files
%{_bindir}/cryfs
%{_bindir}/cryfs-unmount
%{_mandir}/man1/cryfs.1.gz

%changelog
* Wed Sep  2 2020 Alex <redhat@att.org.ru> 0.10.2-1
- Initial spec file
