%define name 	ezusbmidi
%define version 2002_10_20
%define release %mkrel 6

Summary: 	Firmware drivers for EZUSB MIDI devices
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-udev.patch
License: 	GPLv2
URL: 		http://linux-hotplug.sourceforge.net
Group: 		System/Kernel and hardware
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch: 	noarch
Requires: 	fxload udev
BuildRequires: 	linuxdoc-tools sdcc

%description
This program is an USB-MIDI compliant firmware for the EZUSB chip
(AN2131SC) developed to make an USB-MIDI adapter to run with Linux.
It runs with these USB-MIDI devices:
- Midiman Midisport 1x1
- Midiman Midisport 2x2
- Midiman Midisport UNO
- Steinberg USB-2-MIDI
Author: Lars Doelle <lars.doelle@on-line.de>

%prep
%setup
%patch0 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog descriptor.png KnownBugs README *.html
%{_sysconfdir}/udev/rules.d/*
%{_datadir}/usb/ezusbmidi

