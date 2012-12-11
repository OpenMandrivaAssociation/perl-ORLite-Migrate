# find-requires also extracts version, which is then misunderstood by
# rpm. therefore, forcing require skipping of File::Spec - which is
# nevertheless required by perl-PathTools
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(File::Spec\\)'
%else
%define _requires_exceptions perl.File::Spec.
%endif

%define upstream_name    ORLite-Migrate
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Extremely light weight SQLite-specific schema migration
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(File::Which)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(ORLite)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl-PathTools

BuildArch:	noarch

Requires:	perl(IPC::Run3)
Requires:	perl-PathTools

%description
SQLite is a light weight single file SQL database that provides an
excellent platform for embedded storage of structured data.

ORLite is a light weight single class Object-Relational Mapper (ORM)
system specifically designed for (and limited to only) work with SQLite.

ORLite::Migrate is a light weight single class Database Schema Migration
enhancement for ORLite.

It provides a simple implementation of schema versioning within the
SQLite database using the built-in user_version pragma (which is set to
zero by default).

When setting up the ORM class, an additional timeline parameter is
provided, which should point to a directory containing standalone
migration scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 654270
- rebuild for updated spec-helper

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 527736
- update to 1.07

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 488016
- adding missing buildrequires:
- update to 1.06

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 450062
- update to 1.05

* Sat Jul 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 396988
- rebuild for auto provides extraction
- using %%perl_convert_version
- fixed license field

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-4mdv2010.0
+ Revision: 372567
- adding runtime prereq

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-3mdv2010.0
+ Revision: 371647
- forcing prereq skipping to allow installation

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-2mdv2010.0
+ Revision: 369812
- forcing runtime requires

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-1mdv2010.0
+ Revision: 369661
- prereq should be in form of mdv pkg, since it is a dual lifed pkg
- adding missing prereq
- update to 0.03

* Tue Dec 30 2008 Jérôme Quelin <jquelin@mandriva.org> 0.01-1mdv2009.1
+ Revision: 321395
- import perl-ORLite-Migrate


* Tue Dec 30 2008 jquelin 0.01-1mdv
- initial mdv release

