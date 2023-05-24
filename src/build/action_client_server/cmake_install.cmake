# Install script for directory: /home/impact4impact/Desktop/drone_ros1/src/action_client_server

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/msg/point.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/action" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Takeoff.action"
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Exploration.action"
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Waypoint_exploration.action"
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Trajectory.action"
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Trajectory_uav2.action"
    "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/action/Takeoff_1.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffAction.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TakeoffFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationAction.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/ExplorationFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationAction.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Waypoint_explorationFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryAction.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/TrajectoryFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2Action.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2ActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2ActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2ActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2Goal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2Result.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Trajectory_uav2Feedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/msg" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1Action.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1ActionGoal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1ActionResult.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1ActionFeedback.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1Goal.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1Result.msg"
    "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/action_client_server/msg/Takeoff_1Feedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/cmake" TYPE FILE FILES "/home/impact4impact/Desktop/drone_ros1/src/build/action_client_server/catkin_generated/installspace/action_client_server-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/impact4impact/Desktop/drone_ros1/src/build/devel/include/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/roseus/ros/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/common-lisp/ros/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/impact4impact/Desktop/drone_ros1/src/build/devel/share/gennodejs/ros/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/impact4impact/Desktop/drone_ros1/src/build/devel/lib/python3/dist-packages/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/impact4impact/Desktop/drone_ros1/src/build/devel/lib/python3/dist-packages/action_client_server")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/impact4impact/Desktop/drone_ros1/src/build/action_client_server/catkin_generated/installspace/action_client_server.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/cmake" TYPE FILE FILES "/home/impact4impact/Desktop/drone_ros1/src/build/action_client_server/catkin_generated/installspace/action_client_server-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server/cmake" TYPE FILE FILES
    "/home/impact4impact/Desktop/drone_ros1/src/build/action_client_server/catkin_generated/installspace/action_client_serverConfig.cmake"
    "/home/impact4impact/Desktop/drone_ros1/src/build/action_client_server/catkin_generated/installspace/action_client_serverConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/action_client_server" TYPE FILE FILES "/home/impact4impact/Desktop/drone_ros1/src/action_client_server/package.xml")
endif()

