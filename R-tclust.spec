%global packname  tclust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.03
Release:          1
Summary:          Robust Trimmed Clustering
Group:            Sciences/Mathematics
License:          GPLv3
URL:              https://cran.r-project.org/web/packages/tclust/index.html
Source0:          http://cran.r-project.org/src/contrib/tclust_1.1-03.tar.gz
BuildRequires:    R-devel R-mvtnorm R-sn R-mclust R-cluster libblas-devel liblapack-devel
Requires:    	  R-core R-mvtnorm R-sn R-mclust R-cluster

%description
Robust Trimmed Clustering

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R