import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import message_filters
import os
import sys
# fps_ratio = 5
fps_ratio = int(sys.argv[1])

cvb = CvBridge()
i = 0


def imnormalize(xmax, image):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : image:image data.
    : return: Numpy array of normalize data
    """
    xmin = 0
    a = 0
    b = 255

    return ((np.array(image, dtype=np.float32) - xmin) * (b - a)) / (xmax - xmin)


def callback(image, depth):
    global i
    print("Image Received")
    cv_image = cvb.imgmsg_to_cv2(image, "bgr8")
    cv_depth = cvb.imgmsg_to_cv2(depth, depth.encoding)
    cv_depth_normal = np.array(imnormalize(
        np.max(cv_depth), cv_depth), dtype=np.uint8)
    if i % fps_ratio == 0:
        cv2.imwrite("./rgb/frame"+str(int(i/fps_ratio))+".jpg", cv_image)
        # cv2.imwrite("./depth/dframe"+str(int(i/fps_ratio))+".jpg", cv_depth_normal)
        print(str(int(i/fps_ratio)) + " Image(s) Found")
    i += 1
    # Solve all of perception here...


def image_callback(image):
    global i
    #print("Image Received")
    cv_image = cvb.imgmsg_to_cv2(image, "bgr8")
    #cv_image_cropped = cv_image_raw[0:400,0:640]
    #cv_image = cv2.rotate(cv_image_cropped, cv2.ROTATE_180)
    if i % fps_ratio == 0:
        cv2.imwrite("./rgb1/frame"+str(int(i/fps_ratio))+".jpg", cv_image)
        # cv2.imwrite("./depth/dframe"+str(int(i/fps_ratio))+".jpg", cv_depth_normal)
        print(str(int(i/fps_ratio)) + " Image(s) Found")
    i += 1


if __name__ == '__main__':
    rospy.init_node("GrabRGBD")
    rospy.loginfo("Running RGB-D Grabber")

    path = "./"  # Default path
    if not os.path.exists(path + "depth"):
        os.makedirs(path + "depth")
    if not os.path.exists(path + "rgb1"):
        os.makedirs(path + "rgb1")

    image_subs = rospy.Subscriber(
        'typhoon_h480/camera/rgb/image_raw', Image, callback=image_callback)
    # image_sub = message_filters.Subscriber(
    #     '/uav1/camera/color/image_raw', Image)
    # depth_sub = message_filters.Subscriber(
    #     '/uav1/camera/depth/image_rect_raw', Image)

    # ts = message_filters.ApproximateTimeSynchronizer(
    #     [image_sub, depth_sub], 1, 1)
    # ts.registerCallback(callback)
    rospy.spin()
