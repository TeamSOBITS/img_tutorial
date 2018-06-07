#!/usr/bin/env python
#coding: utf-8
import rospy
import cv2
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def img_cb(msg):
    try:
        cv_img = CvBridge().imgmsg_to_cv2(msg, "bgr8")

        #cascadeのパスの指定
        face_cascade_path = "/home/rg26/opencv/data/haarcascades/haarcascade_frontalface_alt.xml"

        #分類器の作成
        face_classify = cv2.CascadeClassifier(face_cascade_path)

        #画像をグレースケールに変換
        gray_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

        line_color = (0, 255, 0)

        # 顔の検出
        faces = face_classify.detectMultiScale(gray_img)

        if len(faces) == 0:
            rospy.logwarn("no faces")

        else:
            rospy.loginfo(str(len(faces)) + " faces")
            for (x, y, w, h) in faces:
                #検出した顔を矩形で囲む
                cv2.rectangle(cv_img, (x, y), (x+w, y+h), line_color, 2)

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
