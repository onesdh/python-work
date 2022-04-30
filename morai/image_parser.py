from cv2 import COLOR_GRAY2BGR
import rospy
import cv2
import numpy as np
import os, rospkg


from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridgeError



class IMGParser :
    def __init__(self) :
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)

        self.img_bgr = None

        self.crop_pts = np.array(
            [[
                [0,180],
                [140,120],
                [180,120],
                [320,180]
            ]]
        )

        self.source_prop = np.float32([[0.01, 0.80],
        [0.5 - 0.14, 0.52],
        [0.5 + 0.14, 0.52],
        [1 - 0.01, 0.80]])  # 초인터 수직이 되도록 찾기

    def callback(self, msg) :
        try :
            np_arr = np.fromstring(msg.data, np.unit8)
            img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        except CvBridgeError as e :
            print(e)

        img_warp = warp_image(self.img_bgr, self.source_prop)
        img_concat = np.concatenate([self.img_bgr, img_warp], axis = 1)

        cv2.imshow("Image window", img_concat)
        cv2.waitKey(1)

        img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

        lower_wlane = np.array()  #대회에서 찾음 [(21,100,75), (25,255,255)], [(1,75,75), (9,225,225)]

        upper_wlane = np.array([30,60,255])

        img_wlane = cv2.inRange(img_hsv, lower_wlane, upper_wlane)
        img_wlane = cv2.cvtColor(img_wlane cv2.COLOR_GRAY2BGR)

        img_concat = np.concatenate([img_bgr, img_hsv], axis = 1)
        cv2.imshow("Image window", img_bgr)
        cv2.waitKey(1)

        self.mask = self.mask_roi(img_bgr)

        if len(self.mask.shape) == 3 :
            img_concat = np.concatenate([img_bgr, self.mask], axis = 1)

        else : img_concat = np.concatenate([img_bgr, cv2.cvtColor(self.mask, cv2.COLOR_GRAY2BGR)], axis = 1)

        cv2.imshow("Image window", img_concat)
        cv2.waitKey(1)

    def mask_roi(self, img) :

        h = img.shape[0]
        w = img.shape[1]

        if len(img.shape) == 3:
            c = img.shape[2]
            mask = np.zeros((h,w,c), dtype = np.unit8)

            mask_value = (255, 255, 255)

        else :
            mask = np.zeros((h, w), dtype = np.unit8)

            mask_value = (255)
            
        cv2.fillPoly(mask, self.crop_pts, mask_value)

        mask = cv2.birwise_and(mask, img)

        return mask

if __name__ == '__main__' :
    rospy.init_node('image_parser', annoymous = True)

    image_parser = IMGParser()

    rospy.spin()