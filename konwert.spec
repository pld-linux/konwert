Summary:	Converter of character encodings
Summary(pl.UTF-8):   Konwerter kodowań znaków
Name:		konwert
Version:	1.8
Release:	7
License:	GPL
Group:		Applications/Text
Source0:	http://qrczak.ids.net.pl/programy/linux/konwert/%{name}-%{version}.tar.gz
# Source0-md5:	0a1dcb0fa7a1990980aba8ab9a4c3184
Patch0:		%{name}-forbids_data_member.patch
URL:		http://qrczak.ids.net.pl/programy/linux/konwert/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
Requires:	perl-base >= 5.001
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konwert is a package for conversion of text between various character
encodings.

%description -l pl.UTF-8
Pakiet Konwert służy do konwersji tekstów między różnymi kodowaniami
znaków.

%package devel
Summary:	Development of Konwert's filters
Summary(pl.UTF-8):   Narzędzia do tworznie filtrów Konwerta
Group:		Applications/Text
Requires:	konwert

%description devel
Konwert is a package for conversion of text between various character
encodings. This package contains scripts and data files useful for
development new filters. They are not needed for normal usage.

%description devel -l pl.UTF-8
Pakiet Konwert służy do konwersji tekstów między różnymi kodowaniami
znaków. Ten pakiet zawiera skrypty i dane przydatne do tworzenia
nowych filtrów. Nie są one potrzebne do normalnego użytkowania.

%prep
%setup -q
%patch0 -p1

%build
OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
OPTFLAGS="$OPTFLAGS -fno-rtti -fno-exceptions -fno-implicit-templates"
%{__make} \
	CXXFLAGS="$OPTFLAGS" \
	prefix=%{_prefix} \
	perl=%{__perl} \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	mydocdir=$RPM_BUILD_ROOT%{_docdir}/konwert-%{version} \
	perl=%{__perl} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	dontfixmanconfig=1

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/share/konwert/aux/fixmanconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/trs
%attr(755,root,root) %{_bindir}/konwert
%attr(755,root,root) %{_bindir}/filterm
%dir %{_datadir}/konwert
%attr(755,root,root) %{_datadir}/konwert/filters
%dir %{_datadir}/konwert/aux
%{_datadir}/konwert/aux/UTF8-ascii
%{_datadir}/konwert/aux/UTF8-ascii1
%attr(755,root,root) %{_datadir}/konwert/aux/UTF8-charset
%{_datadir}/konwert/aux/UTF8-tex
%{_datadir}/konwert/aux/any
%attr(755,root,root) %{_datadir}/konwert/aux/argcharset
%attr(755,root,root) %{_datadir}/konwert/aux/charset-charset
%{_datadir}/konwert/aux/charsets
%attr(755,root,root) %{_datadir}/konwert/aux/fixmanconfig
%attr(755,root,root) %{_datadir}/konwert/aux/fixmeta
%dir %{_libdir}/konwert
%attr(755,root,root) %{_libdir}/konwert/aux
%docdir %{_docdir}/konwert-%{version}
%dir %{_docdir}/konwert-%{version}
%dir %{_docdir}/konwert-%{version}/en
%{_docdir}/konwert-%{version}/en/BUGS
%{_docdir}/konwert-%{version}/en/CHANGES
%{_docdir}/konwert-%{version}/en/README
%{_docdir}/konwert-%{version}/en/TODO
%{_docdir}/konwert-%{version}/en/filterm
%{_docdir}/konwert-%{version}/en/filters
%{_docdir}/konwert-%{version}/en/konwert
%{_docdir}/konwert-%{version}/en/thanks
%{_docdir}/konwert-%{version}/en/trs
%lang(pl) %dir %{_docdir}/konwert-%{version}/pl
%lang(pl) %{_docdir}/konwert-%{version}/pl/BLEDY
%lang(pl) %{_docdir}/konwert-%{version}/pl/CZYTAJTO
%lang(pl) %{_docdir}/konwert-%{version}/pl/DO_ZROBIENIA
%lang(pl) %{_docdir}/konwert-%{version}/pl/ZMIANY
%lang(pl) %{_docdir}/konwert-%{version}/pl/filterm
%lang(pl) %{_docdir}/konwert-%{version}/pl/filtry
%lang(pl) %{_docdir}/konwert-%{version}/pl/konwert
%lang(pl) %{_docdir}/konwert-%{version}/pl/podziekowania
%lang(pl) %{_docdir}/konwert-%{version}/pl/trs
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/konwert/devel
%{_datadir}/konwert/devel/UTF8-ascii
%{_datadir}/konwert/devel/UTF8-charset
%{_datadir}/konwert/devel/aliases
%{_datadir}/konwert/devel/any
%attr(755,root,root) %{_datadir}/konwert/devel/charset-UTF8
%{_datadir}/konwert/devel/charset-charset
%attr(755,root,root) %{_datadir}/konwert/devel/fixtrsutf8
%attr(755,root,root) %{_datadir}/konwert/devel/fixutf8
%attr(755,root,root) %{_datadir}/konwert/devel/frequencies
%attr(755,root,root) %{_datadir}/konwert/devel/hex-trs
%attr(755,root,root) %{_datadir}/konwert/devel/mergetrs
%{_datadir}/konwert/devel/mergewithcp437
%attr(755,root,root) %{_datadir}/konwert/devel/mime
%attr(755,root,root) %{_datadir}/konwert/devel/mkUTF8-ascii
%attr(755,root,root) %{_datadir}/konwert/devel/mkUTF8-charset
%attr(755,root,root) %{_datadir}/konwert/devel/mkaliases
%attr(755,root,root) %{_datadir}/konwert/devel/mkany
%attr(755,root,root) %{_datadir}/konwert/devel/mkcharset-charset
%attr(755,root,root) %{_datadir}/konwert/devel/whichletters
%docdir %{_docdir}/konwert-%{version}
%{_docdir}/konwert-%{version}/en/devel
%lang(pl) %{_docdir}/konwert-%{version}/pl/tworzenie
