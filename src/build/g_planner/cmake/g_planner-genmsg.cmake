# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "g_planner: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ig_planner:/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Imavros_msgs:/opt/ros/noetic/share/mavros_msgs/cmake/../msg;-Igeographic_msgs:/opt/ros/noetic/share/geographic_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Iuuid_msgs:/opt/ros/noetic/share/uuid_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(g_planner_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_custom_target(_g_planner_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "g_planner" "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" "mavros_msgs/MountControl:std_msgs/Header:geometry_msgs/Point"
)

get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_custom_target(_g_planner_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "g_planner" "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" "geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/mavros_msgs/cmake/../msg/MountControl.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/g_planner
)
_generate_msg_cpp(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/g_planner
)

### Generating Services

### Generating Module File
_generate_module_cpp(g_planner
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/g_planner
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(g_planner_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(g_planner_generate_messages g_planner_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_cpp _g_planner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_cpp _g_planner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(g_planner_gencpp)
add_dependencies(g_planner_gencpp g_planner_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS g_planner_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/mavros_msgs/cmake/../msg/MountControl.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/g_planner
)
_generate_msg_eus(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/g_planner
)

### Generating Services

### Generating Module File
_generate_module_eus(g_planner
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/g_planner
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(g_planner_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(g_planner_generate_messages g_planner_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_eus _g_planner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_eus _g_planner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(g_planner_geneus)
add_dependencies(g_planner_geneus g_planner_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS g_planner_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/mavros_msgs/cmake/../msg/MountControl.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/g_planner
)
_generate_msg_lisp(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/g_planner
)

### Generating Services

### Generating Module File
_generate_module_lisp(g_planner
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/g_planner
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(g_planner_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(g_planner_generate_messages g_planner_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_lisp _g_planner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_lisp _g_planner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(g_planner_genlisp)
add_dependencies(g_planner_genlisp g_planner_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS g_planner_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/mavros_msgs/cmake/../msg/MountControl.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/g_planner
)
_generate_msg_nodejs(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/g_planner
)

### Generating Services

### Generating Module File
_generate_module_nodejs(g_planner
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/g_planner
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(g_planner_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(g_planner_generate_messages g_planner_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_nodejs _g_planner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_nodejs _g_planner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(g_planner_gennodejs)
add_dependencies(g_planner_gennodejs g_planner_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS g_planner_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/mavros_msgs/cmake/../msg/MountControl.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner
)
_generate_msg_py(g_planner
  "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner
)

### Generating Services

### Generating Module File
_generate_module_py(g_planner
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(g_planner_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(g_planner_generate_messages g_planner_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/point.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_py _g_planner_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/impact4impact/Desktop/drone_ros1/src/g_planner/msg/camera.msg" NAME_WE)
add_dependencies(g_planner_generate_messages_py _g_planner_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(g_planner_genpy)
add_dependencies(g_planner_genpy g_planner_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS g_planner_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/g_planner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/g_planner
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(g_planner_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(g_planner_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET mavros_msgs_generate_messages_cpp)
  add_dependencies(g_planner_generate_messages_cpp mavros_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/g_planner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/g_planner
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(g_planner_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(g_planner_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET mavros_msgs_generate_messages_eus)
  add_dependencies(g_planner_generate_messages_eus mavros_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/g_planner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/g_planner
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(g_planner_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(g_planner_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET mavros_msgs_generate_messages_lisp)
  add_dependencies(g_planner_generate_messages_lisp mavros_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/g_planner)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/g_planner
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(g_planner_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(g_planner_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET mavros_msgs_generate_messages_nodejs)
  add_dependencies(g_planner_generate_messages_nodejs mavros_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/g_planner
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(g_planner_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(g_planner_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET mavros_msgs_generate_messages_py)
  add_dependencies(g_planner_generate_messages_py mavros_msgs_generate_messages_py)
endif()
