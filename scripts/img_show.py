#!/usr/bin/env python
#coding: utf-8
import rospy
import cv2
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def img_cb(msg):
    try:
        rospy.loginfo("Subscribed Image Topic !")
        cv_img = CvBridge().imgmsg_to_cv2(msg, "bgr8")
        """
        何らかの処理
        """
        cv2.imshow("window", cv_img)
        cv2.waitKey(1)


    except CvBridgeError, e:
        rospy.logerror("Failed to Subscribe Image Topic")

def main():
    rospy.init_node("img_subscriber", anonymous=True)

    img_topic_name = "/usb_cam/image_raw"

    rospy.Subscriber(img_topic_name, Image, img_cb)
    rospy.spin()

if __name__ == "__main__":
    main()
