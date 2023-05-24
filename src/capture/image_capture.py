#!/usr/bin/env python

import rospy
import cv2 as cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Bool
from g_planner.msg import camera
from geometry_msgs.msg import Point,PoseStamped
import os
import math

path = '/home/impact4impact/Desktop/drone_ros1/src/Images'

class image_converter:
  def __init__(self):
    self.image_no = 0
    self.bridge = CvBridge()
    self.current_pose = PoseStamped()
    self.feedback = True
    self.image_fb = rospy.Subscriber("trajectory/camera",camera,self.image_cb)
    self.pose = rospy.Subscriber("mavros/local_position/pose",PoseStamped,self.pose_cb)
    self.cam_fb=rospy.Publisher("camera_feedback",Bool,queue_size=1)
    # self.depth_sub = rospy.Subscriber("/realsense/camera/depth/image_raw",Image,self.callback)

  def pose_cb(self,msg):
    self.current_pose = msg

  def hasReached(self,desired_pose):
    x_start = self.current_pose.pose.position.x
    y_start = self.current_pose.pose.position.y
    z_start = self.current_pose.pose.position.z

    x_goal = desired_pose.pose.position.x
    y_goal = desired_pose.pose.position.y
    z_goal = desired_pose.pose.position.z

    distance = math.sqrt((x_start - x_goal) ** 2 + (y_start - y_goal) ** 2 + (z_start - z_goal) ** 2)
    if (distance <= 1.0):
      return True
    else:
      False

  
  def image_cb(self,msg):
    rospy.loginfo("recieved surface")
    points = msg.camera_waypoints
    goal = PoseStamped()
    # rate = rospy.Rate(0.25)
    for i in range(len(points)):
      goal.pose.position.x = points[i].x
      goal.pose.position.y = points[i].y
      goal.pose.position.z = points[i].z
      while(not self.hasReached(goal)):
        rospy.loginfo("not reached")
        # rate.sleep()
      else:
        rospy.loginfo("reached target")
        self.color_sub = rospy.Subscriber("typhoon_h480/camera/rgb/image_raw",Image,self.callback)

    self.feedback = True
    self.cam_fb.publish(self.feedback)
    self.feedback = False

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except:
      cv_image = self.bridge.imgmsg_to_cv2(data)
	  # print(type(cv_image))
    # print(cv_image) 
    cv2.imwrite(os.path.join(path,"image_" + str(self.image_no) + ".jpg"), cv_image)
    self.image_no += 1
    

if __name__ == '__main__':
  ic = image_converter()
  rospy.init_node('image_capture')
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")