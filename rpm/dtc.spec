Name:       dtc
Version:    1.4.6
Release:    1
Summary:    Device Tree Compiler
License:    GPLv2+
URL:        https://github.com/sailfishos/dtc

Source0:    %{name}-%{version}.tar.bz2

BuildRequires:     gcc
BuildRequires:     make
BuildRequires:     flex
BuildRequires:     bison
BuildRequires:     sed

%description
Devicetree is a data structure for describing hardware. Rather than hard coding
every detail of a device into an operating system, many aspects of the hardware
can be described in a data structure that is passed to the operating system at
boot time. The devicetree is used by OpenFirmware, OpenPOWER Abstraction Layer
(OPAL), Power Architecture Platform Requirements (PAPR) and in the standalone
Flattened Device Tree (FDT) form.

%prep
%autosetup -p1

%build
cd dtc
make %{?_smp_mflags} V=1 CC="gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS" dtc
# Drop libfdt bits from manual as we do not install it
sed -ri '
    /^III - libfdt$/, /^I - "dtc"/ { /^I - "dtc"/ ! d }
' Documentation/manual.txt

%install
install -d ${RPM_BUILD_ROOT}/%{_bindir}
install dtc/dtc dtc/dtdiff ${RPM_BUILD_ROOT}/%{_bindir}

%files
%license dtc/GPL
%doc dtc/Documentation/manual.txt
%{_bindir}/*
