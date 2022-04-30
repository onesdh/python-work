import rospy
import rospkg
from math import cos, sin, pi, sqrt, pow, atan2
from geometry_msgs.msg import Point ,PoseWidthCovarianceStamped
from nav_msgs.msg import Odometry, Path
from marai_msgs.msg import CtrlCmd
import numpy as np
import tf
from tf.transformations import euler_from_quaternion,quaternion_fronm_euler

class pidControl :
    def __init__(self) :
        self.p_gain = 1.0
        self.i_gain =0.0
        self.d_gain = 0.4
        self.prev_error = 0
        self.i_control = 0
        self.controlTime = 0.0333

    def pid(self, target_vel, current_vel) :
        error = target_vel-current_vel

        p_control = self.p_gain*error
        self.i_control += self.i_gain*error*self.controlTime
        d_control = self.d_gain*(error-self.prev_error)/self.controlTime

        output = p_control+self.i_control + d_control
        self.prev_error = error
        return output


class pure_pursuit :
    def __init__(self):
        rospy. init_node('pure_pursuit', anonymous=True)
        rospy.Subscriber("local_path", Path, self.path_callback)
        rospy.Subscriber("odom", Odometry, self .odom_callback)
        rospy.Subscriber("/target_vel", Float64, self.target_vel_callback)
        rospy.Subscriber("/", Float64, self.status_callback)    # odom으ㅡ로 current_vel 구해야함
        self.ctrl_cmd_pub = rospy.Publisher('ctrl_cmd' ,CtrlCmd, queue_size=1)
        self.ctrl_cmd_esg=CtrlCmd()
        self.ctrl_cmd_msg.longlCadType=1

        self.is_path=False
        self.is_odom=False
        self.is_current_vel = False   # pid 추가
        self.target_vel = 0.0    # pid 추가
        self.forward_point=Point()  
        self.current_position = Point()
        self.is_look_forward_point=False
        self.vehicle_length = 1
        self.lfd = 3
        current_vel = sqrt(vel_x^2 + vel_y^2 + vel_z^2) 

        self.pid_conroller = pidControl()     # pid 추가


        rate = rospy.Rate(30) 
        while not rospy.is_shutdowm():
            if self.is_path == True and self.is_odom == True :
                
                vehicle_position = self.current_position
                self.is_look_forward_point= False

                translation = [vehicle_position.x, vehicle_position.y]
                
                t=np.array([
                    [cos(self.vehicle_yaw), -sin(self.vehicle_yaw) , translation(0)],
                    [sin(self.vehicle_yaw) ,cos(self.vehicle_yaw) ,translation(1)],
                    [0, 0, 1]])

                det_t = np.array ([
                    [t[0][0], t[1][0], -(t[0][0]*translation[0]+t[1][0]*translation[1])],
                    [t[0][1], t[1][1], -(t[0][1]*translation[0]+t[1][1]*translation[1])],
                    [0,0,1]
                ])

                for num,i in enumerate(self.path.poses) :
                    path_point=i .pose.position
                    
                    gobal_path_point = [path_point.x, path_point.y, 1]
                    local_path_point = det_t.dot(global_path_point)
                    if local_path_point[0] > 0 :

                        dis=sqrt(pow(local_path_point[0],2)*pow(local_path_point[1] ,2))
                        if dis >= self. lfd :
                            self.forward_point = path_point
                            self.is_look_forward_point = True
                            break
                theta = atan2(local_path_point[1], local_path_point[0])



                if self.is_look_forward_point :
                    self.ctrl_cmd_msg.steering = atan2((2*self.vehicle_length*sin(theta)),self.lfd)
                    output = self.pid_controller.pid(self.target_vel,self.current_vel)
                    print(self.ctrl_cmd_msg.steering)
                    if output > 0.0:
                        self.ctrl_cmd_msg.accel = output
                        self.crtl_cmd_msg.brake = 0
                    else :
                        self.ctrl_cmd_msg.accel = 0
                        self.crtl_cmd_msg.brake = output
                    print(self.ctrl_cmd_mag.steering)
                else :
                    print("no found forward point")
                    self.ctrl_cmd_msg.steering = 0.0
                    self.ctrl_cmd_msg.velocity = 0.0
                    self.ctrl_cmd_msg.accel = 0.0
                    self.ctrl_cmd_msg.brake = 1.0
                self.ctrl_cmd_pub.publish(self.ctrl_cmd_msg)
            rate.sleep()


    def path_callback(self ,msg):
        self.is_path = True
        self.path = msg

    def odom_callback(self ,msg):
        self.is_odom = True
        odom_quaternion=(msg.pose.pose.orientation.x,msg.pose.pose.orientation.y, msg.pose.pose.orientation.w )
        _,_,self.vehicle_yaw = euler_from_quaternion(odom_quaternion)
        self.current_position.x = msg.pose.pose.position.x
        self.current_position.y = msg.pose.pose.position.y

if __name__ == '__main__' :

    try:

        test_track = pure_pursuit()

    except rospy.ROSInterruptException :
        pass