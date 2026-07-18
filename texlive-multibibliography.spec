%global tl_name multibibliography
%global tl_revision 77682
%global tl_bin_links multibibliography:%{_texmfdistdir}/scripts/multibibliography/multibibliography.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Multiple versions of a bibliography, with different sort orders
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multibibliography
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibibliography.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(multibibliography.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Conventional standards for bibliography styles impose a forced choice
between index and name/year citations, and corresponding references. The
package avoids this choice, by providing alphabetic, sequenced, and even
chronological orderings of references. Inline citations, that integrate
these heterogeneous styles, are also supported (and work with other
bibliography packages).

