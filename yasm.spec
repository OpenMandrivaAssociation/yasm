Summary:	Modular Assembler
Name:		yasm
Version:	1.2.0
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://www.tortall.net/projects/yasm/
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz
BuildRequires:	xmlto
BuildRequires:	python-pyrex > 0.9.5.1
BuildRequires:  python-cython
BuildRequires:  python-devel
%if %{mdkversion} <= 200710
BuildRequires:	lzma
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD
License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%package devel
Summary:	Development headers and files for %{name}
Group:		Development/C
Obsoletes:	%mklibname -d yasm 0
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and files for %{name}.

%package python
Summary:	Python bindings for %{name}
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

%description python
Python bindings for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%ifnarch ix86
export CFLAGS="%{optflags} -fPIC"
%endif

%configure2_5x \
	--disable-rpath \
	--enable-python \
	--enable-python-bindings

%make

%install
rm -rf  %{buildroot}

%makeinstall_std

rm -f %{buildroot}%{_libdir}/yasm/*.a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man1/yasm.1*
%{_mandir}/man7/yasm_arch.7*
%{_mandir}/man7/yasm_dbgfmts.7.*
%{_mandir}/man7/yasm_objfmts.7.*
%{_mandir}/man7/yasm_parsers.7.*

%files python
%defattr(-,root,root)
%{py_sitedir}/*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.a
%{_includedir}/libyasm
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h


%changelog
* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 732051
- version update to 1.2.0 removed unneeded patchset

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 1.1.0-4
+ Revision: 672150
- add gentoo patches to build

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 1.1.0-3mdv2011.0
+ Revision: 591132
- Add BR for python-devel
- Remove py_requires -d macro
- Add missing BR ( python-cython)

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7
    - rebuild for python 2.7

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 1.1.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2mdv2010.1
+ Revision: 524477
- rebuilt for 2010.1

* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2010.0
+ Revision: 440815
- update to new version 0.8.0

* Sat Jun 06 2009 Giuseppe Ghibò <ghibo@mandriva.com> 0.7.2-3mdv2010.0
+ Revision: 383351
- Better python-pyrex BuildRequires.
- Added conditional lzma BuildRequires.

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2009.1
+ Revision: 319240
- rebuild for new python

* Fri Oct 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.2-1mdv2009.0
+ Revision: 291448
- update to new version 0.7.2

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-2mdv2009.0
+ Revision: 269852
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.1-1mdv2009.0
+ Revision: 209592
- update to new version 0.7.1

* Mon May 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.0-1mdv2009.0
+ Revision: 206302
- add requires on python-devel
- new version
- enable pythin bindings
- add missing buildrequires on xmlto and python-pyrex
- compile with fPIC on non-ix86 archs
- spec file clean

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 22 2007 trem <trem@mandriva.org> 0.6.2-1mdv2008.1
+ Revision: 92122
- update to 0.6.2
- update to 0.6.2

* Sun Aug 19 2007 Michael Scherer <misc@mandriva.org> 0.6.1-3mdv2008.0
+ Revision: 66497
- rebuild for missing lib

* Thu Aug 16 2007 Michael Scherer <misc@mandriva.org> 0.6.1-2mdv2008.0
+ Revision: 64650
- fix build errors due to manpages
- rebuild for 2008.0

* Sat Jun 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1mdv2008.0
+ Revision: 40287
- new version

