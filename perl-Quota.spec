%include	/usr/lib/rpm/macros.perl
Summary:	Quota perl module
Summary(pl):	Modu³ perla Quota
Name:		perl-Quota
Version:	1.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Quota/Quota-%{version}.tar.gz
Patch:		perl-Quota-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

cp -a contrib $RPM_BUILD_ROOT/usr/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Quota/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Quota
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz

%{perl_sitearch}/Quota.pm

%dir %{perl_sitearch}/auto/Quota
%{perl_sitearch}/auto/Quota/.packlist
%{perl_sitearch}/auto/Quota/autosplit.ix
%{perl_sitearch}/auto/Quota/Quota.bs
%attr(755,root,root) %{perl_sitearch}/auto/Quota/Quota.so

%{_mandir}/man3/*

/usr/src/examples/%{name}
