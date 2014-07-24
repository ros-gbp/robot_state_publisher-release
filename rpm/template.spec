Name:           ros-hydro-robot-state-publisher
Version:        1.9.11
Release:        0%{?dist}
Summary:        ROS robot_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-hydro-catkin
Requires:       ros-hydro-kdl-parser
Requires:       ros-hydro-orocos-kdl >= 1.3.0
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rostime
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf-conversions
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-kdl-parser
BuildRequires:  ros-hydro-orocos-kdl >= 1.3.0
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostime
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf-conversions

%description
This package allows you to publish the state of a robot to tf. Once the state
gets published, it is available to all components in the system that also use
tf. The package takes the joint angles of the robot as input and publishes the
3D poses of the robot links, using a kinematic tree model of the robot. The
package can both be used as a library and as a ROS node. This package has been
well tested and the code is stable. No major changes are planned in the near
future

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Jul 24 2014 Ioan Sucan <isucan@willowgarage.com> - 1.9.11-0
- Autogenerated by Bloom

