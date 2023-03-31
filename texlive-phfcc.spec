Name:		texlive-phfcc
Version:	60731
Release:	2
Summary:	Convenient inline commenting in collaborative documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfcc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfcc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfcc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfcc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Easily define helper macros to insert comments in a LaTeX
document. A convenient syntax enables you to mark text
additions (e.g., "... \phf{I'm adding this text} ..." or "...
\phf I'm adding this text\endphf ..."), an in-line comment
(e.g., "... We're the best \phf[I'm not sure about this.]
..."), and text removals (e.g., "... \phf*{remove me} ...").
New colors are assigned automatically to each commenter by
default, and the appearance of all comments is highly
customizable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfcc
%{_texmfdistdir}/tex/latex/phfcc
%doc %{_texmfdistdir}/doc/latex/phfcc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
