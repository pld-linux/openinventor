Summary:	Open Inventor 3D toolkit
Summary(pl):	Open Inventor - toolkit 3D
Name:		openinventor
Version:	2.1.5
%define	subver	7
Release:	%{subver}.1
License:	LGPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/AplicaÁıes/Gr·ficos
Source0:	ftp://oss.sgi.com/projects/inventor/download/inventor-%{version}-%{subver}.src.tar.gz
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-nodisplay.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-nobash.patch
URL:		http://oss.sgi.com/projects/inventor
BuildRequires:	XFree86-devel => 3.3.6
BuildRequires:	OpenGL-devel
BuildRequires:	motif-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	freetype >= 2.0.1
BuildRequires:	flex
BuildRequires:	bison
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
Open Inventor jest zorientowanym obiektowo toolkitem 3D, ktÛry
upraszcza zadanie programowania grafiki do zestawu ≥atwych do uøycia
obiektÛw. Moøna uøywaÊ obiektÛw pocz±wszy od niskiego poziomu,
zwi±zanego z danymi (np. kula, kamera, materia≥, ∂wiat≥o) do
wysokiego, zwi±zanego z aplikacj± (np. edytor materia≥Ûw).

%package devel
Summary:	Open Inventor for programmers
Summary(pl):	Open Inventor dla programistÛw
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Obsoletes:	sgi-OpenInventor-devel

%description devel
Package for programmers using Open Inventor. Contains header files,
API documentation and examples.

%description devel -l pl
Pakiet dla programistÛw korzystaj±cych z Open Inventora. Zawiera pliki
nag≥Ûwkowe, dokumentacjÍ API i przyk≥ady.

%package static
Summary:	Open Inventor static libraries
Summary(pl):	Biblioteki statyczne Open Inventora
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Open Inventor static libraries.

%description static -l pl
Biblioteki statyczne Open Inventora.

%package demos
Summary:	Open Inventor demos
Summary(pl):	Programy demonstracyjne Open Inventora
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/AplicaÁıes/Gr·ficos
Requires:	%{name} = %{version}

%description demos
Demonstration programs for Open Inventor.

%description demos -l pl
Programy demonstruj±ce moøliwo∂ci Open Inventora.

%prep
%setup -q -n inventor
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
LD_LIBRARY_PATH="`pwd`/lib:`pwd`/libSoXt"; export LD_LIBRARY_PATH
%{__make} OPTIMIZER="%{rpmcflags}" YACC="bison -y"

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

(cd $RPM_BUILD_ROOT%{_mandir}
mv -f man1/inventor.1 man7/inventor.7
)

gzip -9nf KNOWN.BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc KNOWN.BUGS.gz
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
%attr(755,root,root) %{_bindir}/gview
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
