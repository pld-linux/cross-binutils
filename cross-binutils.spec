# TODO
# - warning: Installed (but unpackaged) file(s) found:
#        /usr/sh64-linux/sh64-elf
#
# Conditional build:
# Targets:
%bcond_without	alpha			# enable alpha
%bcond_without	arm			# enable arm
%bcond_without	aarch64			# enable aarch64
%bcond_without	avr32			# enable avr32
%bcond_without	blackfin		# enable blackfin
%bcond_without	c6x			# enable c6x
%bcond_without	cris			# enable cris
%bcond_without	frv			# enable frv
%bcond_without	h8300			# enable h8300
%bcond_without	hppa			# enable hppa
%bcond_without	hppa64			# enable hppa64
%bcond_without	ia64			# enable ia64
%bcond_without	m32r			# enable m32r
%bcond_without	m68k			# enable m68k
%bcond_without	metag			# enable metag
%bcond_without	microblaze		# enable microblaze
%bcond_without	mips64			# enable mips64
%bcond_without	mn10300			# enable mn10300
%bcond_without	nios2			# enable nios2
%bcond_without	openrisc		# enable openrisc
%bcond_without	powerpc64		# enable powerpc64
%bcond_without	s390x			# enable s390x
%bcond_without	score			# enable score
%bcond_without	sh			# enable sh
%bcond_without	sh64			# enable sh64
%bcond_without	sparc64			# enable sparc64
%bcond_without	tile			# enable tile
%bcond_without	x86_64			# enable x86_64
%bcond_without	xtensa			# enable xtensa

# 32-bit packages we don't build as we can use the 64-bit package instead
%undefine with_i386
%undefine with_mips
%undefine with_powerpc
%undefine with_s390
%undefine with_sparc
%undefine with_sh4

# not available in binutils-2.24
%undefine with_hexagon
%undefine with_unicore32

Summary:	A GNU collection of cross-compilation binary utilities
Name:		cross-binutils
Version:	2.25
Release:	0.10
License:	GPL v3+
Group:		Development/Tools
# Note - the Linux Kernel binutils releases are too unstable and contain too
# many controversial patches so we stick with the official FSF version
# instead.
Source0:	http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	d9f3303f802a5b6b0bb73a335ab89d66
Source2:	binutils-2.19.50.0.1-output-format.sed
# Bring up to date with what's in the git release branch
#Patch00: binutils-2.24-cde98f8566e14f52b896abc92c357cdd14717505.patch
Patch01:	binutils-2.20.51.0.2-libtool-lib64.patch
Patch02:	binutils-2.20.51.0.10-ppc64-pie.patch
Patch03:	binutils-2.20.51.0.2-ia64-lib64.patch
Patch04:	binutils-2.25-version.patch
Patch05:	binutils-2.25-set-long-long.patch
Patch06:	binutils-2.20.51.0.10-copy-osabi.patch
Patch07:	binutils-2.20.51.0.10-sec-merge-emit.patch
# Enable -zrelro by default: BZ #621983
Patch08:	binutils-2.22.52.0.1-relro-on-by-default.patch
# Local patch - export demangle.h with the binutils-devel rpm.
Patch09:	binutils-2.22.52.0.1-export-demangle.h.patch
# Disable checks that config.h has been included before system headers.  BZ #845084
Patch10:	binutils-2.22.52.0.4-no-config-h-check.patch
# Fix addr2line to use the dynamic symbol table if it could not find any ordinary symbols.
Patch11:	binutils-2.23.52.0.1-addr2line-dynsymtab.patch
Patch12:	binutils-2.25-kernel-ld-r.patch
# Correct bug introduced by patch 12
Patch13:	binutils-2.23.2-aarch64-em.patch
# Fix detections little endian PPC shared libraries
Patch14:	binutils-2.24-ldforcele.patch
URL:		http://sources.redhat.com/binutils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	texinfo >= 4.0
BuildRequires:	zlib-devel
# BZ 920545: We need pod2man in order to build the manual pages.
BuildRequires:	/usr/bin/pod2man
# Required for: ld-bootstrap/bootstrap.exp bootstrap with --static
# It should not be required for: ld-elf/elf.exp static {preinit,init,fini} array
Conflicts:	gcc-c++ < 4.0.0
%ifarch ia64
Obsoletes:	gnupro <= 1117-1
%endif
Provides:	bundled(libiberty)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Where the binaries aimed at gcc will live (ie. /usr/<target>/bin/)
%define auxbin_prefix %{_exec_prefix}
%define srcdir binutils-%{version}

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%package common
Summary:	Cross-build binary utility documentation and translation files
Group:		Development/Tools
BuildArch:	noarch

%description common
Documentation, manual pages and translation files for cross-build
binary image generation, manipulation and query tools.

%define do_package() \
%package -n binutils-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Tools \
Requires:	%{name}-common = %{version}-%{release}\
\
%description -n binutils-%1 \
Cross-build binary image generation, manipulation and query tools. \

%define do_symlink() \
%package -n binutils-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Tools \
Requires:	binutils-%2 = %{version}-%{release}\
\
%description -n binutils-%1 \
Cross-build binary image generation, manipulation and query tools. \

%do_package alpha-linux-gnu
%do_package arm-linux-gnu
%do_package aarch64-linux-gnu
%do_package avr32-linux-gnu
%do_package bfin-linux-gnu
%do_package c6x-linux-gnu
%do_package cris-linux-gnu
%do_package frv-linux-gnu
%do_package h8300-linux-gnu
%do_package hexagon-linux-gnu
%do_package hppa-linux-gnu
%do_package hppa64-linux-gnu
%do_package i386-linux-gnu
%do_package ia64-linux-gnu
%do_package m32r-linux-gnu
%do_package m68k-linux-gnu
%do_package metag-linux-gnu
%do_package microblaze-linux-gnu
%do_package mips-linux-gnu
%do_package mips64-linux-gnu
%do_package mn10300-linux-gnu
%do_package nios2-linux-gnu
%do_package openrisc-linux-gnu
%do_package powerpc-linux-gnu
%do_package powerpc64-linux-gnu
%do_symlink ppc-linux-gnu	powerpc-linux-gnu
%do_symlink ppc64-linux-gnu	powerpc64-linux-gnu
%do_package s390-linux-gnu
%do_package s390x-linux-gnu
%do_package score-linux-gnu
%do_package sh-linux-gnu
%do_package sh4-linux-gnu
%do_package sh64-linux-gnu
%do_package sparc-linux-gnu
%do_package sparc64-linux-gnu
%do_package tile-linux-gnu
%do_package unicore32-linux-gnu
%do_package x86_64-linux-gnu
%do_package xtensa-linux-gnu

%prep
%setup -qc
cd %{srcdir}
%if 1
#%%patch00 -p1 -b .latest-git~
%patch -P01 -p1
%patch -P02 -p1
%ifarch ia64
%if "%{_lib}" == "lib64"
%patch -P03 -p1
%endif
%endif
%patch -P04 -p1
%patch -P05 -p1
%patch -P06 -p1
%patch -P07 -p1
%patch -P08 -p1
%patch -P09 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%endif

# We cannot run autotools as there is an exact requirement of autoconf-2.59.

# On ppc64 we might use 64KiB pages
sed -i -e '/#define.*ELF_COMMONPAGESIZE/s/0x1000$/0x10000/' bfd/elf*ppc.c
# LTP sucks
# exclude "gas/config", "libiberty/config", it's a dir
%{__sed} -i -e 's/i\[3-7\]86/i[34567]86/g' $(echo */conf* | sed -e 's#gas/config##;s#libiberty/config##;')
sed -i -e 's/%''{release}/%{release}/g' bfd/Makefile{.am,.in}
sed -i -e '/^libopcodes_la_\(DEPENDENCIES\|LIBADD\)/s,$, ../bfd/libbfd.la,' opcodes/Makefile.{am,in}
# Build libbfd.so and libopcodes.so with -Bsymbolic-functions if possible.
if %{__cc} %{rpmcflags} -v --help 2>&1 | grep -q -- -Bsymbolic-functions; then
	sed -i -e 's/^libbfd_la_LDFLAGS = /&-Wl,-Bsymbolic-functions /' bfd/Makefile.{am,in}
	sed -i -e 's/^libopcodes_la_LDFLAGS = /&-Wl,-Bsymbolic-functions /' opcodes/Makefile.{am,in}
fi

# $PACKAGE is used for the gettext catalog name.
sed -i -e 's/^ PACKAGE=/ PACKAGE=cross-/' */configure
# Undo the name change to run the testsuite.
for tool in binutils gas ld; do
	sed -i -e "2aDEJATOOL = $tool" $tool/Makefile.am
	sed -i -e "s/^DEJATOOL = .*/DEJATOOL = $tool/" $tool/Makefile.in
done
touch */configure
cd ..

cat > target.list <<EOF
%{?with_alpha:alpha-linux-gnu}
%{?with_arm:arm-linux-gnu}
%{?with_aarch64:aarch64-linux-gnu}
%{?with_avr32:avr32-linux-gnu}
%{?with_blackfin:bfin-linux-gnu}
%{?with_c6x:c6x-linux-gnu}
%{?with_cris:cris-linux-gnu}
%{?with_frv:frv-linux-gnu}
%{?with_h8300:h8300-linux-gnu}
%{?with_hexagon:hexagon-linux-gnu}
%{?with_hppa:hppa-linux-gnu}
%{?with_hppa64:hppa64-linux-gnu}
%{?with_i386:i386-linux-gnu}
%{?with_ia64:ia64-linux-gnu}
%{?with_m32r:m32r-linux-gnu}
%{?with_m68k:m68k-linux-gnu}
%{?with_metag:metag-linux-gnu}
%{?with_microblaze:microblaze-linux-gnu}
%{?with_mips:mips-linux-gnu}
%{?with_mips64:mips64-linux-gnu}
%{?with_mn10300:mn10300-linux-gnu}
%{?with_nios2:nios2-linux-gnu}
%{?with_openrisc:openrisc-linux-gnu}
%{?with_powerpc:powerpc-linux-gnu}
%{?with_powerpc64:powerpc64-linux-gnu}
%{?with_s390:s390-linux-gnu}
%{?with_s390x:s390x-linux-gnu}
%{?with_score:score-linux-gnu}
%{?with_sh:sh-linux-gnu}
%{?with_sh4:sh4-linux-gnu}
%{?with_sh64:sh64-linux-gnu}
%{?with_sparc:sparc-linux-gnu}
%{?with_sparc64:sparc64-linux-gnu}
%{?with_tile:tile-linux-gnu}
%{?with_unicore32:unicore32-linux-gnu}
%{?with_x86_64:x86_64-linux-gnu}
%{?with_xtensa:xtensa-linux-gnu}
EOF

if [ $(wc -w < target.list) = 0 ]; then
	echo >&2 "No targets selected"
	exit 8
fi

%build
config_target() {
	local arch=$1
	local prefix=$arch-
	local build_dir=${1%%%%-*}

	case $arch in
	arm-*)		target=arm-linux-gnueabi;;
	aarch64-*)	target=aarch64-linux-gnu;;
	avr32-*)	target=avr-linux;;
	bfin-*)		target=bfin-uclinux;;
	c6x-*)		target=c6x-uclinux;;
	h8300-*)	target=h8300-elf;;
	m32r-*)		target=m32r-elf;;
	mn10300-*)	target=am33_2.0-linux;;
	m68knommu-*)	target=m68k-linux;;
	openrisc-*)	target=or1k-linux-gnu;;
	parisc-*)	target=hppa-linux;;
	score-*)	target=score-elf;;
	sh64-*)		target=sh64-linux;;
	tile-*)		target=tilegx-linux;;
	v850-*)		target=v850e-linux;;
	x86-*)		target=x86_64-linux;;
	*)		target=$arch;;
	esac

	echo $arch: target is $target
	CARGS=

	case $target in i?86*|sparc*|ppc*|s390*|sh*|arm*)
		CARGS="$CARGS --enable-64-bit-bfd"
		;;
	esac

	case $target in ia64*)
		CARGS="$CARGS --enable-targets=i386-linux"
		;;
	esac

	case $target in ppc*|ppc64*)
		CARGS="$CARGS --enable-targets=spu"
		;;
	esac

	case $target in sh-*)
		CARGS="$CARGS --enable-targets=sh4-linux"
		;;
	esac

	case $target in sh64*)
		CARGS="$CARGS --enable-targets=sh64-linux,sh-elf,sh-linux,sh4-linux"
		;;
	esac

	mkdir $build_dir
	cd $build_dir

	# We could optimize the cross builds size by --enable-shared but the produced
	# binaries may be less convenient in the embedded environment.
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -Wl,-z,relro" \
	../%{srcdir}/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--enable-checking \
	--prefix=%{_prefix} \
	--exec-prefix=%{auxbin_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=$target \
	--program-prefix=$prefix \
	--disable-shared \
	--disable-install_libbfd \
	--with-sysroot=%{_prefix}/$arch/sys-root \
	$CARGS \
	--with-bugurl="http://bugs.pld-linux.org"
	cd ..
}

for target in $(cat target.list); do
	config_target $target
done

build_target() {
	local build_dir=${1%%%%-*}
	%{__make} -C $build_dir tooldir=%{_prefix} all
}

for target in $(cat target.list); do
	build_target $target
done

# for documentation purposes only
install -d cross-binutils
cd cross-binutils
../%{srcdir}/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--prefix=%{_prefix} \
	--exec-prefix=%{auxbin_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--program-prefix=cross- \
	--disable-shared \
	--with-bugurl="http://bugs.pld-linux.org"

%{__make} tooldir=%{_prefix} all
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install_bin() {
	local cpu=${1%%%%-*}
	local build_dir=$cpu
	%{__make} install -C $build_dir DESTDIR=$RPM_BUILD_ROOT

	# We want links for ppc and ppc64 also if we make powerpc or powerpc64
	case $cpu in
	powerpc*)
		cd $RPM_BUILD_ROOT%{_bindir}
			for i in $cpu-*; do
				ln -s $i ppc${i#powerpc}
			done
		cd -
		cd $RPM_BUILD_ROOT%{_prefix}
		for i in $cpu-*; do
			ln -s $i ppc${i#powerpc}
		done
		cd -
		cd $RPM_BUILD_ROOT%{_mandir}/man1
		for i in $cpu-*; do
			ln -s $i ppc${i#powerpc}
		done
		cd -
		;;
	esac
}

for target in $(cat target.list); do
	echo "=== INSTALL target $target ==="
	install -d $RPM_BUILD_ROOT%{_prefix}/$target/sys-root
	install_bin $target

	if [ $target = sh64-linux-gnu ]; then
		ln -s %{auxbin_prefix}/sh64-elf $RPM_BUILD_ROOT%{auxbin_prefix}/sh64-linux
	fi
done

echo "=== INSTALL man targets ==="
%{__make} install-man1 -C cross-binutils/binutils/doc DESTDIR=$RPM_BUILD_ROOT
%{__make} install-man1 -C cross-binutils/gas/doc DESTDIR=$RPM_BUILD_ROOT
%{__make} install-man1 -C cross-binutils/ld DESTDIR=$RPM_BUILD_ROOT
%{__make} install-man1 -C cross-binutils/gprof DESTDIR=$RPM_BUILD_ROOT

echo "=== INSTALL po targets ==="
%{__make} install -C cross-binutils/binutils/po DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C cross-binutils/gas/po DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C cross-binutils/ld/po DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C cross-binutils/gprof/po DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C cross-binutils/bfd/po DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C cross-binutils/opcodes/po DESTDIR=$RPM_BUILD_ROOT

# Add the additional symlink-only targets
grep ^powerpc target.list | sed -e s/powerpc/ppc/ > symlink-target.list

# For cross-binutils we drop the documentation.
echo "=== REMOVE documentation ==="
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

echo "=== REMOVE libraries and scripts ==="
rm -rf $RPM_BUILD_ROOT%{_libdir}/libiberty.a
rm -rf $RPM_BUILD_ROOT%{auxbin_prefix}/*/lib/ldscripts
rmdir $RPM_BUILD_ROOT%{auxbin_prefix}/*/lib || :

echo "=== BUILD file lists ==="
build_file_list() {
	local arch=$1
	local cpu=${arch%%%%-*}

	case $cpu in
	avr32)		target_cpu=avr;;
	bfin)		target_cpu=bfin;;
	h8300)		target_cpu=h8300;;
	mn10300)	target_cpu=am33_2.0;;
	openrisc)	target_cpu=or1k;;
	score)		target_cpu=score;;
	tile)		target_cpu=tilegx;;
	v850)		target_cpu=v850e;;
	*)		target_cpu=$cpu;;
	esac

	(
	echo "%%defattr(-,root,root,-)"
	echo "%{_bindir}/$arch-[!l]*"
	echo "%{_bindir}/$arch-ld*"
	if [ -L $RPM_BUILD_ROOT%{auxbin_prefix}/$target_cpu-* ]; then
		echo "%{auxbin_prefix}/$target_cpu-*"
	else
		echo "%dir %{auxbin_prefix}/$target_cpu-*"
		echo "%dir %{auxbin_prefix}/$target_cpu-*/bin"
		echo "%{auxbin_prefix}/$target_cpu-*/bin/*"
		if [ "$target_cpu" != "$cpu" ]; then
			echo "%dir %{_prefix}/$arch"
		fi
		echo "%{_prefix}/$arch/sys-root"
	fi
	echo "%{_mandir}/man1/$arch-*"
	) > files.$arch
}

for target in $(cat target.list symlink-target.list); do
	build_file_list $target
done

# All the installed manual pages and translation files for each program are the
# same, so symlink them to the core package
echo "=== CROSSLINK man pages ==="
cd $RPM_BUILD_ROOT%{_mandir}/man1
	for i in cross-*.1*; do
		j=${i#cross-}

		for k in *-$j; do
			if [ $k != $i ]; then
				ln -sf $i $k
			fi
		done
	done

	# Add ld.bfd manual pages
	find * -name "*ld.1*" -a ! -name "cross-ld.1*" -print |
	while read x; do
		y=$(echo $x | sed -e s/ld[.]1/ld.bfd.1/)
		ln -s $x $y
	done
cd -

# Find the language files which only exist in the common package
%find_lang cross-binutils
%find_lang cross-opcodes
%find_lang cross-bfd
%find_lang cross-gas
%find_lang cross-ld
%find_lang cross-gprof
cat \
cross-binutils.lang \
cross-opcodes.lang \
cross-bfd.lang \
cross-gas.lang \
cross-ld.lang \
cross-gprof.lang \
 > files.cross

%clean
rm -rf $RPM_BUILD_ROOT

%files common -f files.cross
%defattr(644,root,root,755)
%doc %{srcdir}/README
%doc %{srcdir}/COPYING*
%{_mandir}/man1/cross-*

%define do_files() \
%files -n binutils-%1 -f files.%1 \
%defattr(644,root,root,755) \

%{?with_alpha:%do_files alpha-linux-gnu}
%{?with_arm:%do_files arm-linux-gnu}
%{?with_aarch64:%do_files aarch64-linux-gnu}
%{?with_avr32:%do_files avr32-linux-gnu}
%{?with_blackfin:%do_files bfin-linux-gnu}
%{?with_c6x:%do_files c6x-linux-gnu}
%{?with_cris:%do_files cris-linux-gnu}
%{?with_frv:%do_files frv-linux-gnu}
%{?with_h8300:%do_files h8300-linux-gnu}
%{?with_hexagon:%do_files hexagon-linux-gnu}
%{?with_hppa:%do_files hppa-linux-gnu}
%{?with_hppa64:%do_files hppa64-linux-gnu}
%{?with_i386:%do_files i386-linux-gnu}
%{?with_ia64:%do_files ia64-linux-gnu}
%{?with_m32r:%do_files m32r-linux-gnu}
%{?with_m68k:%do_files m68k-linux-gnu}
%{?with_metag:%do_files metag-linux-gnu}
%{?with_microblaze:%do_files microblaze-linux-gnu}
%{?with_mips:%do_files mips-linux-gnu}
%{?with_mips64:%do_files mips64-linux-gnu}
%{?with_mn10300:%do_files mn10300-linux-gnu}
%{?with_nios2:%do_files nios2-linux-gnu}
%{?with_openrisc:%do_files openrisc-linux-gnu}
%{?with_powerpc:%do_files powerpc-linux-gnu}
%{?with_powerpc64:%do_files powerpc64-linux-gnu}
%{?with_powerpc:%do_files ppc-linux-gnu}
%{?with_powerpc64:%do_files ppc64-linux-gnu}
%{?with_s390:%do_files s390-linux-gnu}
%{?with_s390x:%do_files s390x-linux-gnu}
%{?with_score:%do_files score-linux-gnu}
%{?with_sh:%do_files sh-linux-gnu}
%{?with_sh4:%do_files sh4-linux-gnu}
%{?with_sh64:%do_files sh64-linux-gnu}
%{?with_sparc:%do_files sparc-linux-gnu}
%{?with_sparc64:%do_files sparc64-linux-gnu}
%{?with_tile:%do_files tile-linux-gnu}
%{?with_unicore32:%do_files unicore32-linux-gnu}
%{?with_x86_64:%do_files x86_64-linux-gnu}
%{?with_xtensa:%do_files xtensa-linux-gnu}
