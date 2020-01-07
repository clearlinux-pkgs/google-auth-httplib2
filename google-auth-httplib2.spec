#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-auth-httplib2
Version  : 0.0.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/google-auth-httplib2-0.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/google-auth-httplib2-0.0.3.tar.gz
Summary  : Google Authentication Library: httplib2 transport
Group    : Development/Tools
License  : Apache-2.0
Requires: google-auth-httplib2-license = %{version}-%{release}
Requires: google-auth-httplib2-python = %{version}-%{release}
Requires: google-auth-httplib2-python3 = %{version}-%{release}
Requires: httplib2
BuildRequires : buildreq-distutils3

%description
======================================
        
        |pypi|
        
        This library provides an `httplib2`_ transport for `google-auth`_.

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

%description python3
python3 components for the google-auth-httplib2 package.


%prep
%setup -q -n google-auth-httplib2-0.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542311870
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-auth-httplib2
cp LICENSE %{buildroot}/usr/share/package-licenses/google-auth-httplib2/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-auth-httplib2/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
