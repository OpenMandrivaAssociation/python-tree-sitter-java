Name:		python-tree-sitter-java
Version:	0.23.5
Release:	1
Summary:	Tree-sitter java grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-java
Source0:	https://files.pythonhosted.org/packages/fa/dc/eb9c8f96304e5d8ae1663126d89967a622a80937ad2909903569ccb7ec8f/tree_sitter_java-0.23.5.tar.gz
# PyPI sdist omits src/tree_sitter/*.h
Source1:	tree-sitter-c-headers.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for java, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_java-0.23.5
tar -C src -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_java*
