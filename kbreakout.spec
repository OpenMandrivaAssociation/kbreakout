Summary:	Breakout like game
Name:		kbreakout
Version:	16.04.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kbreakout/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)

Requires:	libkdegames-corebindings

%description
KBreakout is a Breakout-like game.

Its object is to destroy as many bricks as possible without losing the ball.

%files
%doc %{_docdir}/*/*/kbreakout                                                                          
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



