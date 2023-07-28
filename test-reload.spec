Name:           test-reload
Version:        0
Release:        %autorelease
Summary:        Test reload macros

License:        TBD
BuildArch:      noarch

%description
TBD

%prep
cat >test-reload.service <<EOF
[Service]
ExecStart=sleep infinity
ExecReload=true
EOF

%build

%install
install -Dt %buildroot/%_unitdir/ test-reload.service
install -Dt %buildroot/%_userunitdir/ test-reload.service

%post
%systemd_post test-reload.service
%systemd_user_post test-reload.service

%preun
%systemd_preun test-reload.service
%systemd_user_preun test-reload.service

%postun
%systemd_postun_with_reload test-reload.service
%systemd_user_postun_with_reload test-reload.service

%files
%_unitdir/test-reload.service
%_userunitdir/test-reload.service

%changelog
%autochangelog
