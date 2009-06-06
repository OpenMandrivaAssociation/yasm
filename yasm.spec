Summary:	Modular Assembler
Name:		yasm
Version:	0.7.2
Release:	%mkrel 3
License:	BSD
Group:		Development/Other
Url:		http://www.tortall.net/projects/yasm/
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.bz2
BuildRequires:	xmlto
BuildRequires:	python-pyrex > 0.9.5.1
%if %{mdkversion} <= 200710
BuildRequires:	lzma
%endif
%py_requires -d
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
%{_bindir}/%{name}
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
