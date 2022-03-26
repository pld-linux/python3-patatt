Summary:	Simple library to add cryptographic attestation to patches sent via email
Summary(pl.UTF-8):	Prosta biblioteka dodająca kryptograficzne poświadczenie do łatek wysyłanych pocztą
Name:		python3-patatt
Version:	0.4.9
Release:	3
License:	MIT-0
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/devel/patatt/patatt-%{version}.tar.xz
# Source0-md5:	d7f3beccdc4babc7b2497a251f34800e
URL:		https://pypi.org/project/patatt/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility allows an easy way to add end-to-end cryptographic
attestation to patches sent via mail. It does so by adapting the DKIM
email signature standard to include cryptographic signatures via the
X-Developer-Signature email header.

%description -l pl.UTF-8
To narzędzie umożliwia w łatwy sposób dodawać poświadczenia
kryptograficzne do łatek przesyłanych pocztą elektroniczną. Zostało to
osiągnięte przez zaadaptowanie standardu podpisów listów DKIM do
dołączania podpisów kryptograficznych poprzez nagłówek
X-Developer-Signature.

%prep
%setup -q -n patatt-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.rst
%attr(755,root,root) %{_bindir}/patatt
%{py3_sitescriptdir}/patatt
%{py3_sitescriptdir}/patatt-%{version}-py*.egg-info
%{_mandir}/man5/patatt.5*
