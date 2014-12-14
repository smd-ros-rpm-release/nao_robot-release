Name:           ros-indigo-nao-pose
Version:        0.5.3
Release:        0%{?dist}
Summary:        ROS nao_pose package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nao_pose
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-naoqi-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-catkin

%description
This package contains nodes for managing Nao's poses.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 14 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.3-0
- Autogenerated by Bloom

* Thu Dec 04 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.1-0
- Autogenerated by Bloom

* Fri Nov 07 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.0-0
- Autogenerated by Bloom

