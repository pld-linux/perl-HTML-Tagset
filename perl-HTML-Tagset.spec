%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Tagset
Summary:	This module contains data tables useful in dealing with HTML
Summary(cs):	Modul datových tabulek pro práci s HTML
Summary(da):	Dette modul indeholder datatabeller som er nyttiga ved behandling af HTML
Summary(de):	Dieses Modul enthält Datentabellen, die bei der Arbeit mit HTML nützlich sind
Summary(es):	Este módulo contiene tablas de datos útiles para trabajar con HTML
Summary(fr):	Ce module contient des tables de données pratiques pour travailler avec HTML
Summary(it):	Questo modulo contiene tabelle di dati utili per la gestione di HTML
Summary(ja):	¤³¤Î¥â¥¸¥å¡¼¥ë¤Ë¤Ï¡¢HTML ¤ò½èÍý¤¹¤ë¤Î¤ËÌòÎ©¤Ä¥Ç¡¼¥¿¥Æ¡¼¥Ö¥ë¤¬¼ýÏ¿¤µ¤ì¤Æ¤¤¤Þ¤¹¡£
Summary(ko):	ÀÌ ¸ðÁÙÀº HTMLÀ» Ã³¸®ÇÏ´Âµ¥ À¯¿ëÇÑ µ¥ÀÌÅÍ Ç¥µéÀ» Æ÷ÇÔÇÏ°í ÀÖ½À´Ï´Ù
Summary(pl):	Modu³ perla zawieraj±cy tablice przydatne przy obróbce HTML
Summary(pt):	Este módulo contém tabelas de dados úteis para lidar com o HTML
Summary(sv):	Denna modul innehåller datatabeller som är användbara vid hantering av HTML
Summary(zh_CN):	Õâ¸öÄ£¿é°üÀ¨¶Ô´¦Àí HTML ÓÐÓÃµÄÊý¾±í¡£
Name:		perl-HTML-Tagset
Version:	3.03
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tagset - This module contains data tables useful in dealing with
HTML. It provides no functions or methods.

%description -l cs
Balíèek perl-HTML-Tagset obsahuje datové tabulky, které se pou¾ívají
pro práci s HTML. Neposkytuje ¾ádné funkce ani metody.

%description -l da
HTML::Tagset - Dette modul indeholder datatabeller som er godt at have
når man handskas HTML. Den tillhandahåller inga funktioner eller
metoder.

%description -l de
HTML::Tagset - Dieses Modul enthält Datentabellen, die bei der Arbeit
mit HTML nützlich sind. Es liefert weder Funktionen noch Methoden.

%description -l es
HTML::Tagset - Este módulo contiene tablas de datos útiles para
trabajar con HTML. No proporciona ni funciones ni métodos.

%description -l fr
HTML::Tagset - Ce module contient des tables de données pratiques
lorsque vous travailler avec HTML. Il ne fournit aucune fonction ou
méthode.

%description -l it
HTML::Tagset - Questo modulo contiene tabelle di dati utili per la
gestione di HTML. Non fornisce funzioni né metodi."

%description -l ja
¤³¤Î¥â¥¸¥å¡¼¥ë¤Ë¤Ï¡¢HTML ¤ò½èÍý¤¹¤ë¤Î¤ËÌòÎ©¤Ä¥Ç¡¼¥¿¥Æ¡¼¥Ö¥ë¤¬¼ýÏ¿¤µ¤ì
¤Æ¤¤¤Þ¤¹¡£¤³¤ì¤Ï´Ø¿ô¤ä¥á¥½¥Ã¥É¤òÄó¶¡¤·¤Þ¤»¤ó¡£

%description -l pl
HTML::Tagset jest modu³em dostarczaj±cym tablic uzytecznych przy
obróbce plików HTML.

%description -l pt
HTML::Tagset - Este módulo contém tabelas de dados úteis para lidar
com o HTML. Não fornece funções ou métodos.

%description -l sv
HTML::Tagset - Denna modul innehåller datatabeller som är bra att ha
när man handskas med HTML. Den tillhandahåller inga funktioner eller
metoder.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/HTML/Tagset.pm
%{_mandir}/man3/*
