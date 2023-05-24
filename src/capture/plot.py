#!/usr/bin/env python

import rospy
import cv2 as cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Bool
from g_planner.msg import point,camera
from geometry_msgs.msg import Point,PoseStamped
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os
import math

class plotter:
  def __init__(self):
    self.eg = rospy.Subscriber("trajectory/global",point,self.plot_cb)

  def convert(self,waypoint):
    # point = np.empty((len(waypoint),3))
    point = []
    for i in range(len(waypoint)):
      x = waypoint[i].x
      y = waypoint[i].y
      z = waypoint[i].z

      point.append([x,y,z])

    point = np.stack(point)
    return point


  
  def plot_cb(self,msg):
    waypoint1 = msg.surface1
    waypoint2 = msg.surface2
    waypoint3 = msg.surface3
    waypoint4 = msg.surface4
    waypoint5 = msg.surface5

    cluster = [waypoint1,waypoint2,waypoint3,waypoint4,waypoint5]
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    waypoint1_np = self.convert(waypoint1)
    waypoint2_np = self.convert(waypoint2)
    waypoint3_np = self.convert(waypoint3)
    waypoint4_np = self.convert(waypoint4)
    waypoint5_np = self.convert(waypoint5)

    # print(waypoint1_np) # r x 3

    zdata = np.hstack([waypoint1_np[:,2],waypoint2_np[:,2],waypoint3_np[:,2],waypoint4_np[:,2],waypoint5_np[:,2]])
    ydata = np.hstack([waypoint1_np[:,1],waypoint2_np[:,1],waypoint3_np[:,1],waypoint4_np[:,1],waypoint5_np[:,1]])
    xdata = np.hstack([waypoint1_np[:,0],waypoint2_np[:,0],waypoint3_np[:,0],waypoint4_np[:,0],waypoint5_np[:,0]])

    print(xdata.shape, ydata.shape, zdata.shape)
    # ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

    for i in range(1, len(xdata)):
      ax.plot([xdata[i-1], xdata[i]], [ydata[i-1], ydata[i]],zs=[zdata[i-1], zdata[i]],color = 'black')

    plt.savefig('lawnmowercollapsed.png')


if __name__ == '__main__':
  plot = plotter()
  rospy.init_node('plot')
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")  