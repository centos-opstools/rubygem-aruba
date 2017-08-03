%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from aruba-0.4.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name aruba

Summary: CLI Steps for Cucumber, hand-crafted for you in Aruba
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.14.2
Release: 1%{?dist}
Group: Development/Languages
# aruba itself is MIT
# icons in templates/images are CC-BY
# jquery.js itself is MIT or GPLv2
# jquery.js includes sizzle.js, which is MIT or BSD or GPLv2
License: MIT and CC-BY and (MIT or GPLv2) and (MIT or BSD or GPLv2)
URL: http://github.com/cucumber/aruba
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
Requires:      %{?scl_prefix}rubygem(cucumber) >= 1.3.19
Requires:      %{?scl_prefix}rubygem(childprocess) >= 0.5.6
Requires:      %{?scl_prefix}rubygem(childprocess) < 0.6
Requires:      %{?scl_prefix}rubygem(rspec-expectations) >= 2.99
Requires:      %{?scl_prefix}rubygem(contracts) >= 0.9
Requires:      %{?scl_prefix}rubygem(contracts) < 1
Requires:      %{?scl_prefix}rubygem(thor) >= 0.19
Requires:      %{?scl_prefix}rubygem(thor) < 1
Requires:      %{?scl_prefix}rubygem(ffi) >= 1.9.10
Requires:      %{?scl_prefix}rubygem(ffi) < 1.10
BuildRequires: %{?scl_prefix}rubygem(builder)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(cucumber) >= 1.1.1
BuildRequires: %{?scl_prefix}rubygem(childprocess) >= 0.2.0
BuildRequires: %{?scl_prefix}rubygem(rspec) >= 3
BuildRequires: %{?scl_prefix}rubygem(gherkin)
# Dependency missing
#BuildRequires: %{?scl_prefix}rubygem(multi_test)
# used in one of the features
BuildRequires: bc
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
%{?scl:Requires: %{?scl_prefix}runtime}

%description
Aruba is Cucumber extension for Command line applications written
in any programming language.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
# Dependency missing, therefore tests cannot be run
#cucumber rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{_bindir}/aruba
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.simplecov
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/TODO.md
%{gem_instdir}/appveyor.yml
%{gem_instdir}/bin
%{gem_instdir}/config
%{gem_instdir}/cucumber.yml
%{gem_instdir}/features
%{gem_instdir}/fixtures
%{gem_libdir}
%{gem_instdir}/script
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/aruba.gemspec
%doc %{gem_instdir}/doc
%{gem_instdir}/spec

%changelog
* Wed Sep 21 2016 Rich Megginson <rmeggins@redhat.com> - 0.14.2-1
- update for 0.14.2

* Wed Feb 24 2016 Pavel Valena <pvalena@redhat.com> - 0.6.2-4
- Add scl macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.2-1
- 0.6.2

* Mon Sep  1 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1-1
- 0.6.1

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0-1
- 0.6.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.4-1
- 0.5.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Josef Stribny <jstribny@redhat.com> - 0.5.2-1
- Update to aruba 0.5.2

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 0.4.11-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-5
- Disable tests that do not actually test anything (patch from upstream).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-2
- Remove the ffi dependency and add conflicts with the problematic version.

* Fri Feb 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-1
- Initial package
