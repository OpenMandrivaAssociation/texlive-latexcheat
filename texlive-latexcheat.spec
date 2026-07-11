%global tl_name latexcheat
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	A LaTeX cheat sheet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/latexcheat
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX reference sheet for writing scientific papers. Unlike many other
such sheets, this sheet does not focus on typesetting mathematics
(though it does list some symbols).

