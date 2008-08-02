%define name rzip
%define version 2.1
%define release %mkrel 5

Name: %{name}
Summary: Compression program, similar in functionality to gzip or bzip2
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
URL: http://rzip.samba.org/
Group: Archiving/Compression
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bzip2-devel

%description
rzip is a compression program, similar in functionality to gzip or bzip2,
but able to take advantage long distance redundencies in files, which can
sometimes allow rzip to produce much better compression ratios than other
programs.
The principal advantage of rzip is that it has an effective history
buffer of 900 Mbyte. This means it can find matching pieces of the input
file over huge distances compared to other commonly used compression
programs. The gzip program by comparison uses a history buffer of 32
kbyte and bzip2 uses a history buffer of 900 kbyte. The second advantage
of rzip over bzip2 is that it is usually faster.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc COPYING
%{_mandir}/man1/rzip.1*
%{_bindir}/rzip

