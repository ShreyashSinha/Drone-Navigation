#!/usr/bin/env python

import rospy
import actionlib
from mavros_msgs.srv import CommandBool, SetMode , CommandBoolRequest,SetModeRequest,CommandHome,CommandTOL
from mavros_msgs.msg import State,ExtendedState
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped, Twist
from action_client_server.msg import *
from quadrotor_msgs.msg import PositionCommand
from mavros_msgs.msg import PositionTarget
from scipy.spatial.transform import Rotation
from mavros_msgs.msg import MountControl
import math

class Server:
    def __init__(self):
        self.server_action1 = actionlib.SimpleActionServer('takeoff', TakeoffAction, self.execute_action1, False)
        self.server_action2 = actionlib.SimpleActionServer('exploration', ExplorationAction, self.execute_action2, False)
        self.server_action3 = actionlib.SimpleActionServer('preliminary_exploration', TrajectoryAction, self.preliminary_exploration, False)
        self.server_action4 = actionlib.SimpleActionServer('exhaustive_exploration', TrajectoryAction, self.exhaustive_exploration, False)
        self.server_action1.start()
        self.server_action2.start()
        self.server_action3.start()
        self.server_action4.start()
                

        
        self.setpoint_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size=10)
        self.setvel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=10)
        self.local_p = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        self.gimbal_p = rospy.Publisher('/mavros/mount_control/command', MountControl, queue_size=10)
        # self.drone_p = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
        self.set_mode_client = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        self.arm_client = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        self.pose_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, callback=self.pose_callback)
        self.state_sub = rospy.Subscriber('/mavros/state', State, callback=self.state_callback)
        self.command_sub = rospy.Subscriber('/planning/pos_cmd', PositionCommand, callback=self.command_callback)

    def state_callback(self, msg):
        self.current_state = msg
        rospy.loginfo('Current mode: {}'.format(msg.mode))

    def pose_callback(self, msg):
        self.current_pose = msg

    def arm(self):
        rospy.loginfo('Arming')
        success = False
        while not success:
            req = CommandBoolRequest()
            req.value = True
            success = self.arm_client.call(req).success
            rospy.loginfo(success)
            rospy.sleep(0.1)

    def command_callback(self,msg):
        rospy.loginfo("Recieved Command")
        # point = PoseStamped()
        vel = Twist()
        vel.linear.x = msg.velocity.x
        vel.linear.y = msg.velocity.y
        vel.linear.z = msg.velocity.z        
        self.setvel_pub.publish(vel)

        # rot = Rotation.from_euler('xyz', [0, 0, msg.yaw], degrees=False)
        # rot_quat = rot.as_quat()
        # point.pose.position.x = msg.position.x
        # point.pose.position.y = msg.position.y
        # point.pose.position.z = msg.position.z
        # point.pose.orientation.x = rot_quat[0]
        # point.pose.orientation.y = rot_quat[1]
        # point.pose.orientation.z = rot_quat[2]
        # point.pose.orientation.w = rot_quat[3]

        # for i in range(10):
        #     self.setpoint_pub.publish(point)
        # isReached = False
        # while not isReached:
        #     self.setpoint_pub.publish(point)
        #     isReached = self.has_reached_desired_position(point)
        # for i in rang?e(10):


    


# SEE Why this was not workingggggggggggg
    # def set_mode(self, mode):
    #     rospy.loginfo('Setting mode: {}'.format(mode))
    #     success = False
    #     while not success:
    #         success = self.set_mode_client(custom_mode=mode).mode_sent
            
    #         rospy.sleep(0.1)

    
    def set_mode(self,mode):
        rospy.wait_for_service('/mavros/set_mode')
        try:
            flight_mode_service = rospy.ServiceProxy('/mavros/set_mode', SetMode)
            flight_mode_service(custom_mode=mode)
        except rospy.ServiceException as e:
            print("Service call failed: %s" % e)



    def dist_from_closest_lndng_stn(self):
        lndng_stn1=PoseStamped()
        lndng_stn1.pose.position.x=0
        lndng_stn1.pose.position.y=0
        lndng_stn1.pose.position.z=0
        lndng_stn2=PoseStamped()
        lndng_stn2.pose.position.x=0
        lndng_stn2.pose.position.y=54
        lndng_stn2.pose.position.z=0
        dist1= math.sqrt((self.current_pose.pose.position.x - lndng_stn1.pose.position.x) ** 2 + (self.current_pose.pose.position.y - lndng_stn1.pose.position.y) ** 2 + (self.current_pose.pose.position.z -lndng_stn1.pose.position.z ) ** 2)
        dist2= math.sqrt((self.current_pose.pose.position.x - lndng_stn2.pose.position.x) ** 2 + (self.current_pose.pose.position.y - lndng_stn2.pose.position.y) ** 2 + (self.current_pose.pose.position.z -lndng_stn2.pose.position.z ) ** 2)
        if dist1<=dist2:
            rospy.loginfo("Going to Landing Station1")
            return lndng_stn1
        else:
            rospy.loginfo("Going to Landing Station 2")
            return lndng_stn2
    


    def extended_state_callback(self,data):
        global landed
        if data.landed_state == ExtendedState.LANDED_STATE_ON_GROUND and not landed:
            rospy.loginfo('Drone has landed')
            landed = True
        elif data.landed_state != ExtendedState.LANDED_STATE_ON_GROUND and landed:
            rospy.loginfo('Drone is no longer landed')
        landed = False
    

    def has_reached_desired_position(self,desired_pose):
        x1 = self.current_pose.pose.position.x
        y1 = self.current_pose.pose.position.y
        z1 = self.current_pose.pose.position.z

        x2 = desired_pose.pose.position.x
        y2 = desired_pose.pose.position.y
        z2 = desired_pose.pose.position.z

        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        # rospy.loginfo(distance)
        if distance <= 3.0:
            return True
        else:
            return False
    
    def percentage_covered(self,total_pts,pts_covered):
        value=(pts_covered/total_pts)*100
        return value


    def execute_action1(self, goal):
        self.feedback = TakeoffFeedback()
        self.result = TakeoffResult()
        self.set_mode('AUTO.LOITER')
        self.arm()
        self.set_mode('AUTO.LOITER')
        self.set_mode('OFFBOARD')
        success = True
        goal_altitude = goal.altitude
        rate = rospy.Rate(10)
        while self.current_pose is None:
            rate.sleep()
        takeoff_altitude = goal_altitude

        pose=PoseStamped()
        pose.pose.position.x=self.current_pose.pose.position.x
        pose.pose.position.y=self.current_pose.pose.position.y
        pose.pose.position.z=takeoff_altitude
        while self.current_pose.pose.position.z < takeoff_altitude - 0.1:
            if self.server_action1.is_preempt_requested():
                
                self.server_action1.set_preempted()
                success = False
                break
            self.feedback.reached_altitude = False
            self.server_action1.publish_feedback(self.feedback)
            # self.local_p.publish(pose)

            
            for i in range(10):   
                if(rospy.is_shutdown()):
                    break
                self.setpoint_pub.publish(pose)
                # self.local_p.publish(pose)

            rate.sleep()
        # success=True
        # if success:
        #     rospy.loginfo('Takeoff succeeded')
        #     self.server.set_succeeded()
        if success:
            self.result.success = True
            rospy.loginfo('Takeoff succeeded')
            self.server_action1.set_succeeded(self.result)

    def execute_action2(self,goal):
        rospy.loginfo(type(goal))
        rate=rospy.Rate(10)
        lis_wp=[] #List of tuple of setpoints
        self.feedback = ExplorationFeedback()
        self.result = ExplorationResult()
        self.set_mode('AUTO.LOITER')
        self.arm()
        # self.set_mode('AUTO.LOITER')
        self.set_mode('OFFBOARD')
        self.feedback=ExplorationFeedback()
        success=True
        
        
        var=PoseStamped()
        var=goal.trgt_pose
        x1 = var.pose.position.x
        y1 = var.pose.position.y
        z1 = var.pose.position.z

        x2 = self.current_pose.pose.position.x
        y2 = self.current_pose.pose.position.y
        z2 = self.current_pose.pose.position.z

        dist = int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2))

        self.feedback.distance_left=dist
        self.server_action2.publish_feedback(self.feedback)
        while dist > 3:
            x2 = self.current_pose.pose.position.x
            y2 = self.current_pose.pose.position.y
            z2 = self.current_pose.pose.position.z
            if self.server_action2.is_preempt_requested():
                set_home_position = rospy.ServiceProxy('/mavros/cmd/set_home', CommandHome)

                home_pose = PoseStamped()
                
                response = set_home_position(0, 0, 0, home_pose)
                home_pose=self.dist_from_closest_lndng_stn()
                home_pose.pose.position.z=home_pose.pose.position.z 
                self.set_mode("RTL")
                # for i in range(50):
                #     self.setpoint_pub.publish(home_pose)
                rospy.Subscriber('/mavros/extended_state', ExtendedState, callback=self.extended_state_callback)
                self.server_action2.set_preempted()
                success = False
                break
            dist = int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2))
            self.feedback.distance_left = dist
            self.server_action2.publish_feedback(self.feedback)
            
            for i in range(50):   
                if(rospy.is_shutdown()):
                    break

                self.setpoint_pub.publish(var)
            rate.sleep()
        rospy.loginfo("HERE")
        if success==False:
            rospy.loginfo("Task was preempted")
        if success==True:
            self.result.success=True
            rospy.loginfo("Reached Destination")
            self.server_action2.set_succeeded(self.result)
    

    def preliminary_exploration(self,goal):
        print("Inside _Execute 3")
        lis_wp=goal.traj_points
        gimbal = goal.gimbal
        # self.set_mode('AUTO.LOITER')
        self.set_mode('OFFBOARD')
        self.arm()
        # self.set_mode('AUTO.LOITER')
        
        self.feedback=TrajectoryFeedback()
        self.result = TrajectoryResult()
        success=True
        l=0
        # k=goal.strtng_pt
        # print(k)

        
        for i in range(len(lis_wp)):
            print(len(lis_wp))
            self.set_mode('OFFBOARD')
            pose=PoseStamped()
            pose.pose.position.x=lis_wp[i].x
            pose.pose.position.y=lis_wp[i].y

            pose.pose.position.z=lis_wp[i].z
            
            # if self.server_action4.is_preempt_requested():
            #     set_home_position = rospy.ServiceProxy('/mavros/cmd/set_home', CommandHome)
            #     last_pose=lis_wp[k]
            #     home_pose = PoseStamped()
                
                
            #     home_pose=self.dist_from_closest_lndng_stn()
            #     home_pose.pose.position.z=home_pose.pose.position.z + 10
            #     for i in range(100):
            #         self.setpoint_pub.publish(home_pose)
            #         rate.sleep()
            #     # response = set_home_position(0, 0, 0, home_pose)
            #     rospy.wait_for_service('/mavros/cmd/land')

            #     # Create a service proxy for the command service
            #     land_service = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)

            #     # Call the service with the landing altitude (in meters)
            #     landing_altitude = 0.0 # Set to 0.0 to land on the current position
            #     landing_altitude = 0.0 # Set to 0.0 to land on the current position
            #     response = land_service(altitude=landing_altitude)
            #     # self.set_mode("RTL")
            #     self.result.no_points_covered = l 
            #     # rospy.Subscriber('/mavros/extended_state', ExtendedState, callback=self.extended_state_callback)
            #     self.server_action4.set_preempted(self.result)
            #     success = False
            #     break

            self.feedback.percentage = self.percentage_covered(len(lis_wp),l) 
            self.server_action4.publish_feedback(self.feedback)
            rate=rospy.Rate(20)
            self.gimbal_p.publish(gimbal)
            while not self.has_reached_desired_position(pose):   
                if(rospy.is_shutdown()):
                    break
                # rospy.loginfo("Publishing SetPoints")
                self.setpoint_pub.publish(pose)
                # self.local_p.publish(pose)

                rate.sleep()
            l+=1
            # rate=rospy.Rate(20)
            # while  not self.has_reached_desired_position(pose):
            #     # rospy.sleep(0.01)
            #     # rospy.loginfo("Waiting for drone to reach {}th waypoint.".format(l))
            #     pass
                
            # rospy.sleep(2)
            # rate.sleep()
            # rospy.loginfo("Drone reached {}th point".format(l))
        
        if success==False:
            self.result.surface_success=False
            
            rospy.loginfo("Task was preempted")
        if success==True:
            self.result.surface_success=True
            
            rospy.loginfo("Reached Destination")
            self.server_action4.set_succeeded(self.result)

        
    
    def exhaustive_exploration(self,goal):
        print("Inside _Execute 4")
        lis_wp=goal.traj_points
        gimbal = goal.gimbal
        # self.set_mode('AUTO.LOITER')
        self.set_mode('OFFBOARD')
        self.arm()
        # self.set_mode('AUTO.LOITER')
        
        self.feedback=TrajectoryFeedback()
        self.result = TrajectoryResult()
        success=True
        l=0
        # k=goal.strtng_pt
        # print(k)

        
        for i in range(len(lis_wp)):
            print(len(lis_wp))
            self.set_mode('OFFBOARD')
            pose=PoseStamped()
            pose.pose.position.x=lis_wp[i].x
            pose.pose.position.y=lis_wp[i].y
            pose.pose.position.z=lis_wp[i].z
            
            # if self.server_action4.is_preempt_requested():
            #     set_home_position = rospy.ServiceProxy('/mavros/cmd/set_home', CommandHome)
            #     last_pose=lis_wp[k]
            #     home_pose = PoseStamped()
                
                
            #     home_pose=self.dist_from_closest_lndng_stn()
            #     home_pose.pose.position.z=home_pose.pose.position.z + 10
            #     for i in range(100):
            #         self.setpoint_pub.publish(home_pose)
            #         rate.sleep()
            #     # response = set_home_position(0, 0, 0, home_pose)
            #     rospy.wait_for_service('/mavros/cmd/land')

            #     # Create a service proxy for the command service
            #     land_service = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)

            #     # Call the service with the landing altitude (in meters)
            #     landing_altitude = 0.0 # Set to 0.0 to land on the current position
            #     landing_altitude = 0.0 # Set to 0.0 to land on the current position
            #     response = land_service(altitude=landing_altitude)
            #     # self.set_mode("RTL")
            #     self.result.no_points_covered = l 
            #     # rospy.Subscriber('/mavros/extended_state', ExtendedState, callback=self.extended_state_callback)
            #     self.server_action4.set_preempted(self.result)
            #     success = False
            #     break

            self.feedback.percentage = self.percentage_covered(len(lis_wp),l) 
            self.server_action4.publish_feedback(self.feedback)
            rate=rospy.Rate(20)
            self.gimbal_p.publish(gimbal)
            while not self.has_reached_desired_position(pose):   
                if(rospy.is_shutdown()):
                    break
                # rospy.loginfo("Publishing SetPoints")
                # self.setpoint_pub.publish(pose)
                self.local_p.publish(pose)

                rate.sleep()
            l+=1
            # rate=rospy.Rate(20)
            # while  not self.has_reached_desired_position(pose):
            #     # rospy.sleep(0.01)
            #     # rospy.loginfo("Waiting for drone to reach {}th waypoint.".format(l))
            #     pass
                
            # rospy.sleep(2)
            # rate.sleep()
            # rospy.loginfo("Drone reached {}th point".format(l))
        
        if success==False:
            self.result.surface_success=False
            
            rospy.loginfo("Task was preempted")
        if success==True:
            self.result.surface_success=True
            
            rospy.loginfo("Reached Destination")
            self.server_action4.set_succeeded(self.result)



if __name__ == '__main__':
    rospy.init_node('takeoff_server')
    server = Server()
    rospy.spin()

