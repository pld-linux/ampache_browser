Summary:	Ampache desktop client library
Summary(pl.UTF-8):	Biblioteka graficznego klienta Ampache
Name:		ampache_browser
Version:	1.0.3
Release:	1
License:	GPL v3
Group:		Libraries
#Source0Download: https://github.com/ampache-browser/ampache_browser/releases
Source0:	https://github.com/ampache-browser/ampache_browser/archive/v%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	23f9cca4171662e4ecaa7aa51f4ccd0b
URL:		https://github.com/ampache-browser/ampache_browser
BuildRequires:	Qt5Concurrent-devel >= 5
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel >= 6:4.7
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
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for Ampache Browser library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ampache Browser.

%prep
%setup -q -n ampache_browser-%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

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
