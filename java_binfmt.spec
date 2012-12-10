Name:           java_binfmt
Version:        1.0.3
Release:        %mkrel 7
Epoch:          0
Summary:        Java Binary Kernel Support for Linux
License:        GPL
Group:          Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://developer.osdl.org/dev/robustmutexes/src/fusyn.hg/Documentation/java.txt
Source0:        %{name}-%{version}.tar.bz2
Patch0:		jarwrapper.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper

%description
With this package, you can directly execute Java applications and
applets. The binfmt_misc kernel module must be loaded.

%prep
%setup -q
%patch0 -p0

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


%changelog
* Wed Oct 13 2010 Lev Givon <lev@mandriva.org> 0:1.0.3-7mdv2011.0
+ Revision: 585434
- Fix bug #61270.

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:1.0.3-6mdv2010.0
+ Revision: 429594
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.0.3-5mdv2009.0
+ Revision: 247389
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 David Walluck <walluck@mandriva.org> 0:1.0.3-3mdv2008.1
+ Revision: 117654
- rebuild


* Sat Dec 09 2006 David Walluck <walluck@mandriva.org> 1.0.3-2mdv2007.0
+ Revision: 93935
- use preferred appletviewer

* Fri Dec 08 2006 David Walluck <walluck@mandriva.org> 0:1.0.3-1mdv2007.1
+ Revision: 93843
- 1.0.3
- Import java_binfmt

* Mon Jul 24 2006 David Walluck <walluck@mandriva.org> 1.0.2-11mdv2007.0
- fix PreReq use

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-10mdk 
- better description (Adam Williamson <awilliamson@mandriva.com>)

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-9mdk 
- spec cleanup

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0.2-8mdk 
- rebuild

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0.2-7mdk
- more macros

