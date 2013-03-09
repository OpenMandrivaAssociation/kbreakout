Name:		kbreakout
Version:	4.10.1
Release:	1
Epoch:		1
Summary:	Breakout like game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kbreakout/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

