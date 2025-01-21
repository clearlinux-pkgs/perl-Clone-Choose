#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone-Choose
Version  : 0.010
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/H/HE/HERMES/Clone-Choose-0.010.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HE/HERMES/Clone-Choose-0.010.tar.gz
Summary  : 'Choose appropriate clone utility'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-Choose-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Without::Module)

%description
# NAME
Clone::Choose - Choose appropriate clone utility
# SYNOPSIS
use Clone::Choose;

%package dev
Summary: dev components for the perl-Clone-Choose package.
Group: Development
Provides: perl-Clone-Choose-devel = %{version}-%{release}
Requires: perl-Clone-Choose = %{version}-%{release}

%description dev
dev components for the perl-Clone-Choose package.


%package perl
Summary: perl components for the perl-Clone-Choose package.
Group: Default
Requires: perl-Clone-Choose = %{version}-%{release}

%description perl
perl components for the perl-Clone-Choose package.


%prep
%setup -q -n Clone-Choose-0.010
cd %{_builddir}/Clone-Choose-0.010

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Clone::Choose.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
