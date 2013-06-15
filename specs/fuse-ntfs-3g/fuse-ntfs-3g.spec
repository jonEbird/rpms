# $Id$
# Authority: dag

%define _sbindir /sbin

### EL5 and older has too old gnutls :-/
%{?el5:%define _without_crypto 1}
%{?el4:%define _without_crypto 1}
%{?el3:%define _without_crypto 1}
%{?rh9:%define _without_crypto 1}
%{?rh7:%define _without_crypto 1}
%{?el2:%define _without_crypto 1}

%define real_name ntfs-3g_ntfsprogs

Summary: Linux NTFS userspace driver 
Name: fuse-ntfs-3g
Version: 2013.1.13
Release: 1%{dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.ntfs-3g.org/

#Source: http://www.ntfs-3g.org/ntfs-3g-%{version}.tgz
#Source: http://tuxera.com/opensource/ntfs-3g-%{version}.tgz
Source: http://tuxera.com/opensource/ntfs-3g_ntfsprogs-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.6.3
BuildRequires: gcc-c++
%{!?_without_crypto:BuildRequires: libgcrypt-devel, gnutls >= 1.2.8}
%{!?_without_gnomevfs:BuildRequires: glib2-devel, gnome-vfs2-devel}
Requires: fuse >= 2.6.3

Provides: ntfs-3g = %{version}-%{release}
Obsoletes: ntfs-3g <= %{version}-%{release}

%description
The ntfs-3g driver is an open source, GPL licensed, third generation Linux NTFS
driver. It provides full read-write access to NTFS, excluding access to
encrypted files, writing compressed files, changing file ownership, access
right.

Technically it’s based on and a major improvement to the third generation Linux
NTFS driver, ntfsmount. The improvements include functionality, quality and
performance enhancements.

ntfs-3g features are being merged to ntfsmount. In the meanwhile, ntfs-3g is
currently the only free, as in either speech or beer, NTFS driver for Linux
that supports unlimited file creation and deletion.

%package -n ntfsprogs
Summary: NTFS filesystem libraries and utilities
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Provides: ntfsprogs = %{version}-%{release}
Obsoletes: ntfsprogs <= %{version}-%{release}
Provides: ntfsprogs-fuse = %{version}-%{release}
Obsoletes: ntfsprogs-fuse <= %{version}-%{release}

%description -n ntfsprogs
The Linux-NTFS project aims to bring full support for the NTFS filesystem
to the Linux operating system. Linux-NTFS currently consists of a static
library and utilities such as mkntfs, ntfscat, ntfsls, ntfsresize, and
ntfsundelete (for a full list of included utilities see man 8 ntfsprogs).

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: ntfs-3g-devel <= %{version}-%{release}
Provides: ntfs-3g-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --disable-ldconfig \
    --disable-static \
%{!?_without_crypto:--enable-crypto} \
    --enable-extras \
%{!?_without_gnomevfs:--enable-gnome-vfs} \
    --enable-mount-helper
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Symlink different locations
%{__ln_s} %{_bindir}/ntfs-3g %{buildroot}%{_sbindir}/mount.ntfs
%{__ln_s} %{_bindir}/ntfs-3g %{buildroot}%{_bindir}/ntfsmount

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* CREDITS NEWS README
%doc %{_mandir}/man8/mount.ntfs-3g.8*
%doc %{_mandir}/man8/mount.lowntfs-3g.8*
%doc %{_mandir}/man8/ntfs-3g.8*
%doc %{_mandir}/man8/ntfs-3g.probe.8*
%doc %{_mandir}/man8/ntfs-3g.secaudit.8*
%doc %{_mandir}/man8/ntfs-3g.usermap.8*
%{_bindir}/lowntfs-3g
%{_bindir}/ntfs-3g
%{_bindir}/ntfs-3g.probe
%{_bindir}/ntfs-3g.secaudit
%{_bindir}/ntfs-3g.usermap
%{_bindir}/ntfsmount
%{_libdir}/libntfs-3g.so.*
%{_sbindir}/mount.lowntfs-3g
%{_sbindir}/mount.ntfs
%{_sbindir}/mount.ntfs-3g
%exclude %{_docdir}/ntfs-3g/

%files -n ntfsprogs
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/mkfs.ntfs.8.gz
%doc %{_mandir}/man8/mkntfs.8.gz
%doc %{_mandir}/man8/ntfscat.8.gz
%doc %{_mandir}/man8/ntfsclone.8.gz
%doc %{_mandir}/man8/ntfscluster.8.gz
%doc %{_mandir}/man8/ntfscmp.8.gz
%doc %{_mandir}/man8/ntfscp.8.gz
%doc %{_mandir}/man8/ntfsfix.8.gz
%doc %{_mandir}/man8/ntfsinfo.8.gz
%doc %{_mandir}/man8/ntfslabel.8.gz
%doc %{_mandir}/man8/ntfsls.8.gz
%doc %{_mandir}/man8/ntfsprogs.8.gz
%doc %{_mandir}/man8/ntfsresize.8.gz
%doc %{_mandir}/man8/ntfsundelete.8.gz
%{_sbindir}/mkfs.ntfs
%{_sbindir}/mkntfs
%{_bindir}/ntfscat
%{_bindir}/ntfsck
%{_bindir}/ntfscluster
%{_bindir}/ntfscmp
%{!?_without_crypto:%{_bindir}/ntfsdecrypt}
%{_bindir}/ntfsdump_logfile
%{_bindir}/ntfsfix
%{_bindir}/ntfsinfo
%{_bindir}/ntfsls
%{_bindir}/ntfsmftalloc
%{_bindir}/ntfsmove
%{_bindir}/ntfstruncate
%{_bindir}/ntfswipe
%{_sbindir}/ntfsclone
%{_sbindir}/ntfscp
%{_sbindir}/ntfslabel
%{_sbindir}/ntfsresize
%{_sbindir}/ntfsundelete

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so
%{_libdir}/pkgconfig/libntfs-3g.pc
%exclude %{_libdir}/libntfs-3g.la

%changelog
* Fri Feb 15 2013 Dag Wieers <dag@wieers.com> - 2013.1.13-1
- Updated to release 2013.1.13.

* Sun Oct 31 2010 Dag Wieers <dag@wieers.com> - 2010.10.2-1
- Updated to release 2010.10.2.

* Sun Jun 20 2010 Dag Wieers <dag@wieers.com> - 2010.5.22-1
- Updated to release 2010.5.22.

* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 2009.11.14-1
- Updated to release 2009.11.14.

* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 2009.4.4-2
- Added symlink for mount.ntfs so Gnome's Disk Mounter applet doesn't crash.

* Tue May 05 2009 Dag Wieers <dag@wieers.com> - 2009.4.4-1
- Updated to release 2009.4.4.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2009.2.1-1
- Updated to release 2009.2.1.

* Sat Jan 24 2009 Dag Wieers <dag@wieers.com> - 2009.1.1-1
- Updated to release 2009.1.1.

* Mon Dec 01 2008 Dag Wieers <dag@wieers.com> - 1.5130-1
- Updated to release 1.5130.

* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 1.5012-1
- Updated to release 1.5012.

* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 1.2918-1
- Updated to release 1.2918.

* Thu Aug 28 2008 Dag Wieers <dag@wieers.com> - 1.2812-1
- Updated to release 1.2812.

* Mon Jul 14 2008 Dag Wieers <dag@wieers.com> - 1.2712-1
- Updated to release 1.2712.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 1.2531-1
- Updated to release 1.2531.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 1.2506-1
- Updated to release 1.2506.

* Thu Apr 17 2008 Dag Wieers <dag@wieers.com> - 1.2412-1
- Updated to release 1.2412.

* Wed Mar 12 2008 Dag Wieers <dag@wieers.com> - 1.2310-1
- Updated to release 1.2310.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 1.2216-1
- Updated to release 1.2216.

* Tue Nov 20 2007 Dag Wieers <dag@wieers.com> - 1.1120-1
- Updated to release 1.1120.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.1104-1
- Updated to release 1.1104.

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 1.1030-1
- Updated to release 1.1030.

* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 1.1004-1
- Updated to release 1.1004.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 1.913-1
- Updated to release 1.913.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 1.616-1
- Updated to release 1.616.

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.417-2
- Symlink mount binaries instead of hardlink (different mountpoints). (Jon Wilson)

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.417-1
- Initial package. (using DAR)
