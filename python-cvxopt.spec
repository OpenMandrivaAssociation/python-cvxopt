%define build_doc	0
%define module	cvxopt
#define __noautoreq 'lib(s|t)atlas\\.so'

Summary: 	Free convex optimization package for Python
Name: 	      	python-%{module}
Version:	1.3.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/cvxopt/cvxopt-%{version}.tar.gz
# dropped (no longer applies): Patch0:		%{name}-setup.patch
License:	GPLv3+
Group:		Development/Python
Url:		https://cvxopt.org/
Requires:	gcc-gfortran
BuildRequires:	make
BuildRequires:	gcc-gfortran
BuildRequires:	python-sphinx
BuildRequires:	suitesparse-devel
BuildRequires:	fftw3-devel
BuildRequires:	glpk-devel
BuildRequires:	gsl-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
#BuildRequires:	pkgconfig(atlas)
BuildRequires:	pkgconfig(flexiblas)

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
%autosetup -p1 -n cvxopt-1.3.3
# setup() does not pass a version, so the egg metadata becomes 0.0.0.
sed -i "s/setup (name = 'cvxopt',/setup (name = 'cvxopt', version='%{version}',/" setup.py

%build
# OpenMandriva ships BLAS/LAPACK through flexiblas. There is no libblas.so
# or liblapack.so. The 1.3.2 package also built the gsl, fftw, and glpk
# extensions; 1.3.3 leaves them off unless these are set, and their
# libraries live in /usr/lib64, not /usr/lib.
export CVXOPT_BLAS_LIB=flexiblas
export CVXOPT_LAPACK_LIB=flexiblas
export CVXOPT_BLAS_LIB_DIR=%{_libdir}
export CVXOPT_BUILD_GSL=1
export CVXOPT_GSL_LIB_DIR=%{_libdir}
export CVXOPT_GSL_INC_DIR=%{_includedir}/gsl
export CVXOPT_BUILD_FFTW=1
export CVXOPT_FFTW_LIB_DIR=%{_libdir}
export CVXOPT_FFTW_INC_DIR=%{_includedir}
export CVXOPT_BUILD_GLPK=1
export CVXOPT_GLPK_LIB_DIR=%{_libdir}
export CVXOPT_GLPK_INC_DIR=%{_includedir}
export CVXOPT_SUITESPARSE_LIB_DIR=%{_libdir}
export CVXOPT_SUITESPARSE_INC_DIR=%{_includedir}/suitesparse
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
