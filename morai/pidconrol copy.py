class pidControl :
    def __init__(self) :
        self.p_gain = 1.0 # 
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
        rospy.Subscriber("/target_vel", Float64, self.target_vel_callback)
        rospy.Subscriber("/Ego_topic", Float64, self.status_callback)


        self.ctrl_cmd_msg.longlCadType=1

        self.is_current_vel = False
        self.target_vel = 0.0



        self.pid_conroller = pidControl()

        if self.is_look_forward_point :
            self.ctrl_cmd_msg.steering = atan2((2*self.vehicle_length*sin(theta)),self.lfd)
            output = self.pid_controller.pid(self.target_vel,self.current_vel)
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
            self.ctrl_cmd_msg.accel = 0.0
            self.ctrl_cmd_msg.brake = 1.0

        self.ctrl_cmd_pub.publish(self.ctrl_cmd_msg)