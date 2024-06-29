#
# Conditional build:
%bcond_with	qt5	# Qt5 instead of Qt6

Summary:	Ampache desktop client library
Summary(pl.UTF-8):	Biblioteka graficznego klienta Ampache
Name:		ampache_browser
Version:	1.0.7
Release:	1
License:	GPL v3
Group:		Libraries
#Source0Download: https://github.com/ampache-browser/ampache_browser/releases
Source0:	https://github.com/ampache-browser/ampache_browser/archive/v%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	8f106232fc0d0e7b13685d65e825bd73
URL:		https://github.com/ampache-browser/ampache_browser
%if %{with qt5}
BuildRequires:	Qt5Concurrent-devel >= 5
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
%else
BuildRequires:	Qt6Concurrent-devel >= 6
BuildRequires:	Qt6Core-devel >= 6
BuildRequires:	Qt6Widgets-devel >= 6
%endif
BuildRequires:	cmake >= 3.13
BuildRequires:	libstdc++-devel >= 6:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ampache Browser is a library that implements desktop client for
Ampache (<http://ampache.org/>). It provides end-user Qt UI and has a
simple C++ interface that allows easy integration to a client
application.

%description -l pl.UTF-8
Ampache Browser to biblioteka implementująca graficznego klienta
Ampache (<http://ampache.org/>). Udostępnia oparty na Qt interfejs
użytkownika i ma prosty interfejs C++, pozwalający na łatwą integrację
z aplikacją kliencką.

%package devel
Summary:	Header files for Ampache Browser library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ampache Browser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for Ampache Browser library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ampache Browser.

%prep
%setup -q -n ampache_browser-%{version}

%build
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	%{?with_qt5:-DUSE_QT6=OFF}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libampache_browser_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libampache_browser_1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libampache_browser_1.so
%{_includedir}/ampache_browser_1
%{_pkgconfigdir}/ampache_browser_1.pc
%{_libdir}/cmake/ampache_browser_1
