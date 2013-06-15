# $Id$
# Authority: dag
# Upstream: Jens Axboe

Summary: I/O benchmark and stress/hardware verification tool
Name: fio
Version: 2.0.14
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://freshmeat.net/projects/fio/

Source: http://brick.kernel.dk/snaps/fio-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libaio-devel

%description
fio is an I/O tool meant to be used both for benchmark and stress/hardware
verification. It has support for 6 different types of I/O engines (sync,
mmap, libaio, posixaio, SG v3, splice), I/O priorities (for newer Linux
kernels), rate I/O, forked or threaded jobs, and much more.

It can work on block devices as well as files. fio accepts job descriptions
in a simple-to-understand text format. Several example job files are included.
fio displays all sorts of I/O performance information, such as completion and
submission latencies (avg/mean/deviation), bandwidth stats, CPU, and disk
utilization, and more. It supports Linux, FreeBSD, and OpenSolaris.

%prep
%setup

#%{__perl} -pi -e 's| \$\(libdir\)| \$(DESTDIR)\$(libdir)|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" bindir="%{_bindir}" libdir="%{_libdir}/fio"
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" bindir="%{_bindir}" mandir="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README examples/
%doc %{_mandir}/man1/fio.1*
%doc %{_mandir}/man1/fio_generate_plots.1*
%{_bindir}/fio
%{_bindir}/fio_generate_plots
#%{_libdir}/fio/

%changelog
* Wed Mar 20 2013 Dag Wieers <dag@wieers.com> - 2.0.14-1
- Updated to release 2.0.14.

* Tue Feb 12 2013 Dag Wieers <dag@wieers.com> - 2.0.13-1
- Updated to release 2.0.13.

* Thu Oct 25 2012 Dag Wieers <dag@wieers.com> - 2.0.10-1
- Updated to release 2.0.10.

* Thu Aug 30 2012 Dag Wieers <dag@wieers.com> - 2.0.9-1
- Updated to release 2.0.9.

* Sun Apr 08 2012 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.

* Sun Mar 11 2012 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Tue Feb 07 2012 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Fri Sep 16 2011 Dag Wieers <dag@wieers.com> - 1.58-1
- Updated to release 1.58.

* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.57-1
- Updated to release 1.57.

* Tue Jun 07 2011 Dag Wieers <dag@wieers.com> - 1.55-1
- Updated to release 1.55.

* Fri May 13 2011 Dag Wieers <dag@wieers.com> - 1.54-1
- Updated to release 1.54.

* Wed May 11 2011 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Mon May 02 2011 Dag Wieers <dag@wieers.com> - 1.52-1
- Updated to release 1.52.

* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 1.50-1
- Updated to release 1.50.

* Fri Jun 18 2010 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 1.39-1
- Updated to release 1.39.

* Wed Mar 31 2010 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 1.37-1
- Updated to release 1.37.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Fri Nov 13 2009 Dag Wieers <dag@wieers.com> - 1.35-1
- Updated to release 1.35.

* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 1.31-1
- Updated to release 1.31.

* Sat Jul 04 2009 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Sat Jun 06 2009 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Sun Apr 26 2009 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Sat Oct 11 2008 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sun Feb 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.18.1-1
- Updated to release 1.18.1.

* Tue Feb  5 2008 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Thu Jan 31 2008 Dries Verachtert <dries@ulyssis.org> - 1.17.3-1
- Updated to release 1.17.3.

* Tue Oct 30 2007 Dag Wieers <dag@wieers.com> - 1.17.2-1
- Updated to release 1.17.2.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 1.16.5-1
- Updated to release 1.16.5.

* Wed Apr 25 2007 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Wed Mar 28 2007 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Mon Oct 23 2006 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Wed Aug 30 2006 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
