# http://github.com/gogo/protobuf
%global goipath         github.com/gogo/protobuf
Version:                1.1.1

%gometa

Name:           golang-googlecode-gogoprotobuf
Release:        1%{?dist}
Summary:        A fork of goprotobuf with several extra features
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: protobuf-compiler

%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%build
%gobuildroot
%gobuild -o _bin/gogoreplace %{goipath}/gogoreplace
%gobuild -o _bin/protoc-gen-combo %{goipath}/protoc-gen-combo
%gobuild -o _bin/protoc-gen-gofast %{goipath}/protoc-gen-gofast
%gobuild -o _bin/protoc-gen-gogo %{goipath}/protoc-gen-gogo
%gobuild -o _bin/protoc-gen-gogofast %{goipath}/protoc-gen-gogofast
%gobuild -o _bin/protoc-gen-gogofaster %{goipath}/protoc-gen-gogofaster
%gobuild -o _bin/protoc-gen-gogoslick %{goipath}/protoc-gen-gogoslick
%gobuild -o _bin/protoc-gen-gogotypes %{goipath}/protoc-gen-gogotypes
%gobuild -o _bin/protoc-gen-gostring %{goipath}/protoc-gen-gostring
%gobuild -o _bin/protoc-min-version %{goipath}/protoc-min-version


%install
#### binary ####
install -d %{buildroot}%{_bindir}
install -m 755 _bin/gogoreplace %{buildroot}/%{_bindir}/gogoreplace
install -m 755 _bin/protoc-gen-combo %{buildroot}/%{_bindir}/protoc-gen-combo
install -m 755 _bin/protoc-gen-gofast %{buildroot}/%{_bindir}/protoc-gen-gofast
install -m 755 _bin/protoc-gen-gogo %{buildroot}/%{_bindir}/protoc-gen-gogo
install -m 755 _bin/protoc-gen-gogofast %{buildroot}/%{_bindir}/protoc-gen-gogofast
install -m 755 _bin/protoc-gen-gogofaster %{buildroot}/%{_bindir}/protoc-gen-gogofaster
install -m 755 _bin/protoc-gen-gogoslick %{buildroot}/%{_bindir}/protoc-gen-gogoslick
install -m 755 _bin/protoc-gen-gogotypes %{buildroot}/%{_bindir}/protoc-gen-gogotypes
install -m 755 _bin/protoc-gen-gostring %{buildroot}/%{_bindir}/protoc-gen-gostring
install -m 755 _bin/protoc-min-version %{buildroot}/%{_bindir}/protoc-min-version

# source codes for building projects
files="$(find . -iname *.golden) $(find . -iname *.proto) $(find . -iname testdata -type d)"
%goinstall ${files}


%check
%gochecks -t protoc-gen-gogo -d test/dashfilename -d test/embedconflict -d test/issue270 -r .*/unsafeunmarshaler -r .*/unsafeboth -r .*/unsafemarshaler -d test/packed

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files
%license LICENSE
%doc CONTRIBUTORS README
%{_bindir}/gogoreplace
%{_bindir}/protoc-gen-combo
%{_bindir}/protoc-gen-gofast
%{_bindir}/protoc-gen-gogo
%{_bindir}/protoc-gen-gogofast
%{_bindir}/protoc-gen-gogofaster
%{_bindir}/protoc-gen-gogoslick
%{_bindir}/protoc-gen-gogotypes
%{_bindir}/protoc-gen-gostring
%{_bindir}/protoc-min-version


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS README


%changelog
* Thu Nov 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Release 1.1.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.4-0.9.git100ba4e
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.4-0.8.git100ba4e
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.7.git100ba4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.4-0.6.git100ba4e
- Bump to 100ba4e885062801d56799d78530b73b178a78f3

* Wed Mar 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.4-0.5.gitf6b4bb7
- Update to spec 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.4.gitf6b4bb7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.3.gitf6b4bb7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.2.gitf6b4bb7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.4-0.1.gitf6b4bb7
- Bump to upstream f6b4bb7b2dde1736b809b3da996ed72f278e9be9
  resolves: #1428951

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-0.6.gitd7788ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.2-0.5.gitd7788ac
- Bump to upstream d7788ac7ca647999a3775cb756e449ab177dd138
  related: #1246215

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0.2-0.4.gite18d7aa
- Polish the spec file
  related: #1246215

* Wed Aug 03 2016 jchaloup <jchaloup@redhat.com> - 0.2-0.3.gite18d7aa
- Bump to upstream e18d7aa8f8c624c915db340349aad4c49b10d173
  related: #1246215

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-0.2.gitc3995ae
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0.2-0.1.gitc3995ae
- Bump to upstream c3995ae437bb78d1189f4f147dfe5f87ad3596e4
  related: #1246215

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.gite8904f5
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 18 2016 jchaloup <jchaloup@redhat.com> - 0.1-0.3.gite8904f5
- Bump to upstream e8904f58e872a473a5b91bc9bf3377d223555263
  related: #1246215

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.git8edb24c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 jchaloup <jchaloup@redhat.com> - 0.1-0.1.git8edb24c
- Bump to upstream 8edb24c179ed858a38f18920d9005c2dde05ec17
  related: #1246215

* Sat Aug 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.13.git5ba1012
- Update spec file to spec-2.0
  related: #1246215

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git5ba1012
- Bump to upstream 5ba1012ef3868db1b9ff374280a558c1bfff39c3
- Disable tests
  resolves: #1246215

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitbc946d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.gitbc946d0
- Bump to upstream bc946d07d1016848dfd2507f90f0859c9471681e
  import path has changed -> add devel package to keep back compatibility
  with code.google.com/p/gogoprotobuf import paths

* Fri Sep 19 2014 jchaloup <jchaloup@redhat.com> - 0-0.9.gitd228c1a
- initial commit (package review #1120882)

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.8.gitd228c1a
- preserve timestamps
- don't own golang dirs
- don't redifine gopath
- ExcluseBuild for goarches

* Thu Jul 17 2014 Colin Walters <walters@verbum.org> - 0-0.7.gitd228c1a
- Initial package
