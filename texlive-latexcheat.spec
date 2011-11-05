# revision 15878
# category Package
# catalog-ctan /info/latexcheat/latexcheat
# catalog-date 2009-04-07 08:49:48 +0200
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-latexcheat
Version:	1.13
Release:	1
Summary:	A LaTeX cheat sheet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX reference sheet for writing scientific papers. Unlike
many other such sheets, this sheet does not focus on
typesetting mathematics (though it does list some symbols).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latexcheat/README
%doc %{_texmfdistdir}/doc/latex/latexcheat/latexsheet.pdf
%doc %{_texmfdistdir}/doc/latex/latexcheat/latexsheet.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
