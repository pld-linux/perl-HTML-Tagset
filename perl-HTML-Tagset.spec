#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	HTML
%define		pnam	Tagset
Summary:	This module contains data tables useful in dealing with HTML
Summary(cs.UTF-8):	Modul datových tabulek pro práci s HTML
Summary(da.UTF-8):	Dette modul indeholder datatabeller som er nyttiga ved behandling af HTML
Summary(de.UTF-8):	Dieses Modul enthält Datentabellen, die bei der Arbeit mit HTML nützlich sind
Summary(es.UTF-8):	Este módulo contiene tablas de datos útiles para trabajar con HTML
Summary(fr.UTF-8):	Ce module contient des tables de données pratiques pour travailler avec HTML
Summary(it.UTF-8):	Questo modulo contiene tabelle di dati utili per la gestione di HTML
Summary(ja.UTF-8):	このモジュールには、HTML を処理するのに役立つデータテーブルが収録されています。
Summary(ko.UTF-8):	이 모줄은 HTML을 처리하는데 유용한 데이터 표들을 포함하고 있습니다
Summary(pl.UTF-8):	Moduł Perla zawierający tablice przydatne przy obróbce HTML
Summary(pt.UTF-8):	Este módulo contém tabelas de dados úteis para lidar com o HTML
Summary(sv.UTF-8):	Denna modul innehåller datatabeller som är användbara vid hantering av HTML
Summary(zh_CN.UTF-8):	这个模块包括对处理 HTML 有用的数据表格。
Name:		perl-HTML-Tagset
Version:	3.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f8db8974f5e7fe7df2a58263a7b00552
URL:		https://metacpan.org/dist/HTML-Tagset
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.46
BuildRequires:	perl-devel >= 1:5.10.1
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.95
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tagset - This module contains data tables useful in dealing with
HTML. It provides no functions or methods.

%description -l cs.UTF-8
Balíček perl-HTML-Tagset obsahuje datové tabulky, které se používají
pro práci s HTML. Neposkytuje žádné funkce ani metody.

%description -l da.UTF-8
HTML::Tagset - Dette modul indeholder datatabeller som er godt at have
når man handskas HTML. Den tillhandahåller inga funktioner eller
metoder.

%description -l de.UTF-8
HTML::Tagset - Dieses Modul enthält Datentabellen, die bei der Arbeit
mit HTML nützlich sind. Es liefert weder Funktionen noch Methoden.

%description -l es.UTF-8
HTML::Tagset - Este módulo contiene tablas de datos útiles para
trabajar con HTML. No proporciona ni funciones ni métodos.

%description -l fr.UTF-8
HTML::Tagset - Ce module contient des tables de données pratiques
lorsque vous travailler avec HTML. Il ne fournit aucune fonction ou
méthode.

%description -l it.UTF-8
HTML::Tagset - Questo modulo contiene tabelle di dati utili per la
gestione di HTML. Non fornisce funzioni né metodi."

%description -l ja.UTF-8
このモジュールには、HTML を処理するのに役立つデータテーブルが収録され
ています。これは関数やメソッドを提供しません。

%description -l pl.UTF-8
HTML::Tagset jest modułem dostarczającym tablic użytecznych przy
obróbce plików HTML.

%description -l pt.UTF-8
HTML::Tagset - Este módulo contém tabelas de dados úteis para lidar
com o HTML. Não fornece funções ou métodos.

%description -l sv.UTF-8
HTML::Tagset - Denna modul innehåller datatabeller som är bra att ha
när man handskas med HTML. Den tillhandahåller inga funktioner eller
metoder.

%description -l zh_CN.UTF-8
该模块包括几个对执行各类 HTML 解析操作有用的数据表格，
如标签和实体名称。

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
%doc Changes README.md
%{perl_vendorlib}/HTML/Tagset.pm
%{_mandir}/man3/HTML::Tagset.3pm*
