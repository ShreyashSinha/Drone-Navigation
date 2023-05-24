#!/usr/bin/env python

import rospy
import actionlib
from action_client_server.msg import *
from geometry_msgs.msg import PoseStamped
import datetime
from std_msgs.msg import Bool
from g_planner.msg import point




'''Full implementation of resuming from the last location when it rained for 1 drone
Work with server_2'''
raining_flag=False
def Rain_cb(msg):
    global raining_flag
    raining_flag=False
    if msg.data==True:
        raining_flag=True
    if msg.data==False:
        raining_flag=False
        
def feedback_callback_action1(feedback):
    # process feedback here
    rospy.loginfo(feedback)
    pass

def FeedBack_Callback(feedback):
    rospy.loginfo(feedback)
    pass

def Waypoint_exploration_FeedBack_Callback(feedback):
    rospy.loginfo(feedback)
    pass

def Trajectory_feedback(feedback):
    rospy.loginfo(feedback)

send_traj=False

def traj_cb(msg):
    global send_traj

    print("Inside Callback")
    global list_pts
    print(type(msg))
    list_pts_1=msg.surface1
    list_pts_2=msg.surface2
    list_pts_3=msg.surface3
    list_pts_4=msg.surface4
    list_pts_5=msg.surface5
    gimbal_list = msg.gimbal
    lst=[list_pts_1,list_pts_2,list_pts_3,list_pts_4,list_pts_5]
    # list(list_pts)
    print("Points Received")
    i = 0

    for wp in lst:
        exhaustive_trajectory(wp,gimbal_list[i])
        i += 1

    # send_traj=True

def traj_preliminary_cb(msg):
    global send_traj
    print("Inside Preliminary Callback")
    global list_pts
    list_pts_1=msg.surface1
    gimbal_list = msg.gimbal
    print("Points Received")        
    preliminary_exploration_client(list_pts_1,gimbal_list[0])
    # send_traj=True


def takeoff_client():
    client = actionlib.SimpleActionClient('takeoff', TakeoffAction)
    rospy.loginfo("Takeoff")
    client.wait_for_server()
    rate=rospy.Rate(1)
    goal = TakeoffGoal()
    goal.altitude = 14.0   # Set goal altitude to 5 meters

    client.send_goal(goal,feedback_cb=feedback_callback_action1)

    while not rospy.is_shutdown():
        state = client.get_state()
        
        
        rospy.loginfo("Current State: {}".format(state))
        if state == actionlib.GoalStatus.ACTIVE:
            rospy.loginfo("Takeoff is in progress...")
        elif state == actionlib.GoalStatus.SUCCEEDED:
            rospy.loginfo("Takeoff succeeded!")
            break
        elif state == actionlib.GoalStatus.PREEMPTED:
            rospy.loginfo("Takeoff was preempted!")
            break
        elif state == actionlib.GoalStatus.ABORTED:
            rospy.loginfo("Takeoff aborted!")
            break
        
        rate.sleep()
    
    result = client.get_result()
    
    rospy.loginfo(result)
    return result
    


def exploration_client():
    client = actionlib.SimpleActionClient('exploration', ExplorationAction)
    client.wait_for_server()
    rate=rospy.Rate(1)
    goal=ExplorationGoal()
    
    goal.trgt_pose.pose.position.x=20
    goal.trgt_pose.pose.position.y=20
    goal.trgt_pose.pose.position.z=5
    client.send_goal(goal,feedback_cb=FeedBack_Callback)
    while not rospy.is_shutdown():
        state = client.get_state()
        if raining_flag==True:
            client.cancel_all_goals()
            
        
        
        rospy.loginfo("Current State: {}".format(state))
        if state == actionlib.GoalStatus.ACTIVE:
            rospy.loginfo("Moving Towards target position ....")
        elif state == actionlib.GoalStatus.SUCCEEDED:
            rospy.loginfo("Reached Target Position.....")
            break
        elif state == actionlib.GoalStatus.PREEMPTED:
            rospy.loginfo("Exploration task Preempted!!!!")
            break
        elif state == actionlib.GoalStatus.ABORTED:
            rospy.loginfo("Exploration Task aborted!!!!")
            break
        
        rate.sleep()
    result=client.get_result()
    rospy.loginfo(result)

def preliminary_exploration_client(preliminary_pts,gimbal):
    client = actionlib.SimpleActionClient('preliminary_exploration', TrajectoryAction)
    client.wait_for_server()
    rate=rospy.Rate(1)
    goal=TrajectoryGoal()
    goal.traj_points= preliminary_pts
    goal.gimbal = gimbal
    k=0
    surface_success=False
    while not surface_success:
        if raining_flag==True:
            pass
        if raining_flag==False:
            goal.starting_point=k
            client.send_goal(goal,feedback_cb=Trajectory_feedback)

            while not rospy.is_shutdown():
                state = client.get_state()
                rospy.loginfo(raining_flag)
                if raining_flag==True:
                    # rospy.loginfo(raining_flag)
                    client.cancel_goal()
                    
                
                
                rospy.loginfo("Current State: {}".format(state))
                if state == actionlib.GoalStatus.ACTIVE:
                    rospy.loginfo("Moving Towards target position ....")
                elif state == actionlib.GoalStatus.SUCCEEDED:
                    rospy.loginfo("Reached Target Position.....")
                    break
                elif state == actionlib.GoalStatus.PREEMPTED:
                    rospy.loginfo("Exploration task Preempted!!!!")
                    break
                elif state == actionlib.GoalStatus.ABORTED:
                    rospy.loginfo("Exploration Task aborted!!!!")
                    break
                rate.sleep()
            
            result=client.get_result()
        surface_success=result.surface_success
        k=result.points_covered    


def exhaustive_trajectory(list_pts,gimbal):
    client = actionlib.SimpleActionClient('exhaustive_exploration', TrajectoryAction)
    client.wait_for_server()
    rate=rospy.Rate(1)
    goal=TrajectoryGoal()
    goal.traj_points=list_pts
    goal.gimbal = gimbal
    k=0
    surface_success=False
    while not surface_success:
        if raining_flag==True:
            pass
        if raining_flag==False:
            goal.starting_point=k
            client.send_goal(goal,feedback_cb=Trajectory_feedback)

            while not rospy.is_shutdown():
                state = client.get_state()
                rospy.loginfo(raining_flag)
                if raining_flag==True:
                    # rospy.loginfo(raining_flag)
                    client.cancel_goal()
                    
                
                
                rospy.loginfo("Current State: {}".format(state))
                if state == actionlib.GoalStatus.ACTIVE:
                    rospy.loginfo("Moving Towards target position ....")
                elif state == actionlib.GoalStatus.SUCCEEDED:
                    rospy.loginfo("Reached Target Position.....")
                    break
                elif state == actionlib.GoalStatus.PREEMPTED:
                    rospy.loginfo("Exploration task Preempted!!!!")
                    break
                elif state == actionlib.GoalStatus.ABORTED:
                    rospy.loginfo("Exploration Task aborted!!!!")
                    break
                rate.sleep()
            
            result=client.get_result()
        surface_success=result.surface_success
        k=result.points_covered    
    
        
    


    
    


if __name__ == '__main__':
    rospy.init_node('takeoff_client')
    #Subscribed to raining topic for now to detect the rain
    rospy.Subscriber('rain',Bool,callback=Rain_cb)
    rospy.Subscriber('trajectory/global',point,queue_size=1,callback=traj_cb)
    rospy.Subscriber('trajectory/preliminary',point,queue_size=1,callback=traj_preliminary_cb)
    surf_pub=rospy.Publisher('surface_feedback',Bool,queue_size=1)
    rospy.loginfo("Client Started")
    takeoff_client()
    
    rospy.spin()
    
    
    
        
    

