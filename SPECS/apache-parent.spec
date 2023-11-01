Name:           apache-parent
Version:        19
Release:        2%{?dist}
Summary:        Parent POM file for Apache projects
License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/apache/%{version}/apache-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)

# Not generated automatically
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
Requires:       mvn(org.apache:apache-jar-resource-bundle)

%description
This package contains the parent pom file for apache projects.

%prep
%setup -n apache-%{version}

%pom_remove_plugin :maven-site-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-1
- Update to upstream version 19
- Add missing BR on apache-resource-bundles

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 18-1
- Update to upstream version 18

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 17-1
- Update to upstream version 17

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 16-1
- Update to upstream version 16

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-1
- Update to upstream version 15

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 14-2
- Rebuild to regenerate Maven auto-requires

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 14-1
- Update to upstream version 14

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 10-15
- Remove maven-site-plugin from dependencies

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14
- Rebuild to regenerate Maven provides

* Thu Aug 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-13
- Add missing R: apache-resource-bundles

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 10-12
- Migrate away from mvn-rpmbuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 10-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 10-8
- Added license (Resolves: #888287)

* Wed Nov 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 10-7
- Install patched pom not the original

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-6
- Add missing R: maven-remote-resources-plugin, apache-resource-bundles
- Add %%check to verify dependencies during build

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 10-5
- Make sure we generate 1.5 version bytecode

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Andy Grimm <agrimm@gmail.com> 10-2
- Follow suggestions in BZ #736069

* Mon Aug 29 2011 Andy Grimm <agrimm@gmail.com> 10-1
- Initial Build
