%define	name	rzip
%define	version	2.1
%define release	9

Name:		%{name}
Summary:	Compression program, similar in functionality to gzip or bzip2
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
URL:		https://rzip.samba.org/
Group:		Archiving/Compression
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	bzip2-devel

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
%configure2_5x
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



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-8mdv2011.0
+ Revision: 614802
- the mass rebuild of 2010.1 packages

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1-7mdv2010.1
+ Revision: 510385
- Use configure2_5x
- Fix mixed of spaces and tabs

* Mon Jun 22 2009 Jérôme Brenier <incubusss@mandriva.org> 2.1-6mdv2010.0
+ Revision: 388006
- fix license tag

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2.1-5mdv2009.0
+ Revision: 260477
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 2.1-4mdv2009.0
+ Revision: 251856
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1-2mdv2008.1
+ Revision: 171086
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.1-1mdv2008.1
+ Revision: 126917
- kill re-definition of %%buildroot on Pixel's request
- import rzip


* Sat May 13 2006 Emmanuel Andry <eandry@mandriva.org> 2.1-1mdk
- 2.1
- mkrel

* Fri Jul 22 2005 Lenny Cartier <lenny@mandriva.com> 2.0-2mdk
- rebuild

* Thu May 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0-1mdk
- from Robert Weiler <mdk-rpms@robwei.de> : 
	- First build of rzip for Mandrake
