Name:           java_binfmt
Version:        1.0.3
Release:        %mkrel 6
Epoch:          0
Summary:        Java Binary Kernel Support for Linux
License:        GPL
Group:          Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://developer.osdl.org/dev/robustmutexes/src/fusyn.hg/Documentation/java.txt
Source0:        %{name}-%{version}.tar.bz2
Requires(post): rpm-helper
Requires(preun): rpm-helper

%description
With this package, you can directly execute Java applications and
applets. The binfmt_misc kernel module must be loaded.

%prep
%setup -q

%build
%{__cc} -Wall %{optflags} -o javaclassname javaclassname.c

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a javaclassname %{buildroot}%{_bindir}/javaclassname
%{__cp} -a javawrapper %{buildroot}%{_bindir}/javawrapper
%{__cp} -a jarwrapper %{buildroot}%{_bindir}/jarwrapper
%{__cp} -a jarwrapper %{buildroot}%{_bindir}/appletviewerwrapper
%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a java_binfmt.init %{buildroot}%{_initrddir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(0644,root,root,0755)
%doc java.txt
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0755,root,root) %{_bindir}/jarwrapper
%attr(0755,root,root) %{_bindir}/javaclassname
%attr(0755,root,root) %{_bindir}/javawrapper
%attr(0755,root,root) %{_bindir}/appletviewerwrapper
