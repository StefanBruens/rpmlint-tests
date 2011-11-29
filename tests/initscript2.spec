Name:		initscript2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
install -d -m 755 %buildroot/etc/init.d
cat <<EOF > %buildroot/etc/init.d/foo
#!/bin/bash
### BEGIN INIT INFO
# Provides:          foo
# Required-Start:    $remote_fs
# Required-Stop:     $remote_fs
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: blah
# Description:       blah blah
### END INIT INFO
# 
status
reload
EOF
install -d -m 755 %buildroot/sbin
ln -s /etc/init.d/foo %buildroot/sbin/rcfoo

%preun
%stop_on_removal foo

%postun
%restart_on_update foo
%insserv_cleanup

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%attr(0755,root,root) /etc/init.d/foo
/sbin/rcfoo

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
