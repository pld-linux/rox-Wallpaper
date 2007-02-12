%include  /usr/lib/rpm/macros.python
%define _appsdir /usr/X11R6/share/ROX-apps
%define _name Wallpaper
Summary:	ROX-Wallpaper can be used to place an image on the background
Summary(pl.UTF-8):   ROX-Wallpaper może być użyty do ustawienia tapety
Name:		rox-%{_name}
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{_name}-%{version}.tgz
URL:		http://rox.sourceforge.net/wallpaper.php3
BuildRequires:	rpm-pythonprov
Requires:	ImageMagick
Requires:	python-pygtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program can be used to place an image on your desktop background.

%description -l pl.UTF-8
Ten program może być użyty do ustawienia obrazka jako tła.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

install App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/AutoStart.py
%attr(755,root,root) %{_appsdir}/%{_name}/no_display.py
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/[df]*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
