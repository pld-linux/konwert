Summary:	Converter of character encodings
Summary(pl):	Konwerter kodowañ znaków
Name:		konwert
Version:	1.8
Release:	3
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Source0:	http://qrczak.home.ml.org/programy/linux/konwert/%{name}-%{version}.tar.gz
Patch0:		%{name}-forbids_data_member.patch
URL:		http://qrczak.home.ml.org/programy/linux/konwert/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	perl >= 5.001
BuildRequires: perl

%description
Konwert is a package for conversion of text between various character
encodings.

%description -l pl
Pakiet Konwert s³u¿y do konwersji tekstów miêdzy ró¿nymi kodowaniami
znaków.

%package devel
Summary:	development of Konwert's filters
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Requires:	konwert

%description devel
Konwert is a package for conversion of text between various character
encodings. This package contains scripts and data files useful for
development new filters. They are not needed for normal usage.

%description -l pl devel
Pakiet Konwert s³u¿y do konwersji tekstów miêdzy ró¿nymi kodowaniami
znaków. Ten pakiet zawieta skrypty i dane przydatne do tworzenia nowych
filtrów. Nie s± one potrzebne do normalnego u¿ytkowania.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS" make prefix=%{_prefix} perl=%{_bindir}/perl

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} perl=%{_bindir}/perl dontfixmanconfig=1

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/share/konwert/aux/fixmanconfig

%files
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/trs
%attr(755, root, root) %{_bindir}/konwert
%attr(755, root, root) %{_bindir}/filterm
%attr(755, root, root) %dir %{_datadir}/konwert
%attr(755, root, root) %{_datadir}/konwert/filters
%attr(755, root, root) %dir %{_datadir}/konwert/aux
%{_datadir}/konwert/aux/UTF8-ascii
%{_datadir}/konwert/aux/UTF8-ascii1
%attr(755, root, root) %{_datadir}/konwert/aux/UTF8-charset
%{_datadir}/konwert/aux/UTF8-tex
%{_datadir}/konwert/aux/any
%attr(755, root, root) %{_datadir}/konwert/aux/argcharset
%attr(755, root, root) %{_datadir}/konwert/aux/charset-charset
%{_datadir}/konwert/aux/charsets
%attr(755, root, root) %{_datadir}/konwert/aux/fixmanconfig
%attr(755, root, root) %{_datadir}/konwert/aux/fixmeta
%attr(755, root, root) %dir %{_libdir}/konwert
%attr(755, root, root) %{_libdir}/konwert/aux
%docdir %{_prefix}/doc/konwert-%{version}
%lang(en) %{_prefix}/doc/konwert-%{version}/en/BUGS
%lang(en) %{_prefix}/doc/konwert-%{version}/en/CHANGES
%lang(en) %{_prefix}/doc/konwert-%{version}/en/README
%lang(en) %{_prefix}/doc/konwert-%{version}/en/TODO
%lang(en) %{_prefix}/doc/konwert-%{version}/en/filterm
%lang(en) %{_prefix}/doc/konwert-%{version}/en/filters
%lang(en) %{_prefix}/doc/konwert-%{version}/en/konwert
%lang(en) %{_prefix}/doc/konwert-%{version}/en/thanks
%lang(en) %{_prefix}/doc/konwert-%{version}/en/trs
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/BLEDY
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/CZYTAJTO
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/DO_ZROBIENIA
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/ZMIANY
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/filterm
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/filtry
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/konwert
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/podziekowania
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/trs
%attr(664, root, man) %lang(en) %{_prefix}/man/man*/*
%attr(664, root, man) %lang(pl) %{_prefix}/man/pl/man*/*

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/konwert/devel
%{_datadir}/konwert/devel/UTF8-ascii
%{_datadir}/konwert/devel/UTF8-charset
%{_datadir}/konwert/devel/aliases
%{_datadir}/konwert/devel/any
%attr(755, root, root) %{_datadir}/konwert/devel/charset-UTF8
%{_datadir}/konwert/devel/charset-charset
%attr(755, root, root) %{_datadir}/konwert/devel/fixtrsutf8
%attr(755, root, root) %{_datadir}/konwert/devel/fixutf8
%attr(755, root, root) %{_datadir}/konwert/devel/frequencies
%attr(755, root, root) %{_datadir}/konwert/devel/hex-trs
%attr(755, root, root) %{_datadir}/konwert/devel/mergetrs
%{_datadir}/konwert/devel/mergewithcp437
%attr(755, root, root) %{_datadir}/konwert/devel/mime
%attr(755, root, root) %{_datadir}/konwert/devel/mkUTF8-ascii
%attr(755, root, root) %{_datadir}/konwert/devel/mkUTF8-charset
%attr(755, root, root) %{_datadir}/konwert/devel/mkaliases
%attr(755, root, root) %{_datadir}/konwert/devel/mkany
%attr(755, root, root) %{_datadir}/konwert/devel/mkcharset-charset
%attr(755, root, root) %{_datadir}/konwert/devel/whichletters
%docdir %{_prefix}/doc/konwert-%{version}
%lang(en) %{_prefix}/doc/konwert-%{version}/en/devel
%lang(pl) %{_prefix}/doc/konwert-%{version}/pl/tworzenie
