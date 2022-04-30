from cv2 import COLOR_GRAY2BGR, getPerspectiveTransform, warpPerspective
import rospy
import cv2
import numpy as np
import os, rospkg

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridgeError

def warp_image(img, source_prop) :
    image_size = (img.shape[1], img.shape[0])

    x = img.shape[1]
    y = img.shape[0]

    destination_points = np.float([
        [0,y],
        [0,0],
        [x,0],
        [x,y]
    ])

    source_points = source_prop * np.float32([[x,y]] * 4)
    perspective_transform = cv2.getPerspectiveTransform(source_points, destination_points)

    warped_img = cv2.warpPerspective(img, perspective_transform, image_size, flags = cv2.INTER_LINEAR)

    return warped_img