Name:		texlive-latexcheat
Version:	15878
Release:	2
Summary:	A LaTeX cheat sheet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/latexcheat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A LaTeX reference sheet for writing scientific papers. Unlike
many other such sheets, this sheet does not focus on
typesetting mathematics (though it does list some symbols).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latexcheat/README
%doc %{_texmfdistdir}/doc/latex/latexcheat/latexsheet.pdf
%doc %{_texmfdistdir}/doc/latex/latexcheat/latexsheet.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
