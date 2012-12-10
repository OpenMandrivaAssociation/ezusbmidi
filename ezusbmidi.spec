%define name 	ezusbmidi
%define version 2002_10_20
%define release %mkrel 10

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2002_10_20-10mdv2011.0
+ Revision: 618252
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2002_10_20-9mdv2010.0
+ Revision: 428661
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2002_10_20-8mdv2009.0
+ Revision: 245017
- rebuild

* Sun Mar 09 2008 Adam Williamson <awilliamson@mandriva.org> 2002_10_20-6mdv2008.1
+ Revision: 182735
- bunzip2 patch
- new license policy
- udev rules are not config files
- adjust udev rules to look for fxload in /sbin not /usr/sbin

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2002_10_20-5mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ezusbmidi


* Tue Mar 21 2006 Austin Acton <austin@mandriva.org> 2002_10_20-5mdk
- mkrel

* Sat Mar 18 2006 Pedro Lopez-Cabanillas <plcl@users.sourceforge.net> 2002_10_20-4mdk
- use udev instead of hotplug, for Mandriva 2006

* Sun Dec 28 2003 Austin Acton <austin@linux.ca> 2002_10_20-3mdk
- rebuild with fixed sdcc

* Sat Dec 27 2003 Austin Acton <austin@linux.ca> 2002_10_20-2mdk
- sweet help from Pedro Lopez-Cabanillas <plcl@bigfoot.com> :
  - fxload is at /usr/sbin

* Wed Apr 30 2003 Austin Acton <aacton@yorku.ca> 2002_10_20-1mdk
- port to Mandrake
- patch for sdcc 2.3.3

* Sun Oct 20 2002 Pedro Lopez-Cabanillas <plcl@bigfoot.com> 2002_10_20
- first snapshot.
