%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Tagset
Summary:	HTML-Tagset perl module
Summary(pl):	Modu³ perla HTML-Tagset
Name:		perl-HTML-Tagset
Version:	3.03
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Tagset - This module contains data tables useful in dealing with
HTML.

%description -l pl
HTML-Tagset jest modu³em dostarczaj±cym tablic uzytecznych przy
obróbce plików HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/Tagset.pm
%{_mandir}/man3/*
