%global tl_name fixme
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.5
Release:	%{tl_revision}.1
Summary:	Collaborative annotation tool for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixme
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixme.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
FiXme is a collaborative annotation tool for LaTeX documents. Annotating
a document here refers to inserting meta-notes, that is, notes that do
not belong to the document itself, but rather to its development or
reviewing process. Such notes may involve things of different importance
levels, ranging from simple "fix the spelling" flags to critical "this
paragraph is a lie" mentions. Annotations like this should be visible
during the development or reviewing phase, but should normally disappear
in the final version of the document. FiXme is designed to ease and
automate the process of managing collaborative annotations, by offering
a set of predefined note levels and layouts, the possibility to register
multiple authors, to reference annotations by listing and indexing etc.
FiXme is extensible, giving you the possibility to create new layouts or
even complete "themes", and also comes with support for AUCTeX.

