%define		_theme	keramik

Summary:	keramik theme
Summary(pl):	Temat keramik
Name:		kde-theme-%{_theme}
Version:	1
Release:	1
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
Windows-XP-like theme. To fully enjoy it set in Control Center, Look & Feel:
- Window decoration
- Style
- Color (menu)

%description -l pl
Temat przypominaj±cy Windows-XP. Aby zobaczyæ go w ca³ej okaza³o¶ci ustaw w 
Centrum Sterowania, Look & Feal:
- Typ dekoracji okien
- Styl
- Kolor (menu)

%prep
%setup  -q -n %{_theme}

%build
rm -f missing

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

KDEDIR=%{_prefix}
export KDEDIR

make -f Makefile.cvs
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.??
%{_libdir}/kde3/plugins/styles/*.??
%{_datadir}/apps/kwin/*
