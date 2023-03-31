Name:		texlive-fixme
Version:	63708
Release:	2
Summary:	Insert "fixme" notes into draft documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixme
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a way to insert fixme notes in documents
being developed (in draft mode). Such notes can appear in the
margin of the document, as index entries, in the log file and
as warnings on stdout. It is also possible to summarize them in
a list. If your document is in a final version, any remaining
fixme notes will produce an error. FiXme also comes with
support for AUC-TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixme
%doc %{_texmfdistdir}/doc/latex/fixme
#- source
%doc %{_texmfdistdir}/source/latex/fixme

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
