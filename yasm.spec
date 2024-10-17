%define _disable_rebuild_configure 1

Summary:	Modular Assembler
Name:		yasm
Version:	1.3.0
Release:	11
License:	BSD
Group:		Development/Other
Url:		https://www.tortall.net/projects/yasm/
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
Obsoletes:	%{mklibname -d yasm 0} < 1.3.0-8
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
%ifarch znver1
# Workaround for infinite hang while building virtualbox 7.0.6
# with yasm built with znver1 flags
export CFLAGS="-O2 -g3 -gdwarf-4 -march=znver1 -fPIC"
%endif

%configure \
	--disable-rpath \
	--disable-python \
	--disable-python-bindings

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/yasm/*.a

# (tpg) strip LTO from "LLVM IR bitcode" files
check_convert_bitcode() {
    printf '%s\n' "Checking for LLVM IR bitcode"
    llvm_file_name=$(realpath ${1})
    llvm_file_type=$(file ${llvm_file_name})

    if printf '%s\n' "${llvm_file_type}" | grep -q "LLVM IR bitcode"; then
# recompile without LTO
	clang %{optflags} -fno-lto -Wno-unused-command-line-argument -x ir ${llvm_file_name} -c -o ${llvm_file_name}
    elif printf '%s\n' "${llvm_file_type}" | grep -q "current ar archive"; then
	printf '%s\n' "Unpacking ar archive ${llvm_file_name} to check for LLVM bitcode components."
# create archive stage for objects
	archive_stage=$(mktemp -d)
	archive=${llvm_file_name}
	cd ${archive_stage}
	ar x ${archive}
	for archived_file in $(find -not -type d); do
	    check_convert_bitcode ${archived_file}
	    printf '%s\n' "Repacking ${archived_file} into ${archive}."
	    ar r ${archive} ${archived_file}
	done
	ranlib ${archive}
	cd ..
    fi
}

for i in $(find %{buildroot} -type f -name "*.[ao]"); do
    check_convert_bitcode ${i}
done

%files
%doc AUTHORS
%{_bindir}/*
%doc %{_mandir}/man1/yasm.1*
%doc %{_mandir}/man7/yasm_arch.7*
%doc %{_mandir}/man7/yasm_dbgfmts.7.*
%doc %{_mandir}/man7/yasm_objfmts.7.*
%doc %{_mandir}/man7/yasm_parsers.7.*

%files devel
%{_libdir}/lib*.a
%{_includedir}/libyasm
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h
