Summary:	Firmware drivers for EZUSB MIDI devices
Name:		ezusbmidi
Version:	2002_10_20
Release:	12
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://linux-hotplug.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ezusbmidi-2002_10_20-sdcc33.patch
Patch1:		ezusbmidi-2002_10_20-udev.patch
BuildRequires:	linuxdoc-tools
BuildRequires:	sdcc
Requires:	fxload
Requires:	udev
BuildArch:	noarch

%description
This program is an USB-MIDI compliant firmware for the EZUSB chip
(AN2131SC) developed to make an USB-MIDI adapter to run with Linux.
It runs with these USB-MIDI devices:
- Midiman Midisport 1x1
- Midiman Midisport 2x2
- Midiman Midisport UNO
- Steinberg USB-2-MIDI

%files
%doc AUTHORS COPYING ChangeLog descriptor.png KnownBugs README *.html
%{_sysconfdir}/udev/rules.d/*
%{_datadir}/usb/ezusbmidi

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make

%install
%makeinstall_std


