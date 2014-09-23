%define mod_path ibus-1.4
Name:       ibus-hangul
Version:    1.4.2
Release:    0
Summary:    The Hangul engine for IBus input platform
License:    GPL-2.0+
Group:      System/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1001: ibus-hangul.manifest

BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libhangul)
BuildRequires:  fdupes

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
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

rm -f %{buildroot}%{_bindir}/ibus-setup-hangul
sed -i 's!^Exec=ibus-setup-hangul!Exec=%{_libexecdir}/ibus-setup-hangul!' %{buildroot}%{_datadir}/applications/ibus-setup-hangul.desktop

%find_lang %{name}
%fdupes %{buildroot}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%manifest %{name}.manifest
%license COPYING
%doc AUTHORS README
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*
%{_libdir}/ibus-hangul/setup/*
%{_datadir}/applications/ibus-setup-hangul.desktop
%{_datadir}/icons/hicolor/*/apps/*

