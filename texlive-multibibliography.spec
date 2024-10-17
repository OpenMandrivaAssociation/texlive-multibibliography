Name:		texlive-multibibliography
Version:	30939
Release:	2
Summary:	Multiple versions of a bibliography, with different sort orders
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multibibliography
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-multibibliography.bin = %{EVRD}

%description
Conventional standards for bibliography styles impose a forced
choice between index and name/year citations, and corresponding
references. The package avoids this choice, by providing
alphabetic, sequenced, and even chronological orderings of
references. Inline citations, that integrate these
heterogeneous styles, are also supported (and work with other
bibliography packages).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/multibibliography
%{_texmfdistdir}/bibtex/bst/multibibliography/chronological.bst
%{_texmfdistdir}/scripts/multibibliography/multibibliography.pl
%{_texmfdistdir}/tex/latex/multibibliography/multibibliography.sty
%doc %{_texmfdistdir}/doc/latex/multibibliography/Makefile
%doc %{_texmfdistdir}/doc/latex/multibibliography/README
%doc %{_texmfdistdir}/doc/latex/multibibliography/figure.pdf
%doc %{_texmfdistdir}/doc/latex/multibibliography/multibibliography.bib
%doc %{_texmfdistdir}/doc/latex/multibibliography/multibibliography.pdf
%doc %{_texmfdistdir}/doc/latex/multibibliography/tug-paper.pdf
%doc %{_texmfdistdir}/doc/latex/multibibliography/tug-paper.tex
%doc %{_texmfdistdir}/doc/latex/multibibliography/type.bib
#- source
%doc %{_texmfdistdir}/source/latex/multibibliography/multibibliography.dtx
%doc %{_texmfdistdir}/source/latex/multibibliography/multibibliography.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/multibibliography/multibibliography.pl multibibliography
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
