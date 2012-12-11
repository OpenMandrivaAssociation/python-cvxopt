%define module	cvxopt
%define name   	python-%{module}
%define version 1.1.4
%define release %mkrel 1

Summary: 	Free convex optimization package for Python
Name: 	      	%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
Patch0:		setup32.py.patch
Patch1:		setup64.py.patch
Patch2:		cvxopt-1.1.3-underlink.patch
License:	GPLv3+
Group:		Development/Python
Url:		http://abel.ee.ucla.edu/cvxopt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	gcc-gfortran
BuildRequires:	gcc-gfortran, python-sphinx
BuildRequires:	blas-devel, lapack-devel, fftw3-devel, glpk-devel
%py_requires -d

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
%ifarch x86_64
%patch1 -p0
%else
%patch0 -p0
%endif
%patch2 -p1

%build
pushd src/
PYTHONDONTWRITEBYTECODE= %__python setup.py build
popd
make -C doc html

%install
%__rm -rf %{buildroot}
pushd src/
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=../FILE_LIST
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc doc/build/html examples/ LICENSE


%changelog
* Wed Jan 11 2012 Lev Givon <lev@mandriva.org> 1.1.4-1
+ Revision: 759656
- Update to 1.1.4.

* Sat Dec 03 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1.3-4
+ Revision: 737558
- Do not explicitly require libgfortran but gcc-gfortran.

* Wed Nov 03 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.1.3-2mdv2011.0
+ Revision: 593037
+ rebuild (emptylog)

* Tue Oct 19 2010 Lev Givon <lev@mandriva.org> 1.1.3-1mdv2011.0
+ Revision: 586754
- Update to 1.1.3.

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 551363
- Update to 1.1.2.

* Wed Apr 01 2009 Lev Givon <lev@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 363359
- Update to 1.1.1.

* Tue Jan 06 2009 Lev Givon <lev@mandriva.org> 1.1-1mdv2009.1
+ Revision: 326017
- Update to 1.1.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 269021
- rebuild early 2009.0 package (before pixel changes)

* Fri May 02 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2009.0
+ Revision: 200193
- Update to 1.0.

* Mon Feb 25 2008 Lev Givon <lev@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 174864
- Update to 0.9.3.

* Thu Jan 03 2008 Lev Givon <lev@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 142318
- Update to 0.9.2.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Lev Givon <lev@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 116321
- Update to 0.9.1.
  Use new devel library naming policy.

* Fri Nov 09 2007 Lev Givon <lev@mandriva.org> 0.9-2mdv2008.1
+ Revision: 106990
- Bump release to rebuild against lapack 3.1.1.
- Update to 0.9.

* Sun Aug 05 2007 Lev Givon <lev@mandriva.org> 0.8.2-1mdv2008.0
+ Revision: 59131
- Import python-cvxopt



* Wed Jun 13 2007 Lev Givon <lev@mandriva.org> 0.8.2-1mdv2007.1
- Initial Mandriva package.
