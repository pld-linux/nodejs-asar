%define		pkg	asar
Summary:	asar - Atom-Shell Archive
Name:		nodejs-%{pkg}
Version:	0.8.3
Release:	0.1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/asar/-/%{pkg}-%{version}.tgz
# Source0-md5:	26b8cdc5b19c905e5f0a163b1428eb8e
URL:		https://github.com/atom/asar
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asar is a simple extensive archive format, it works like tar that
concatenates all files together without compression, while having
random access support.

Features:
- Support random access
- Use JSON to store files' information
- Very easy to write a parser

%prep
%setup -qc
mv package/* .

%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/*
chmod a+rx bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

cp -a bin $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
ln -s %{nodejs_libdir}/%{pkg}/bin/%{pkg} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/asar
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/lib
%dir %{nodejs_libdir}/%{pkg}/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/*
