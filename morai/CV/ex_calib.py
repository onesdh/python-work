#!/usr/bin/env python

import rospy
import numpy as np
import cv2
import math
import time
import rospkg
import os
import json
from sensor_msgs.msg import PointCloud2, CompressedImage
import sensor_msgs.point_cloud2 as pc2

params_lidar = {
    "X":1,#meter
    "Y":0,
    "Z":1.80,
    "YAW":0, #deg
    "PITCH": 0,
    "ROLL":0
}
params_cam={
    "WIDTH":6000,
    "HEIGHT":480,
    "FOV":90,
    "X":1.00,
    "Y":0,
    "Z":1.50,
    "YAW":0,
    "PITCH":5.0,
    "ROLL":0
}

def translationMtx(x, y, z):

    M = np.array([[1,           0,              0,      x],
                  [0,           1,              0,      y],
                  [0,           0,              1,      z],
                  [0,           0,              0,      1],
                  ])

    return M

def rotationMtx(yaw,pitch,roll):
    R_x =np.array([[1,          0,              0,      0],
                   [0,  math.cos(roll),-math.sin(roll), 0],
                   [0,  math.sin(roll), math.cos(roll), 0],
                   [0,          0,              0,      1],
                   ])
    R_y =np.array([[math.cos(pitch),    0,      math.sin(pitch),    0],
                   [0,1,0,0],
                   [-math.sin(pitch),0,math.cos(pitch),0],
                   [0,0,0,1],
                   ])
    R_z =np.array([[math.cos(yaw),-math.sin(yaw),0,0],
                   [math.sin(yaw),math.cos(yaw),0,0],
                   [0,0,1,0],
                   [0,0,0,1],
                   ])
    R=np.matmul(R_x,np.matmul(R_y,R_z))

    return R

def transformMTX_lidar2cam(params_lidar,params_cam):

    #Relative position of lidar w.r.t cam
    lidar_pos=[params_lidar.get(i) for i in (["X","Y","Z"])]
    cam_pos=[params_cam.get(i)for i in(["X","Y","Z"])]

    x_rel=cam_pos[0]-lidar_pos[0]
    y_rel=cam_pos[1]-lidar_pos[1]
    z_rel=cam_pos[2]-lidar_pos[2]

    R_T=np.matmul(translationMtx(x_rel,y_rel,z_rel),rotationMtx(np.deg2rad(-90.),0.,0.))
    R_T=np.matmul(R_T, rotationMtx(0,0.,np.deg2rad(-90.)))

    R_T=np.linalg.inv(R_T)

    return R_T

def project2img_mtx(params_cam):

    #focal lengths
    fc_x = params_cam["HEIGHT"]/(2*np.tan(np.deg2rad(params_cam["FOV"]/2)))
    fc_y = params_cam["HEIGHT"]/(2*np.tan(np.deg2rad(params_cam["FOV"]/2)))

    #the center of image
    cx=params_cam["WIDTH"]/2
    cy=params_cam["HEIGHT"]/2

    #transformation matrix from 3D to 2D
    R_f = np.array([[fc_x,0,cx],
                    [0,fc_y,cy]])

    return R_f


def draw_pts_img(img,xi,yi):
    point_np=img

    #Left Lane
    for ctr in zip(xi,yi):
        point_np=cv2.circle(point_np,ctr,2,(255,0,0),-1)

    return point_np

class LIDAR2CAMTransform:
    def __init__(self,params_cam,params_lidar):
        
        self.width=params_cam["WIDTH"]
        self.height=params_cam["HEIGHT"]
        

        self.RT = transformMTX_lidar2cam(params_lidar,params_cam)

        self.proj_mtx = project2img_mtx(params_cam)

    def transform_lidar2cam(self, xyz_p):
        xyz_c =np.matmul(np.concatenate([xyz_p, np.ones((xyz_p.shape[0],1))],axis=1),self.RT.T)

        return xyz_c

    def project_pts2img(self,xyz_c,crop=True):

        xyz_c=xyz_c.T

        xc,yc,zc=xyz_c[0,:].reshape([1,-1]),xyz_c[1,:].reshape([1,-1]),xyz_c[2,:].reshape([1,-1])

        xn,yn=xc/(zc+0.0001),yc/(zc+0.0001)

        xyi=np.matmul(self.proj_mtx,np.concatenate([xn,yn,np.ones_like(xn)],axis=0))

        xyi=xyi[0:2,:].T

        if crop:
            xyi=self.crop_pts(xyi)
        else:
            pass

        return xyi

    def crop_pts(self,xyi):
        xyi=xyi[np.logical_and(xyi[:,0]>=0,xyi[:,0]<self.width), :]
        xyi=xyi[np.logical_and(xyi[:,1]>=0,xyi[:,1]<self.height),:]

        return xyi
