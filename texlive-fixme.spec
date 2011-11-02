Name:		texlive-fixme
Version:	4.1
Release:	1
Summary:	Insert "fixme" notes into draft documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixme
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a way to insert fixme notes in documents
being developed (in draft mode). Such notes can appear in the
margin of the document, as index entries, in the log file and
as warnings on stdout. It is also possible to summarize them in
a list. If your document is in a final version, any remaining
fixme notes will produce an error. FiXme also comes with
support for AUC-TeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixme/fixme.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/env/fxenvlayoutcolor.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/env/fxenvlayoutcolorsig.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutmarginnote.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfcmargin.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfcnote.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfcsigmargin.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfcsignote.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfmargin.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfnote.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfsigmargin.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/fxlayoutpdfsignote.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/target/fxtargetlayoutchangebar.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/target/fxtargetlayoutcolor.sty
%{_texmfdistdir}/tex/latex/fixme/layouts/target/fxtargetlayoutcolorcb.sty
%{_texmfdistdir}/tex/latex/fixme/themes/fxthemecolor.sty
%{_texmfdistdir}/tex/latex/fixme/themes/fxthemecolorsig.sty
%{_texmfdistdir}/tex/latex/fixme/themes/fxthemesignature.sty
%doc %{_texmfdistdir}/doc/latex/fixme/NEWS
%doc %{_texmfdistdir}/doc/latex/fixme/README
%doc %{_texmfdistdir}/doc/latex/fixme/THANKS
%doc %{_texmfdistdir}/doc/latex/fixme/fixme.el
%doc %{_texmfdistdir}/doc/latex/fixme/fixme.pdf
%doc %{_texmfdistdir}/doc/latex/fixme/header.inc
#- source
%doc %{_texmfdistdir}/source/latex/fixme/fixme.dtx
%doc %{_texmfdistdir}/source/latex/fixme/fixme.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
