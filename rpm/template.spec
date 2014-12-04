Name:           ros-hydro-nao-description
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS nao_description package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-message-filters
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-urdf
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-urdf
BuildRequires:  ros-hydro-xacro

%description
Description of the Nao robot model that can be used with robot_state_publisher
to display the robot's state of joint angles.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Dec 04 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.1-0
- Autogenerated by Bloom

* Fri Nov 07 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.0-0
- Autogenerated by Bloom

