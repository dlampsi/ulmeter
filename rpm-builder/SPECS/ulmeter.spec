Name:           ulmeter
Version:        1.0
Release:        1
Summary:        Collect host load statistic per user
Group:          User Interface/Desktops
License:        GPL
URL:            https://github.com/dlampsi/user-load-meter
Source0:        ulmeter.service
Source1:        ulmeter.timer
Source2:        ulmeter-stat.service
Source3:        ulmeter-stat.timer
Source4:        ulmeter
Source5:        ulmeter-stat

%description
Utilite for get host load statistic per user. Run through systemd.

%prep

%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/systemd/system
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/systemd/system
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/systemd/system
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/systemd/system
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/systemd/system
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/bin
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/usr/local/bin
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/usr/local/bin

%files
%defattr(-,root,root)
/etc/systemd/system/*
/usr/local/bin/*

%post
chmod +x /usr/local/bin/ulmeter*
systemctl enable ulmeter.service
systemctl enable ulmeter.timer
systemctl enable ulmeter-stat.service
systemctl enable ulmeter-stat.timer
systemctl start ulmeter-stat.timer
systemctl start ulmeter.timer

%changelog
* Sun Mar 4 2018 Dmitriy Lampsi 0.1.1
  - Initial rpm release
* Mon Mar 5 2018 Dmitriy Lampsi 1.0.1
  - Get ready for docker
