#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-CD-Rip
Summary:	POE::Component::CD::Rip - POE Component for running cdparanoia, a CD ripper.
#Summary(pl):	
Name:		perl-POE-Component-CD-Rip
Version:	1.2
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.22
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This POE component serves to rip tracks from a CD.  At present it is
merely a wrapper for the B<cdparanoia> program which does the bulk of
the work.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
