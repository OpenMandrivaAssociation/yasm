Summary:	Modular Assembler
Name:		yasm
Version:	1.3.0
Release:	8
License:	BSD
Group:		Development/Other
Url:		http://www.tortall.net/projects/yasm/
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz

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

%prep
%autosetup -p1

%build
ln -s %{_bindir}/python2 python
export PATH=$(pwd):$PATH
%ifnarch ix86
export CFLAGS="%{optflags} -fPIC"
%endif

%configure \
	--disable-rpath \
	--disable-python \
	--disable-python-bindings

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/yasm/*.a

%files
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man1/yasm.1*
%{_mandir}/man7/yasm_arch.7*
%{_mandir}/man7/yasm_dbgfmts.7.*
%{_mandir}/man7/yasm_objfmts.7.*
%{_mandir}/man7/yasm_parsers.7.*

%files devel
%{_libdir}/lib*.a
%{_includedir}/libyasm
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h
