Summary:	Open Inventor 3D toolkit
Summary(pl):	Open Inventor - toolkit 3D
Name:		openinventor
Version:	2.1.5
%define	subver	7
Release:	%{subver}.3
License:	LGPL
Group:		X11/Applications/Graphics
Source0:	ftp://oss.sgi.com/projects/inventor/download/inventor-%{version}-%{subver}.src.tar.gz
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-nodisplay.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-nobash.patch
Patch6:		%{name}-gcc3.patch
Patch7:		%{name}-dprintf.patch
Patch8:		%{name}-morearchs.patch
URL:		http://oss.sgi.com/projects/inventor/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel => 3.3.6
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype >= 2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	motif-devel
Requires:	OpenGL
Obsoletes:	sgi-OpenInventor-clients
Obsoletes:	sgi-OpenInventor-data
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Open Inventor 3D Toolkit is an object-oriented toolkit that
simplifies and abstracts the task of writing graphics programming into
a set of easy to use objects. These objects range from low-level
data-centered objects such as Sphere, Camera, Material, Light, and
Group, to high-level application-level objects such as Walk Viewer and
Material Editor. The foundation concept in Inventor is the "scene
database" which defines the objects to be used in an application. When
using Inventor, a programmer creates, edits, and composes these
objects into hierarchical 3D scene graphs (i.e. database). A variety
of fundamental application tasks such as rendering, picking, event
handling, and file reading/writing are built-in operations of all
objects in the database and thus are simple to invoke.

%description -l pl
Open Inventor jest zorientowanym obiektowo toolkitem 3D, który
upraszcza zadanie programowania grafiki do zestawu ³atwych do u¿ycia
obiektów. Mo¿na u¿ywaæ obiektów pocz±wszy od niskiego poziomu,
zwi±zanego z danymi (np. kula, kamera, materia³, ¶wiat³o) do
wysokiego, zwi±zanego z aplikacj± (np. edytor materia³ów).

%package devel
Summary:	Open Inventor for programmers
Summary(pl):	Open Inventor dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	sgi-OpenInventor-devel

%description devel
Package for programmers using Open Inventor. Contains header files,
API documentation and examples.

%description devel -l pl
Pakiet dla programistów korzystaj±cych z Open Inventora. Zawiera pliki
nag³ówkowe, dokumentacjê API i przyk³ady.

%package static
Summary:	Open Inventor static libraries
Summary(pl):	Biblioteki statyczne Open Inventora
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Open Inventor static libraries.

%description static -l pl
Biblioteki statyczne Open Inventora.

%package demos
Summary:	Open Inventor demos
Summary(pl):	Programy demonstracyjne Open Inventora
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description demos
Demonstration programs for Open Inventor.

%description demos -l pl
Programy demonstruj±ce mo¿liwo¶ci Open Inventora.

%prep
%setup -q -n inventor
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
# use freetype-based libFL instead of precompiled x86 binary libFL.a
rm -f libFL/src/libFL.a
FREETYPE=1; export FREETYPE

LD_LIBRARY_PATH="`pwd`/lib:`pwd`/libSoXt"; export LD_LIBRARY_PATH
%{__make} OPTIMIZER="%{rpmcflags} %{!?debug:-DNDEBUG}" YACC="bison -y"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/InventorDSO,%{_mandir}/man7} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	IVROOT=$RPM_BUILD_ROOT

install lib/lib*.a libSoXt/lib*.a $RPM_BUILD_ROOT%{_libdir}
install apps/nodes/*/*.so $RPM_BUILD_ROOT%{_libdir}/InventorDSO
install apps/demos/*/*.about $RPM_BUILD_ROOT%{_datadir}/Inventor/help
cp -rf apps/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv -f $RPM_BUILD_ROOT%{_mandir}/man{1/inventor.1,7/inventor.7}

# resolve conflict with gview
mv -f $RPM_BUILD_ROOT%{_bindir}/{gview,invgview}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc KNOWN.BUGS
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_libdir}/InventorDSO
%attr(755,root,root) %{_libdir}/InventorDSO/*.so
%attr(755,root,root) %{_bindir}/iv2toiv1
%attr(755,root,root) %{_bindir}/ivcat
%attr(755,root,root) %{_bindir}/ivdowngrade
%attr(755,root,root) %{_bindir}/ivfix
%attr(755,root,root) %{_bindir}/ivinfo
%attr(755,root,root) %{_bindir}/ivview
%attr(755,root,root) %{_bindir}/SceneViewer
%dir %{_datadir}/Inventor
%dir %{_datadir}/Inventor/data
%{_datadir}/Inventor/data/models
%dir %{_datadir}/Inventor/help
%{_datadir}/Inventor/help/*.help
%{_datadir}/Inventor/help/SceneViewer.about
%{_datadir}/Inventor/help/ivview.about
%{_mandir}/man1/*
%{_mandir}/man7/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/drop
%attr(755,root,root) %{_bindir}/invgview
%attr(755,root,root) %{_bindir}/maze
%attr(755,root,root) %{_bindir}/noodle
%attr(755,root,root) %{_bindir}/qmorf
%attr(755,root,root) %{_bindir}/revo
%attr(755,root,root) %{_bindir}/textomatic
%{_datadir}/Inventor/data/demos
%{_datadir}/Inventor/help/noodle.about
%{_datadir}/Inventor/help/qmorf.about
%{_datadir}/Inventor/help/revo.about
%{_datadir}/Inventor/help/textomatic.about
