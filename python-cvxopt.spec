%define build_doc	0
%define module	cvxopt
%define __noautoreq 'lib(s|t)atlas\\.so'

Summary: 	Free convex optimization package for Python
Name: 	      	python-%{module}
Version:	1.3.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cvxopt/cvxopt-%{version}.tar.gz
Patch0:		%{name}-setup.patch
License:	GPLv3+
Url:		https://cvxopt.org/
Requires:	gcc-gfortran
BuildRequires:	gcc-gfortran
BuildRequires:	python-sphinx
BuildRequires:	suitesparse-devel
BuildRequires:	fftw3-devel
BuildRequires:	glpk-devel
BuildRequires:	gsl-devel
BuildRequires:	python3-devel
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(atlas)

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
%autopatch -p1

# Fix library path
%if "%{_lib}" != "lib"
  sed -i "s|/usr/lib|%{_libdir}|" setup.py
%endif

cp -a . %py2dir


%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build build_ext -lm
%if %{build_doc}
make -C doc html
%endif

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%if %{build_doc}
%doc doc/build/html
%endif
%doc examples/ LICENSE
%py3_platsitedir/cvxopt
%py3_platsitedir/cvxopt*.egg-info
