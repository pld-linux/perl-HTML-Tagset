#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Tagset
Summary:	This module contains data tables useful in dealing with HTML
Summary(cs):	Modul datov�ch tabulek pro pr�ci s HTML
Summary(da):	Dette modul indeholder datatabeller som er nyttiga ved behandling af HTML
Summary(de):	Dieses Modul enth�lt Datentabellen, die bei der Arbeit mit HTML n�tzlich sind
Summary(es):	Este m�dulo contiene tablas de datos �tiles para trabajar con HTML
Summary(fr):	Ce module contient des tables de donn�es pratiques pour travailler avec HTML
Summary(it):	Questo modulo contiene tabelle di dati utili per la gestione di HTML
Summary(ja):	���Υ⥸�塼��ˤϡ�HTML ���������Τ���Ω�ĥǡ����ơ��֥뤬��Ͽ����Ƥ��ޤ���
Summary(ko):	�� ������ HTML�� ó���ϴµ� ������ ������ ǥ���� �����ϰ� �ֽ��ϴ�
Summary(pl):	Modu� Perla zawieraj�cy tablice przydatne przy obr�bce HTML
Summary(pt):	Este m�dulo cont�m tabelas de dados �teis para lidar com o HTML
Summary(sv):	Denna modul inneh�ller datatabeller som �r anv�ndbara vid hantering av HTML
Summary(zh_CN):	���ģ������Դ��� HTML ���õ������
Name:		perl-HTML-Tagset
Version:	3.03
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47c56ab15771fac1a6fdfcbf8bff4288
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tagset - This module contains data tables useful in dealing with
HTML. It provides no functions or methods.

%description -l cs
Bal��ek perl-HTML-Tagset obsahuje datov� tabulky, kter� se pou��vaj�
pro pr�ci s HTML. Neposkytuje ��dn� funkce ani metody.

%description -l da
HTML::Tagset - Dette modul indeholder datatabeller som er godt at have
n�r man handskas HTML. Den tillhandah�ller inga funktioner eller
metoder.

%description -l de
HTML::Tagset - Dieses Modul enth�lt Datentabellen, die bei der Arbeit
mit HTML n�tzlich sind. Es liefert weder Funktionen noch Methoden.

%description -l es
HTML::Tagset - Este m�dulo contiene tablas de datos �tiles para
trabajar con HTML. No proporciona ni funciones ni m�todos.

%description -l fr
HTML::Tagset - Ce module contient des tables de donn�es pratiques
lorsque vous travailler avec HTML. Il ne fournit aucune fonction ou
m�thode.

%description -l it
HTML::Tagset - Questo modulo contiene tabelle di dati utili per la
gestione di HTML. Non fornisce funzioni n� metodi."

%description -l ja
���Υ⥸�塼��ˤϡ�HTML ���������Τ���Ω�ĥǡ����ơ��֥뤬��Ͽ����
�Ƥ��ޤ�������ϴؿ���᥽�åɤ��󶡤��ޤ���

%description -l pl
HTML::Tagset jest modu�em dostarczaj�cym tablic u�ytecznych przy
obr�bce plik�w HTML.

%description -l pt
HTML::Tagset - Este m�dulo cont�m tabelas de dados �teis para lidar
com o HTML. N�o fornece fun��es ou m�todos.

%description -l sv
HTML::Tagset - Denna modul inneh�ller datatabeller som �r bra att ha
n�r man handskas med HTML. Den tillhandah�ller inga funktioner eller
metoder.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/HTML/Tagset.pm
%{_mandir}/man3/*
