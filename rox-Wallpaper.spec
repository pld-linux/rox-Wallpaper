%define _name Wallpaper
Summary:	ROX-Wallpaper can be used to place an image on the background
Summary(pl.UTF-8):   ROX-Wallpaper może być użyty do ustawienia tapety
Name:		rox-%{_name}
Version:	1.9.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/wallpaper-%{version}.tgz
# Source0-md5:	24c1671389897150ca330dd234d8f166
URL:		http://rox.sourceforge.net/phpwiki/index.php/Wallpaper
Requires:	ImageMagick
Requires:	python-pygtk-gtk
Requires:	rox >= 2.2.0-2
Requires:	rox-Lib2
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
This program can be used to place an image on your desktop background.

%description -l pl.UTF-8
Ten program może być użyty do ustawienia obrazka jako tła.

%prep
%setup -q -n wallpaper-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

cd %{_name}
install .DirIcon App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
