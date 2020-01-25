#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	POE
%define		pnam	Component-CD-Rip
Summary:	POE::Component::CD::Rip - POE component for running cdparanoia, a CD ripper
Summary(pl.UTF-8):	POE::Component::CD::Rip - komponenty POE do ripowania CD przy pomocy cdparanoi
Name:		perl-POE-Component-CD-Rip
Version:	1.2
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5aeb2fed00d7f02e9bfb3e7b8a64720
URL:		http://search.cpan.org/dist/POE-Component-CD-Rip/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.22
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This POE component serves to rip tracks from a CD. At present it is
merely a wrapper for the cdparanoia program which does the bulk of the
work.

%description -l pl.UTF-8
Ten komponent POE służy do ripowania ścieżek z płyt CD. Aktualnie jest
to jedynie interfejs do programu cdparanoia, który wykonuje całą
pracę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/Component/CD/*
%{_mandir}/man3/*
