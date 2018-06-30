#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : attrs
Version  : 17.4.0
Release  : 18
URL      : http://pypi.debian.net/attrs/attrs-17.4.0.tar.gz
Source0  : http://pypi.debian.net/attrs/attrs-17.4.0.tar.gz
Source99 : http://pypi.debian.net/attrs/attrs-17.4.0.tar.gz.asc
Summary  : Classes Without Boilerplate
Group    : Development/Tools
License  : MIT
Requires: attrs-python3
Requires: attrs-license
Requires: attrs-python
Requires: Sphinx
Requires: six
Requires: zope.interface
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: http://www.attrs.org/en/latest/_static/attrs_logo.png
:alt: attrs Logo

%package legacypython
Summary: legacypython components for the attrs package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the attrs package.


%package license
Summary: license components for the attrs package.
Group: Default

%description license
license components for the attrs package.


%package python
Summary: python components for the attrs package.
Group: Default
Requires: attrs-python3

%description python
python components for the attrs package.


%package python3
Summary: python3 components for the attrs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the attrs package.


%prep
%setup -q -n attrs-17.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530370087
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530370087
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/attrs
cp LICENSE %{buildroot}/usr/share/doc/attrs/LICENSE
cp docs/license.rst %{buildroot}/usr/share/doc/attrs/docs_license.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/attrs/LICENSE
/usr/share/doc/attrs/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
