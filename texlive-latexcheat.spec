# revision 15878
# category Package
# catalog-ctan /info/latexcheat/latexcheat
# catalog-date 2009-04-07 08:49:48 +0200
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-latexcheat
Version:	1.13
Release:	11
Summary:	A LaTeX cheat sheet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.13-2
+ Revision: 753134
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.13-1
+ Revision: 718814
- texlive-latexcheat
- texlive-latexcheat
- texlive-latexcheat
- texlive-latexcheat

