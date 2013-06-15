# $Id$
# Authority: dag
# Upstream: Glenn Randers-Pehrson <glennrp$users,sf,net>

Summary: Optimizer for PNG (Portable Network Graphics) files
Name: pngcrush
Version: 1.7.53
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://pmt.sourceforge.net/pngcrush/

#Source: http://dl.sf.net/pmt/pngcrush-%{version}.tar.bz2
Source: http://dl.sf.net/pmt/pngcrush/%{version}/pngcrush-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, zlib-devel

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can be
run from a commandline in an MSDOS window, or from a UNIX or LINUX commandline.

Its main purpose is to reduce the size of the PNG IDAT datastream by trying
various compression levels an PNG filter methods. It also can be used to
remove unwanted ancillary chunks, or to add certain chunks including gAMA,
tRNS, iCCP, and textual chunks. 

%prep
%setup

%build
%{__make} %{?_smp_mflags} CC="%{__cc}" LD="%{__cc}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -D -m0755 pngcrush %{buildroot}%{_bindir}/pngcrush

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html
%{_bindir}/pngcrush

%changelog
* Wed Mar 20 2013 Dag Wieers <dag@wieers.com> - 1.7.53-1
- Updated to release 1.7.53.

* Thu Oct 25 2012 Dag Wieers <dag@wieers.com> - 1.7.41-1
- Updated to release 1.7.41.

* Sun Sep 23 2012 Dag Wieers <dag@wieers.com> - 1.7.27-1
- Updated to release 1.7.37.

* Wed Aug 01 2012 Dag Wieers <dag@wieers.com> - 1.7.35-1
- Updated to release 1.7.35.

* Mon Oct 24 2011 Dag Wieers <dag@wieers.com> - 1.7.20-1
- Updated to release 1.7.20.

* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 1.7.2-1
- Updated to release 1.7.2.

* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Updated to release 1.7.0.

* Fri Jul 17 2009 Dag Wieers <dag@wieers.com> - 1.6.20-1
- Updated to release 1.6.20.

* Thu Jun 18 2009 Dag Wieers <dag@wieers.com> - 1.6.19-1
- Updated to release 1.6.19.

* Sun May 10 2009 Dag Wieers <dag@wieers.com> - 1.6.17-1
- Updated to release 1.6.17.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 1.6.14-1
- Updated to release 1.6.14.

* Wed Aug 27 2008 Dag Wieers <dag@wieers.com> - 1.6.10-1
- Updated to release 1.6.10.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 1.6.7-1
- Updated to release 1.6.7.

* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 1.6.6-1
- Updated to release 1.6.6.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.6.5-1
- Updated to release 1.6.5.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 1.6.4-1
- Initial package. (using DAR)
