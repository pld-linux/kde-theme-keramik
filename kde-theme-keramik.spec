%define		_theme	keramik

Summary:	keramik theme
Summary(pl):	Temat keramik
Name:		kde-theme-%{_theme}
Version:	1
Release:	0.1
License:	GPL
Group:		Themes/Gtk
#Source0:	http://www.kde-look.org/content/download.php?content=1961
Source0:	1961-keramik.tgz
URL:		http://www.kde-look.org/content/show.php?content=1961
Requires:	kdelibs
BuildRequires:	motif-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define         _htmldir        /usr/share/doc/kde/HTML

%description
Windows-XP-like theme.

%description -l pl
Temat przypominaj±cy Windows-XP.

%prep
%setup  -q -n %{_theme}

%build
rm -f missing

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

make -f Makefile.cvs
%configure

cd ./kdefx
%{__make}
cd ../kstyles/keramik
%{__make}
cd ../../kwin
%{__make}
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT

cd ./kstyle/keramik
%{__make} install
cd ../../clients/keramik
%{__make} install
cd ../..

#install -d $RPM_BUILD_ROOT/{%{_datadir}/{apps/kstyle,apps/kthememgr/Themes,apps/kwin/icewm-themes},%{_pixmapsdir}}
#
#cp -pR style/{pixmaps,themes}	$RPM_BUILD_ROOT%{_datadir}/apps/kstyle
#cp -pR style/wallpapers/*	$RPM_BUILD_ROOT%{_pixmapsdir}
#
#cp -pR theme/Acqua.ktheme	$RPM_BUILD_ROOT%{_datadir}/apps/kthememgr/Themes
#cp -pR theme/%{_theme}		$RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kstyle/pixmaps/*
%{_datadir}/apps/kstyle/themes/*
%{_pixmapsdir}/*
%{_datadir}/apps/kthememgr/Themes/*
%{_datadir}/apps/kwin/icewm-themes/*
