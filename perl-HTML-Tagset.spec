%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Tagset perl module
Summary(pl):	Modu³ perla HTML-Tagset
Name:		perl-HTML-Tagset
Version:	3.02
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Vendor: PLD
Distribution: PLD
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Tagset-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/buildroot-%{name}-%{version}

%description
HTML-Tagset - This module contains data tables useful in dealing with HTML.

%description -l pl
HTML-Tagset jest modu³em dostarczaj±cym tablic uzytecznych przy obróbce plików
HTML.

%prep
%setup -q -n HTML-Tagset-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Tagset
  sed -e "s#$RPM_BUILD_ROOT##" .packlist | sort | uniq >.packlist.new
  mv .packlist.new .packlist
	
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/HTML/Tagset.pm
%{perl_sitearch}/auto/HTML/Tagset

%{_mandir}/man3/*
