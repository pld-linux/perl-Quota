%include	/usr/lib/rpm/macros.perl
Summary:	Quota perl module
Summary(pl):	Modu³ perla Quota
Name:		perl-Quota
Version:	1.3.2
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Quota/Quota-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quota perl module.

%description -l pl
Modu³ perla Quota.

%prep
%setup -q -n Quota-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a contrib $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Quota.pm
%dir %{perl_sitearch}/auto/Quota
%{perl_sitearch}/auto/Quota/autosplit.ix
%{perl_sitearch}/auto/Quota/Quota.bs
%attr(755,root,root) %{perl_sitearch}/auto/Quota/Quota.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
