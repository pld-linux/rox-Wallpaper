%include  /usr/lib/rpm/macros.python
%define _name Wallpaper
Summary:	ROX-Wallpaper can be used to place an image on the background
Summary(pl):	ROX-Wallpaper mo¿e byæ u¿yty do ustawienia tapety
Name:		rox-%{_name}
Version:	0.1.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
URL:		http://rox.sourceforge.net/wallpaper.php3
BuildRequires:	rpm-pythonprov
Requires:	ImageMagick
Requires:	python-pygtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _appsdir  %{_libdir}/ROX-apps

%description
This program can be used to place an image on your desktop background.

%description -l pl
Ten program mo¿e byæ u¿yty do ustawienia obrazka jako t³a.

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
