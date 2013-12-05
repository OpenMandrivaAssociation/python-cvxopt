%define build_doc	0
%define module	cvxopt
%define name   	python-%{module}
%define version 1.1.6
%define release 1

Summary: 	Free convex optimization package for Python
Name: 	      	%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
Patch0:		%{name}-setup.py.patch
Patch1:		%{name}-underlink.patch
# Will submit patch0 to upstream ASAP
Patch2:         %{name}-fixglpkinclude.patch
# Sent upstream 31 Jul 2013.  Move from obsolete glpk API to new API.
Patch3:		%{name}-glpk.patch
License:	GPLv3+
Url:		http://abel.ee.ucla.edu/cvxopt
Requires:	gcc-gfortran
BuildRequires:	gcc-gfortran, python-sphinx
BuildRequires:	blas-devel, lapack-devel, fftw3-devel, glpk-devel, gsl-devel
BuildRequires:	python-devel

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

* a modeling tool for specifying convex piecewise-linear optimization problems
  (which has been superseded by the more powerful CVXMOD package).

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0

# Fix library path
%ifarch x86_64
  sed -i "s|/usr/lib|%{_libdir}|" setup.py
%endif

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
%if %{build_doc}
make -C doc html
%endif

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%if %{build_doc}
%doc doc/build/html
%endif
%doc examples/ LICENSE
