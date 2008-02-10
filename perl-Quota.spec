#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# interactive
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Quota
%define		pnam	Quota
Summary:	Quota - Perl interface to file system quotas
Summary(pl.UTF-8):	Quota - perlowy interfejs do quot systemów plików
Name:		perl-Quota
Version:	1.5.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	6a4887f5aadf34e8d49d067cc78d579a
Patch0:		%{name}-paths.patch
Patch1:		%{name}-pic.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Quota module provides access to file system quotas.  The quotactl
system call or ioctl is used to query or set quotas on the local host,
or queries are submitted via RPC to a remote host.  Mount tables can
be parsed with getmntent and paths can be translated to device files
(or whatever the actual quotactl implementations needs as argument)
of the according file system.

%description -l pl.UTF-8
Moduł Quota daje dostęp do quot systemów plików. Używa wywołań
systemowych quotactl lub ioctl do sprawdzania lub ustawiania quot
lokalnych lub przesyła zapytania po RPC do zdalnej maszyny. Tablice
montowanych partycji mogą być analizowane poprzez getmntent, a ścieżki
tłumaczone na pliki urządzeń (lub cokolwiek, czego dana implementacja
quotactl wymaga jako parametru) odpowiadających im systemów plików.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

# test is interactive
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -af contrib/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/%{pdir}.pm
%dir %{perl_vendorarch}/auto/%{pdir}
%{perl_vendorarch}/auto/%{pdir}/autosplit.ix
%{perl_vendorarch}/auto/%{pdir}/%{pdir}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pdir}.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/[Rqr]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
