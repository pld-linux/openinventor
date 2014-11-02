Summary:	Open Inventor 3D toolkit
Summary(pl.UTF-8):	Open Inventor - toolkit 3D
Name:		openinventor
%define	ver	2.1.5
%define	subver	10
Version:	%{ver}.%{subver}
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications/Graphics
Source0:	ftp://oss.sgi.com/projects/inventor/download/inventor-%{ver}-%{subver}.src.tar.gz
# Source0-md5:	82208096f1e0b111160e864e239c3a51
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-c++.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-nobash.patch
Patch7:		%{name}-dprintf.patch
Patch8:		%{name}-morearchs.patch
Patch9:		%{name}-freetype-includes.patch
Patch10:	%{name}-bison.patch
URL:		http://oss.sgi.com/projects/inventor/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype >= 2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	motif-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXp-devel
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	sgi-OpenInventor-clients
Obsoletes:	sgi-OpenInventor-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Open Inventor jest zorientowanym obiektowo toolkitem 3D, który
upraszcza zadanie programowania grafiki do zestawu łatwych w użyciu
obiektów. Można używać obiektów począwszy od niskiego poziomu,
związanego z danymi (np. sfera, kamera, materiał, światło, grupa) do
wysokiego, związanego z aplikacją (np. przeglądarka ścieżki, edytor
materiałów). Podstawową ideą w Inventorze jest "bza danych sceny",
definiująca obiekty, jakie mają być użyte w aplikacji. Przy użyciu
Inventora programista tworzy, modyfikuje i komponuje te obiekty w
hierarchiczne grafy sceny trójwymiarowej (czyli bazę danych). Wiele
podstawowych zadań aplikacji, takich jak renderowanie, wybieranie,
obsługa elementów oraz odczyt/zapis plików są wbudowanymi operacjami
wszystkich obiektów w bazie danych, dzięki czemu są łatwe do
wywołania.

%package libs
Summary:	Open Inventor shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Open Inventora
Group:		X11/Libraries
Conflicts:	openinventor < 2.1.5.10

%description libs
Open Inventor shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Open Inventora.

%package devel
Summary:	Open Inventor for programmers
Summary(pl.UTF-8):	Open Inventor dla programistów
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	sgi-OpenInventor-devel

%description devel
Package for programmers using Open Inventor. Contains header files,
API documentation and examples.

%description devel -l pl.UTF-8
Pakiet dla programistów korzystających z Open Inventora. Zawiera pliki
nagłówkowe, dokumentację API i przykłady.

%package static
Summary:	Open Inventor static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Open Inventora
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Open Inventor static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Open Inventora.

%package demos
Summary:	Open Inventor demos
Summary(pl.UTF-8):	Programy demonstracyjne Open Inventora
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description demos
Demonstration programs for Open Inventor.

%description demos -l pl.UTF-8
Programy demonstrujące możliwości Open Inventora.

%prep
%setup -q -n inventor
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
export LD_LIBRARY_PATH="`pwd`/lib:`pwd`/libSoXt"
%{__make} \
	CXX="%{__cxx}" \
	FREETYPE=1 \
	IVLIBDIR="\$(IVROOT)%{_libdir}" \
	OPTIMIZER="%{rpmcflags} %{!?debug:-DNDEBUG}" \
	X11LIBDIR=%{_libdir} \
	YACC="bison -y"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/InventorDSO,%{_mandir}/man7,%{_datadir}/Inventor/demos/data} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	IVROOT=$RPM_BUILD_ROOT \
	IVLIBDIR="\$(IVROOT)%{_libdir}"

install apps/nodes/*/*.so $RPM_BUILD_ROOT%{_libdir}/InventorDSO
cp -p lib/lib*.a libSoXt/lib*.a $RPM_BUILD_ROOT%{_libdir}
cp -rf apps/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__mv} $RPM_BUILD_ROOT%{_mandir}/man{1/inventor.1,7/inventor.7}

# move demos data to another dir
%{__mv} $RPM_BUILD_ROOT%{_datadir}/Inventor/help/{noodle,qmorf,revo,textomatic}.about \
	$RPM_BUILD_ROOT%{_datadir}/Inventor/demos/data

# resolve conflict with gview
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{gview,ivgview}
# too generic name
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{drop,ivdrop}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ.misc KNOWN.BUGS README.FIRST
%attr(755,root,root) %{_bindir}/SceneViewer
%attr(755,root,root) %{_bindir}/iv2toiv1
%attr(755,root,root) %{_bindir}/ivcat
%attr(755,root,root) %{_bindir}/ivdowngrade
%attr(755,root,root) %{_bindir}/ivfix
%attr(755,root,root) %{_bindir}/ivinfo
%attr(755,root,root) %{_bindir}/ivview
%attr(755,root,root) %{_libdir}/InventorDSO/*.so
%dir %{_datadir}/Inventor
%dir %{_datadir}/Inventor/data
%{_datadir}/Inventor/data/models
%dir %{_datadir}/Inventor/help
%{_datadir}/Inventor/help/SoXt*.help
%{_datadir}/Inventor/help/SceneViewer.about
%{_datadir}/Inventor/help/ivview.about
%{_mandir}/man1/SceneViewer.1*
%{_mandir}/man1/iv2toiv1.1*
%{_mandir}/man1/ivcat.1*
%{_mandir}/man1/ivdowngrade.1*
%{_mandir}/man1/ivfix.1*
%{_mandir}/man1/ivinfo.1*
%{_mandir}/man1/ivview.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libInventor.so
%attr(755,root,root) %{_libdir}/libInventorXt.so
%dir %{_libdir}/InventorDSO

%files devel
%defattr(644,root,root,755)
%{_includedir}/Inventor
%{_mandir}/man3/Sb*.3iv*
%{_mandir}/man3/So*.3iv*
%{_mandir}/man7/inventor.7*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libInventor.a
%{_libdir}/libInventorXt.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ivdrop
%attr(755,root,root) %{_bindir}/ivgview
%attr(755,root,root) %{_bindir}/maze
%attr(755,root,root) %{_bindir}/noodle
%attr(755,root,root) %{_bindir}/qmorf
%attr(755,root,root) %{_bindir}/revo
%attr(755,root,root) %{_bindir}/textomatic
%{_datadir}/Inventor/demos
