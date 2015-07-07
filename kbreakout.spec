Summary:	Breakout like game
Name:		kbreakout
Version:	15.04.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kbreakout/
Source:	    http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
Requires:	libkdegames-corebindings

%description
KBreakout is a Breakout-like game.

Its object is to destroy as many bricks as possible without losing the ball.

%files
%{_kde_bindir}/kbreakout
%{_kde_applicationsdir}/kbreakout.desktop
%{_kde_appsdir}/kbreakout
%{_kde_iconsdir}/hicolor/*/apps/kbreakout.png
%{_kde_docdir}/*/*/kbreakout

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build



