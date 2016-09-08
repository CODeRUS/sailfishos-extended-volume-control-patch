Name:       sailfishos-extended-volume-control-patch

BuildArch: noarch

Summary:    Extended volume control patch
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager

%description
Extended volume control patch allow you to change ringer and media volume
 separately by moving your finger


%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-extended-volume-control-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-extended-volume-control-patch

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-extended-volume-control-patch ]; then
/usr/sbin/patchmanager -u sailfishos-extended-volume-control-patch || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-extended-volume-control-patch ]; then
/usr/sbin/patchmanager -u sailfishos-extended-volume-control-patch || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-extended-volume-control-patch
