#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Font-Awesome
Version  : 4.3.0.0
Release  : 9
URL      : https://pypi.python.org/packages/source/X/XStatic-Font-Awesome/XStatic-Font-Awesome-4.3.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Font-Awesome/XStatic-Font-Awesome-4.3.0.0.tar.gz
Summary  : Font-Awesome 4.3.0 (XStatic packaging standard)
Group    : Development/Tools
License  : OFL-1.1 MIT
Requires: XStatic-Font-Awesome-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Font-Awesome
--------------
Font Awesome icons packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Font-Awesome package.
Group: Default

%description python
python components for the XStatic-Font-Awesome package.


%prep
%setup -q -n XStatic-Font-Awesome-4.3.0.0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
