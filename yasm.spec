%define _disable_rebuild_configure 1

Summary:	Modular Assembler
Name:		yasm
Version:	1.3.0
Release:	12
License:	BSD
Group:		Development/Other
Url:		https://www.tortall.net/projects/yasm/
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz

%patchlist
# From upstream git https://github.com/yasm/yasm
# The last release is 5 years old, but the last commit only 1 year...
0001-Add-vseg-section-option.patch
0002-New-wrt-optimization-and-improved-seg-optimization.patch
0003-Overrides-and-dummy-value-finalization-for-bin.patch
0004-squashme.patch
0005-Add-segments-to-label-addresses.patch
0006-Generate-segmented-addresses-for-labels.patch
0007-Interpret-vstart-as-linear-address.patch
0008-Better-optimization-of-expr-with-segoffs.patch
0009-Add-missing-objfmt_x64-to-CMakeLists.txt.patch
0010-COFF-PE-Always-set-paddr-and-vaddr-to-0.patch
0011-Make-cmake-module-search-case-insensitive.patch
0012-Fix-a-few-more-cases-of-case-sensitivity-in-module-h.patch
0013-Rename-E-option-to-Z.patch
0014-Allow-longopt-as-well-as-longopt.patch
0015-Fix-yasm-segfaults-GNU-assembler-files-on-OS-X.patch
0016-Avoid-shadowing-warning-when-building-with-VS2015.patch
0017-Add-build-files-for-Visual-Studio-2015.patch
0018-add-Visual-Studio-build-files-missed-in-thye-initial.patch
0019-Support-numbers-prefixed-with-or-in-ifnum.patch
0020-fixing-an-argument-parsing-bug-in-ytasm.patch
0021-update-MSVC14-build.patch
0022-Added-Wno-segreg-in-64bit.patch
0023-add-missing-VC-header.patch
0024-add-Visual-Studio-2017-build-files.patch
0025-New-AMD-Excavator-MONITORX-MWAITX-instruction-suppor.patch
0026-Leak-fixes-79.patch
0027-Only-print-warnings-treated-as-errors-if-there-were-.patch
0028-fix-memory-errors-when-using-gas-processor-with-coff.patch
0029-allow-movbe-to-be-suffixed-with-wlq-in-gas-syntax.patch
0030-avoid-return-value-of-ftruncate-ignored-warnings-76.patch
0031-Update-the-files-for-integrating-YASM-into-Visual-St.patch
0032-change-vsyasm.props-to-use-the-YASM_PATH-environment.patch
0033-correct-bug-in-VSYASM-build-integration-files-vsyasm.patch
0034-correct-bug-in-VSYASM-build-integration-files-vsyasm.patch
0035-add-build-files-for-Microsoft-Visual-Studio-2019.patch
0036-Allow-user-to-set-the-YASM-path-with-or-without-an-e.patch
0037-Fix-info.stab-info.stabstr-typo-in-stabs-dbgfmt.c-96.patch
0038-Revert-optimizations-added-in-68-146.patch
0039-Fix-EOL-handling-in-genmacro.c-123.patch
0040-add-missing-include-file.patch
0041-minor-update-to-VS2019-build.patch
0042-Fix-test-failures-177.patch
0043-Do-not-use-AC_HEADER_STDC-178.patch
0044-Add-GitHub-CI-build-workflow-179.patch
0045-Update-Mach-O-for-newer-macOS-180.patch
0046-Update-Visual-Studio-build-to-Visual-STudio-2022.patch
0047-Add-vcpkg-installation-instructions-200.patch
0048-Introduce-a-security-policy-and-add-text-to-the-READ.patch
0049-Fix-detecting-Windows-platform-204.patch
0050-Remove-__DATE__-from-version-strings-198.patch
0051-Add-EM-for-loongarch-192.patch
0052-Fix-memleak-of-codeview-leaf-114.patch
0053-gas-preproc-Fix-UB-crashes-186.patch
0054-Fix-badly-freed-pointer-on-indented-code-block-after.patch
0055-Fix-test-failure-introduced-in-51af4082cc898b122b88f.patch
0056-Update-elf-objfmt.c-148.patch
0057-Fix-128-bit-variant-of-VPBLENDVB-incorrectly-marked-.patch
0058-Added-missing-config-vars-to-config.h.cmake.-160.patch
0059-Allow-sha256rnds2-to-have-memory-as-2nd-operand-108.patch
0060-Enable-AES-on-westmere-97.patch
0061-Python-2-to-3-migration-m4-folder-144.patch
0062-Fix-allocator-mismatch-107.patch
0063-libyasm-section.c-support-gas-.private_extern-direct.patch
0064-More-makedep-features-80.patch
0065-GAS-preprocessor-don-t-cut-comments-inside-of-string.patch
0066-Fix-missing-yasm_xfree-function-declaration-224.patch
0067-CI-update-GitHub-Actions-version-225.patch
0068-Fix-function-declaration-warnings-with-clang-226.patch
0069-Fix-memory-leak-in-bin-objfmt-231.patch
0070-Add-support-for-NASM-warning-preprocessor-directive-.patch
0071-elf.c-Fix-NULL-deref-on-bad-xsize-expression-234.patch
0072-Fix-access-field-adress-on-null-pointer-in-x86bc.c-2.patch
0073-Fix-memory-leak-if-masm-mode-enabled-in-parsers-239.patch
0074-Fix-nullptr-deref-in-yasm_expr__copy_except-241.patch
0075-Fix-misleading-indentation-132.patch
0076-Fix-use-after-free-in-yasm_intnum_destroy-242.patch
0077-Fix-handle_dot_label-heap-out-of-bound-243.patch
0078-Fix-null-pointer-dereference-in-yasm_expr_get_intnum.patch
0079-Fix-null-pointer-dereference-in-yasm_section_bcs_app.patch
# Not quite as dead as it appears to be...
https://github.com/yasm/yasm/pull/287.patch

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
