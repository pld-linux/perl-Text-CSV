#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	CSV
Summary:	Text::CSV - comma-separated values manipulator (using XS or PurePerl)
Summary(pl.UTF-8):	Text::CSV - obrabianie wartości oddzielonych przecinkami
Name:		perl-Text-CSV
Version:	1.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46267559f7f6e203e0a60e033c36851e
URL:		http://search.cpan.org/dist/Text-CSV/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-Text-CSV_XS
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values using Text::CSV_XS or its pure Perl version.

%description -l pl.UTF-8
Text::CSV ułatwia składanie i rozkład wartości oddzielanych
przecinkami przy użyciu Text::CSV_XS lub wersji w czystym Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Text/CSV

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/CSV.pm
%{perl_vendorlib}/Text/CSV_PP.pm
%{perl_vendorlib}/Text/CSV
%{_mandir}/man3/Text::CSV*.3pm*
