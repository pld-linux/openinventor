Summary:	Open Inventor
Summary(pl):	Open Inventor
Name:		OpenInventor
Version:	2.1.5
Release:	1
Copyright:	GPL
Group:		X11/Graphics
Group(pl):	X11/Grafika
Source0:	ftp://oss.sgi.com/projects/inventor/download/invertor-%{version}-6.src.tar.gz
#Patch0:		
BuildRequires:	XFree86-devel => 3.3.6
BuildRequires:	OpenGL-devel => 4.0
BuildRequires:	Motif-devel
URL:		http://oss.sgi.com/projects/inventor
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
From SGI page:...
"Open Inventor (TM) is an object-oriented 3D toolkit offering a comprehensive
solution to interactive graphics programming problems.
It presents a programming model based on a 3D scene database that dramatically
simplifies graphics programming. It includes a rich set of objects such as 
cubes, polygons, text, materials, cameras, lights, trackballs, handle boxes,
3D viewers, and editors that speed up your programming time and 
extend your 3D programming capabilities.

%description -l pl

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
