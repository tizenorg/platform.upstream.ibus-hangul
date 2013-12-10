%define mod_path ibus-1.4
Name:       ibus-hangul
Version:    1.4.2
Release:    1
Summary:    The Hangul engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1001: ibus-hangul.manifest

BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libhangul)

Requires:   ibus

%description
The Hangul engine for IBus platform. It provides Korean input method from
libhangul.

%prep
%setup -q
cp %{SOURCE1001} .


%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_bindir}/ibus-setup-hangul
sed -i 's!^Exec=ibus-setup-hangul!Exec=%{_libexecdir}/ibus-setup-hangul!' ${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-hangul.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%manifest %{name}.manifest
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*
%{_libdir}/ibus-hangul/setup/*
%{_datadir}/applications/ibus-setup-hangul.desktop
%{_datadir}/icons/hicolor/*/apps/*
