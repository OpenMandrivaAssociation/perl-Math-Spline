%define upstream_name    Math-Spline
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Cubic Spline Interpolation of data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/Math-Spline-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Math::Derivative)
BuildArch:	noarch

%description
This package provides cubic spline interpolation of numeric data. The data is
passed as references to two arrays containing the x and y ordinates. It may be
used as an exporter of the numerical functions or, more easily as a class
module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 403859
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-10mdv2009.0
+ Revision: 257816
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-9mdv2009.0
+ Revision: 245842
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-7mdv2008.1
+ Revision: 136284
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-7mdv2008.0
+ Revision: 86636
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-5mdk
- Fix According to perl Policy
    - Source URL
- use mkrel

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdk 
- better url
- spec cleanup
- don't ship empty directories
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk 
- rpmbuildupdate aware

* Mon Jan 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk
- first mdk release


