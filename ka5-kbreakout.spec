%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kbreakout
Summary:	Kbreakout
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	30ba74c87fd27125118f1c7b78b8dfc5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBreakout is a Breakout-like game. Its object is to destroy as many
bricks as possible without losing the ball.

%description -l pl.UTF-8
KBreakout is grą typu Breakout. Celem gry jest zniszczenie tak dużo
cegieł jak to możliwe bez utraty piłki.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbreakout
%{_desktopdir}/org.kde.kbreakout.desktop
%{_iconsdir}/hicolor/128x128/apps/kbreakout.png
%{_iconsdir}/hicolor/16x16/apps/kbreakout.png
%{_iconsdir}/hicolor/22x22/apps/kbreakout.png
%{_iconsdir}/hicolor/32x32/apps/kbreakout.png
%{_iconsdir}/hicolor/48x48/apps/kbreakout.png
%{_iconsdir}/hicolor/64x64/apps/kbreakout.png
%{_iconsdir}/hicolor/scalable/apps/kbreakout.svg
%{_datadir}/kbreakout
%{_datadir}/metainfo/org.kde.kbreakout.appdata.xml
%{_datadir}/qlogging-categories5/kbreakout.categories
