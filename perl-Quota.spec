%include	/usr/lib/rpm/macros.perl
Summary:	Quota perl module
Summary(pl):	Modu³ perla Quota
Name:		perl-Quota
Version:	1.4.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Quota/Quota-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quota perl module.

%description -l pl
Modu³ perla Quota.

%prep
%setup -q -n Quota-%{version}
%patch0 -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a contrib $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{_examplesdir}/%{name}-%{version}
