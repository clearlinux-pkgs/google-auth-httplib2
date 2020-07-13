#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-auth-httplib2
Version  : 0.0.3
Release  : 10
URL      : https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/google-auth-httplib2-0.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/google-auth-httplib2-0.0.3.tar.gz
Summary  : Google Authentication Library: httplib2 transport
Group    : Development/Tools
License  : Apache-2.0
Requires: google-auth-httplib2-license = %{version}-%{release}
Requires: google-auth-httplib2-python = %{version}-%{release}
Requires: google-auth-httplib2-python3 = %{version}-%{release}
Requires: google-auth
Requires: httplib2
BuildRequires : buildreq-distutils3
BuildRequires : google-auth
BuildRequires : httplib2

%description
``httplib2`` Transport for Google Auth
======================================
|pypi|

%package license
Summary: license components for the google-auth-httplib2 package.
Group: Default

%description license
license components for the google-auth-httplib2 package.


%package python
Summary: python components for the google-auth-httplib2 package.
Group: Default
Requires: google-auth-httplib2-python3 = %{version}-%{release}

%description python
python components for the google-auth-httplib2 package.


%package python3
Summary: python3 components for the google-auth-httplib2 package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth_httplib2)
Requires: pypi(google_auth)
Requires: pypi(httplib2)

%description python3
python3 components for the google-auth-httplib2 package.


%prep
%setup -q -n google-auth-httplib2-0.0.3
cd %{_builddir}/google-auth-httplib2-0.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583538774
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-auth-httplib2
cp %{_builddir}/google-auth-httplib2-0.0.3/LICENSE %{buildroot}/usr/share/package-licenses/google-auth-httplib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-auth-httplib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
