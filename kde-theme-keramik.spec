%define		_theme	keramik

Summary:	keramik theme
Summary(pl.UTF-8):	Motyw keramik
Name:		kde-theme-%{_theme}
Version:	1
Release:	2.2
License:	GPL
Group:		Themes/GTK+
#Source0:	http://www.kde-look.org/content/download.php?content=1961
Source0:	1961-keramik.tgz
# Source0-md5:	bd381b99435683bd4e7ee1b96c522392
URL:		http://www.kde-look.org/content/show.php?content=1961
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	motif-devel
BuildRequires:	qt-devel >= 6:3.0.5
BuildRequires:	kdelibs-devel < 8:3.1
Requires:	kdelibs < 8:3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Keramik theme. To fully enjoy it set in Control Center, Look & Feel:
- Window decoration
- Style
- Color (menu)

%description -l pl.UTF-8
Motyw Keramik. Aby zobaczyć go w całej okazałości należy ustawić w
Centrum Sterowania, Look & Feal:
- Typ dekoracji okien
- Styl
- Kolor (menu)

%prep
%setup -q -n %{_theme}

%build
rm -f missing

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

KDEDIR=%{_prefix}
export KDEDIR

#make -f Makefile.cvs
%{__autoconf}
%configure \
	--with-motif

cd ./kdefx
%{__make}
cd ../kstyles/keramik
%{__make}
cd ../../kwin
%{__make}
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT

KDEDIR=%{_prefix}
export KDEDIR

cd ./kstyles/keramik
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../../kwin/clients/keramik
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../..

%post
/sbin/ldconfig
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.??
%{_libdir}/kde3/plugins/styles/*.??
%{_datadir}/apps/kwin/*
