%include	/usr/lib/rpm/macros.perl
%define		pdir	Quota
%define		pnam	Quota
Summary:	Quota Perl module
Summary(cs):	Modul Quota pro Perl
Summary(da):	Perlmodul Quota
Summary(de):	Quota Perl Modul
Summary(es):	M�dulo de Perl Quota
Summary(fr):	Module Perl Quota
Summary(it):	Modulo di Perl Quota
Summary(ja):	Quota Perl �⥸�塼��
Summary(ko):	Quota �� ����
Summary(no):	Perlmodul Quota
Summary(pl):	Modu� perla Quota
Summary(pt_BR):	M�dulo Perl Quota
Summary(pt):	M�dulo de Perl Quota
Summary(ru):	������ ��� Perl Quota
Summary(sv):	Quota Perlmodul
Summary(uk):	������ ��� Perl Quota
Summary(zh_CN):	Quota Perl ģ��
Name:		perl-Quota
Version:	1.4.4
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quota perl module.

%description -l pl
Modu� perla Quota.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -af contrib $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
