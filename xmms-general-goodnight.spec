Summary:	An XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given time
Summary(pl):	Wtyczka wy³±czaj±ca XMMS o okre¶lonej porze
Name:		xmms-general-goodnight
Version:	0.3.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://fiktiv.szgtikol.kando.hu/~folti/src/xmms-goodnight-%{version}.tar.gz
# Source0-md5:	4a26d272917f034ef18525fa33af9885
URL:		http://fiktiv.szgtikol.kando.hu/~folti/src/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An XMMS plugin to stop playing/quit XMMS/suspend/shutdown at a given
time.

%description -l pl
Wtyczka wy³±czaj±ca XMMS o okre¶lonej porze.

%prep
%setup -q -n xmms-goodnight-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_general_plugindir}

install libgoodnight.so $RPM_BUILD_ROOT%{xmms_general_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{xmms_general_plugindir}/*
