Summary: A file compression utility.
Name: bzip2
Version: 1.0.2
Release: 4
License: BSD
Group: Applications/File
URL: http://sources.redhat.com/bzip2/
Source: ftp://sources.redhat.com/pub/bzip2/v102/bzip2-%{version}.tar.gz
Patch: bzip2-1.0.2-saneso.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: bzip2-libs = %{version}

%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities 
of the best techniques available.  However, bzip2 has the added benefit 
of being approximately two times faster at compression and six times 
faster at decompression than those techniques.  Bzip2 is not the 
fastest compression utility, but it does strike a balance between speed 
and compression capability.

Install bzip2 if you need a compression utility.

%package devel
Summary: Header files and libraries for developing apps which will use bzip2.
Group: Development/Libraries
Requires: bzip2 = %{version}, bzip2-libs = %{version}

%description devel

Header files and a static library of bzip2 functions, for developing apps
which will use the library.

%package libs
Summary: Libraries for applications using bzip2
Group: System Environment/Libraries

%description libs

Libraries for applications using the bzip2 compression format.

%prep
%setup -q 
%patch -p1

%build
make -f Makefile-libbz2_so CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -fpic -fPIC" all
rm -f *.o
make CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64" all

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1,%{_libdir},%{_includedir}}
install -m 755 bzlib.h $RPM_BUILD_ROOT/%{_includedir}
install -m 755 libbz2.so.1.0.2 $RPM_BUILD_ROOT/%{_libdir}
install -m 755 libbz2.a $RPM_BUILD_ROOT/%{_libdir}
install -m 755 bzip2-shared  $RPM_BUILD_ROOT/%{_bindir}/bzip2
install -m 755 bzip2recover bzgrep bzdiff bzmore  $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 bzip2.1 bzdiff.1 bzgrep.1 bzmore.1  $RPM_BUILD_ROOT/%{_mandir}/man1/
ln -s bzip2 $RPM_BUILD_ROOT/%{_bindir}/bunzip2
ln -s bzip2 $RPM_BUILD_ROOT/%{_bindir}/bzcat
ln -s bzdiff $RPM_BUILD_ROOT/%{_bindir}/bzcmp
ln -s bzmore $RPM_BUILD_ROOT/%{_bindir}/bzless
ln -s libbz2.so.1.0.2 $RPM_BUILD_ROOT/%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT/%{_libdir}/libbz2.so
ln -s bzip2.1 $RPM_BUILD_ROOT/%{_mandir}/man1/bzip2recover.1
ln -s bzip2.1 $RPM_BUILD_ROOT/%{_mandir}/man1/bunzip2.1
ln -s bzip2.1 $RPM_BUILD_ROOT/%{_mandir}/man1/bzcat.1
ln -s bzdiff.1 $RPM_BUILD_ROOT/%{_mandir}/man1/bzcmp.1
ln -s bzmore.1 $RPM_BUILD_ROOT/%{_mandir}/man1/bzless.1


%post libs -p /sbin/ldconfig

%postun libs  -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README README.COMPILATION.PROBLEMS Y2K_INFO NEWS ChangeLog
%{_bindir}/*
%{_mandir}/*/*

%files libs
%defattr(-,root,root)
%{_libdir}/*so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*so

%changelog
* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-3
- Rebuild in new environment

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-2
- Rebuild

* Wed Jan 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.2-1
- 1.0.2
- Total overhaul of build precedure
- Add many small helper programs added to 1.0.2
- drop old patches

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-5
- Don't segfault when infile is a directory and "-f" is used (#56623)
- Automake is evil. Add workaround

* Fri Mar 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use "License" instead of "Copyright"
- split out libs

* Fri Jul 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new URL and source location

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jul 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.0.1
- ported my patch

* Tue Jun 13 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging to build on solaris2.5.1.
- remove config.cache from autoconf patch.
- sparc: use %%configure, but not the m4 macros.

* Tue Jun 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Use %%configure, %%makeinstall, %%{_manpath} and %%{_tmpdir}

* Wed May 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.0.0 - ported my 1.0pre8 libtoolizedautoconf patch

* Tue May 16 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use soft links, not hardlinks, for binaries
- mv .so to devel

* Mon May 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- autoconfed and libtoolized package 
- fixed Copyright (it's BSD, not GPL)
- dumped bzless (less works fine with bz2-files)
- rewrote build and install parts
- separated main package and devel package

* Mon May  8 2000 Bernhard Rosenkränzer <bero@redhat.com>
- 1.0pre8

* Fri Apr 14 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Add bzgrep (a version of zgrep hacked to do bzip2)

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Fri Dec 31 1999 Bernhard Rosenkränzer <bero@redhat.com>
- 0.9.5d
- Update download URL, add URL: tag in header

* Tue Aug 10 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 0.9.5c.

* Mon Aug  9 1999 Bill Nottingham <notting@redhat.com>
- install actual bzip2 binary, not libtool cruft.

* Sun Aug  8 1999 Jeff Johnson <jbj@redhat.com>
- run ldconfig to get shared library.

* Mon Aug  2 1999 Jeff Johnson <jbj@redhat.com>
- create shared libbz1.so.* library.

* Sun Apr  4 1999 Jeff Johnson <jbj@redhat.com>
- update to bzip2-0.9.0c.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- force compilation with egcs to avoid gcc optimization bug (thank God 
  we haven't been beaten by it)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- version 0.9.0b

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.9.0

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- first build for Manhattan
