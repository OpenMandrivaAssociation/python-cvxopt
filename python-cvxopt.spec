%define  module	cvxopt
%define name   	python-%{module}
%define version 0.9
%define release %mkrel 1

Summary: 	Free convex optimization package for Python
Name: 	      	%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.bz2
Patch0:		setup32.py.patch
Patch1:		setup64.py.patch
License:	GPL
Group:		Development/Python
Url:		http://abel.ee.ucla.edu/cvxopt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libgfortran
BuildRequires:	libgfortran, python-devel
BuildRequires:	blas-devel, lapack-devel, fftw3-devel, glpk-devel

%description
CVXOPT is a free software package for convex optimization based on the
Python programming language. It provides

* efficient Python classes for dense and sparse matrices (real and
  complex), with Python indexing and slicing and overloaded operations
  for matrix arithmetic;

* an interface to most of the double-precision real and complex BLAS;

* an interface to LAPACK routines for solving linear equations and
  least-squares problems, matrix factorizations (LU, Cholesky, LDL and
  QR), eigenvalue and singular value decomposition;

* an interface to the fast Fourier transform routines from FFTW

* interfaces to the sparse LU and Cholesky solvers from UMFPACK and CHOLMOD

* routines for solving convex optimization problems, interfaces to the
  linear programming solver in GLPK and the semidefinite programming
  solver in DSDP5

* a modeling tool for specifying convex piecewise-linear optimization problems.

%prep
%setup -q -n %{module}-%{version}
%ifarch x86_64
%patch1 -p0
%else
%patch0 -p0
%endif

%build
cd src/
%__python setup.py build

%install
%__rm -rf %{buildroot}
cd src/
%__python setup.py install --root=%{buildroot} --record=../INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/cvxopt examples/ LICENSE
