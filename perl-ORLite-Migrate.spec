
%define realname   ORLite-Migrate
%define version    0.03
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Extremely light weight SQLite-specific schema migration
Source:     http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(File::pushd)
BuildRequires: perl(File::Spec)
BuildRequires: perl(ORLite)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Probe::Perl)

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
%setup -q -n %{realname}-%{version} 

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


