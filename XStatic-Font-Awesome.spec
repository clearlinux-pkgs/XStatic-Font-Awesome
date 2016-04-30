#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Font-Awesome
Version  : 4.5.0.0
Release  : 14
URL      : https://pypi.python.org/packages/source/X/XStatic-Font-Awesome/XStatic-Font-Awesome-4.5.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Font-Awesome/XStatic-Font-Awesome-4.5.0.0.tar.gz
Summary  : Font-Awesome 4.5.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT OFL-1.1
Requires: XStatic-Font-Awesome-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Font-Awesome
--------------
Font Awesome icons packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Font-Awesome package.
Group: Default
Provides: xstatic-font-awesome-python

%description python
python components for the XStatic-Font-Awesome package.


%prep
%setup -q -n XStatic-Font-Awesome-4.5.0.0

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
