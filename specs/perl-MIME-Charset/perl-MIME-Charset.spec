# $Id$
# Authority: dries
# Upstream: IKEDA Soji <hatuka$nezumi,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Charset

Summary: Charset Informations for MIME
Name: perl-MIME-Charset
Version: 1.010
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Charset/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Charset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode) >= 1.98
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Encode) >= 1.98
Requires: perl >= 5.005
Requires: perl(ExtUtils::MakeMaker)

%filter_from_requires /^perl*/d
%filter_setup

%description
Charset Informations for MIME.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::Charset.3pm*
%doc %{_mandir}/man3/MIME::Charset::JA_JP.3pm*
%dir %{perl_vendorlib}/MIME/
%{perl_vendorlib}/MIME/Charset/
%{perl_vendorlib}/MIME/Charset.pm

%changelog
* Mon Jun 24 2013 David Hrbáč <david@hrbac.cz> - 1.010-1
- new upstream release

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 1.008-1
- Updated to version 1.008.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.007.1-1
- Updated to version 1.007.1.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.006.2-1
- Updated to release 1.006.2.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.000-1
- Updated to release 1.000.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.044-1
- Updated to release 0.044.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.043-1
- Initial package.
