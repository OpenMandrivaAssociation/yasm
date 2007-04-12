Summary:	Modular Assembler
Name:		yasm
Version:	0.6.0
Release:	%mkrel 4
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.bz2
License:	BSD
Group:		Development/Other
Url:		http://www.tortall.net/projects/yasm/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD
License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%package -n %name-devel
Group:		Development/C
Summary:	Yasm modular assembler library
Obsoletes:	%mklibname -d yasm 0

%description -n %name-devel
Yasm is a complete rewrite of the NASM assembler under the "new" BSD
License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
	--disable-rpath

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
%{_mandir}/man7/yasm_dbgfmts.7.bz2
%{_mandir}/man7/yasm_objfmts.7.bz2
%{_mandir}/man7/yasm_parsers.7.bz2

%files -n %name-devel
%defattr(-,root,root)
%{_libdir}/lib*a
%{_includedir}/libyasm
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h


