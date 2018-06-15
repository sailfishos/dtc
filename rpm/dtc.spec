Name:       dtc
Summary:    Linux Kernel device tree compiler
Version:    0.0.0
Provides:   dtc
Release:    1
Group:      Development/Tools
URL:        https://git.kernel.org/pub/scm/utils/dtc/dtc.git
Source0:    %{name}-%{version}.tar.bz2
License:    GPLv2

BuildRequires: flex
BuildRequires: bison

%description
Linux Kernel device tree compiler

%prep
%setup -q

%build
cd dtc
# We only need the compiler, no python necessary so skip it.
make NO_PYTHON=1 HOME=$RPM_BUILD_ROOT/usr

%install
cd dtc
make NO_PYTHON=1 HOME=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root,-)
%{_bindir}/convert-dtsv0
%{_bindir}/dtc
%{_bindir}/dtdiff
%{_bindir}/fdtdump
%{_bindir}/fdtget
%{_bindir}/fdtoverlay
%{_bindir}/fdtput
%{_includedir}/fdt.h
%{_includedir}/libfdt.h
%{_includedir}/libfdt_env.h
%{_libdir}/libfdt-1.4.6.so
%{_libdir}/libfdt.a
%{_libdir}/libfdt.so
%{_libdir}/libfdt.so.1

