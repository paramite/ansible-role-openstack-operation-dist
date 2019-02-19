%global srcname ansible_role_openstack_operations
%global rolename ansible-role-openstack-operations
%global commit          784a2cd80a2e550ae4e068264ba618ce704956c1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Perform various common OpenStack operations by calling this role with an action and appropriate variables.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-openstack-operations
#Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz
# Note(mmagr): Project is not versioned. Gonna use the above source as soon as it will be
Source0:        https://github.com/openstack/%{rolename}/archive/%{commit}.tar.gz#/%{rolename}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires: ansible

%description
Perform various common OpenStack operations by calling this role with an action and appropriate variables.

%prep
%autosetup -n %{rolename}-%{commit} -S git

%build
%py2_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py2_install


%files
%doc README*
%license LICENSE
%{python2_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Mon Feb 18 2019 Martin Mágr <mmagr@redhat.com> 1.0.0-1
- Initial package
