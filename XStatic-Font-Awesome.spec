#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Font-Awesome
Version  : 4.7.0.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/e5/28/34ced5dd65f1cb7b21a156a88f36e9ce37efd5d96bc2d9dca82f86103bd3/XStatic-Font-Awesome-4.7.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/28/34ced5dd65f1cb7b21a156a88f36e9ce37efd5d96bc2d9dca82f86103bd3/XStatic-Font-Awesome-4.7.0.0.tar.gz
Summary  : Font-Awesome 4.7.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT OFL-1.1
Requires: XStatic-Font-Awesome-python3
Requires: XStatic-Font-Awesome-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
--------------
        
        Font Awesome icons packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Font-Awesome package.
Group: Default
Requires: XStatic-Font-Awesome-python3
Provides: xstatic-font-awesome-python

%description python
python components for the XStatic-Font-Awesome package.


%package python3
Summary: python3 components for the XStatic-Font-Awesome package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-Font-Awesome package.


%prep
%setup -q -n XStatic-Font-Awesome-4.7.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532378902
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
