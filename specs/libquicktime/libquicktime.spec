# $Id$
# Authority: matthias
# Upstream: <libquicktime-devel$lists,sourceforge,net>

%{?dist: %{expand: %%define %dist 1}}

# We want to explicitely disable MMX for ppc, x86_64 etc.
%ifnarch %{ix86}
    %define _without_mmx 1
%endif

#define prever pre1

Summary: Library for reading and writing quicktime files
Name: libquicktime
Version: 0.9.3
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: System Environment/Libraries
URL: http://libquicktime.sourceforge.net/
Source: http://dl.sf.net/libquicktime/libquicktime-%{version}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, libdv-devel, libvorbis-devel
BuildRequires: libpng-devel >= 1.0.8, libjpeg-devel
%{?!dist:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?fc2:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?fc1:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?el3:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?rh9:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?rh8:BuildRequires: libraw1394-devel, libavc1394-devel}

# The configure automatically adds MMX stuff if detected, so x86 becomes i586
%ifarch %{ix86}
%{!?_without_mmx:BuildArch: i586}
%endif

%description
Libquicktime is a library for reading and writing QuickTime files
on UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library.  Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.


%package devel
Summary: Development files from the libquicktime library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with many extensions.

You will need to install this development package if you intend to rebuild
programs that need to access quicktime files using libquicktime.


%prep
%setup -n %{name}-%{version}%{?prever}

%{__perl} -pi.orig -e '
    s|\$exec_prefix/lib|\$libdir|g;
    s|(OPTIMIZE_CFLAGS)="-O3|$1="%{optflags}|;
    ' configure.ac

%build
./autogen.sh
%configure \
    --enable-static \
    %{?_without_mmx:--disable-mmx}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/lqtplay
%{_bindir}/lqt_transcode
%{_bindir}/qt*
%{_libdir}/*.so.*
%dir %{_libdir}/libquicktime/
%{_libdir}/libquicktime/*.so
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/libquicktime_config
%{_bindir}/lqt-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%dir %{_libdir}/libquicktime/
%{_libdir}/%{name}/*.a
%exclude %{_libdir}/%{name}/*.la
%{_datadir}/aclocal/*.m4


%changelog
* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.9.2-3
- Fixes for x86_64 from MandrakeCooker.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-3
- Rebuild for Fedora Core 1.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-2
- Rebuild against new libdv.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Update to 0.9.2 final.
- Rebuild for Fedora Core 1.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Fix plugin compilation, thanks to Dag.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

