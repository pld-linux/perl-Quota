#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Quota
%define		pnam	Quota
Summary:	Quota - Perl interface to file system quotas
Summary(pl):	Quota - perlowy interfejs do quot systemów plików
Name:		perl-Quota
Version:	1.4.6
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Quota module provides access to file system quotas.  The quotactl
system call or ioctl is used to query or set quotas on the local host,
or queries are submitted via RPC to a remote host.  Mount tables can
be parsed with getmntent and paths can be translated to device files
(or whatever the actual quotactl implementations needs as argument)
of the according file system.

%description -l pl
Modu³ Quota daje dostêp do quot systemów plików. U¿ywa wywo³añ
systemowych quotactl lub ioctl do sprawdzania lub ustawiania quot
lokalnych lub przesy³a zapytania po RPC do zdalnej maszyny. Tablice
montowanych partycji mog± byæ analizowane poprzez getmntent, a ¶cie¿ki
t³umaczone na pliki urz±dzeñ (lub cokolwiek, czego dana implementacja
quotactl wymaga jako parametru) odpowiadaj±cych im systemów plików.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

# test is interactive
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -af contrib/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitearch}/Quota.pm
%dir %{perl_sitearch}/auto/Quota
%{perl_sitearch}/auto/Quota/autosplit.ix
%{perl_sitearch}/auto/Quota/Quota.bs
%attr(755,root,root) %{perl_sitearch}/auto/Quota/Quota.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/[Rqr]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
