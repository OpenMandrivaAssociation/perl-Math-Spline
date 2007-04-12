%define module  Math-Spline
%define name    perl-%{module}
%define version 0.01
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Cubic Spline Interpolation of data
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This package provides cubic spline interpolation of numeric data. The data is
passed as references to two arrays containing the x and y ordinates. It may be
used as an exporter of the numerical functions or, more easily as a class
module.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*

