# $Id$
# Authority: dag

Summary: tool for computing context triggered piecewise hashes (CTPH)
Name: ssdeep
Version: 2.9
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://ssdeep.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%description
Computes a checksum based on context triggered piecewise hashes for
each input file. If requested, the program matches those checksums
against a file of known checksums and reports any possible matches.
Output is written to standard out and errors to standard error.
Input from standard input is not supported.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING FILEFORMAT INSTALL NEWS README TODO
%doc %{_mandir}/man1/ssdeep.1*
%{_bindir}/ssdeep
%{_includedir}/fuzzy.h
%{_libdir}/libfuzzy.*

%changelog
* Fri Oct 19 2012 Richard Harman <rpm+ssdeep@richardharman.com>
- Update to ssdeep 2.9 and build/install shared libraries
