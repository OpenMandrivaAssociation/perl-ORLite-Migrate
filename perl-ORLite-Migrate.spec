# find-requires also extracts version, which is then misunderstood by
# rpm. therefore, forcing require skipping of File::Spec - which is
# nevertheless required by perl-PathTools
%define _requires_exceptions perl.File::Spec.

%define upstream_name    ORLite-Migrate
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extremely light weight SQLite-specific schema migration
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(File::pushd)
BuildRequires: perl(ORLite)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl-PathTools
Requires: perl(IPC::Run3)
Requires: perl-PathTools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


