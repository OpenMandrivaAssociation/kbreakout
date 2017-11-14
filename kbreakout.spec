Summary:	Breakout like game
Name:		kbreakout
Version:	17.08.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kbreakout/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

Requires:	libkdegames-corebindings

%description
KBreakout is a Breakout-like game.

Its object is to destroy as many bricks as possible without losing the ball.

%files -f %{name}.lang
%{_bindir}/kbreakout                                                                                   
%{_datadir}/applications/org.kde.kbreakout.desktop                                                     
%{_datadir}/kxmlgui5/kbreakout/kbreakoutui.rc                                                          
%{_datadir}/kbreakout                                                                                  
%{_iconsdir}/hicolor/*/apps/kbreakout.png     

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
