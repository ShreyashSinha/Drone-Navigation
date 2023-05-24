#include <iostream>
#include <bits/stdc++.h>
#include "lawnmow.h"
#include "calibration.h"
#include <ros/ros.h>
#include "g_planner/point.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/PoseStamped.h"
#include <std_msgs/Bool.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include <mavros_msgs/MountControl.h>
#include <math.h>

using namespace std;

g_planner::point trajectory;
vector<vector<double>> waypoints;
float path_length;
ros::Publisher waypoint_pub;
ros::Publisher setpoint_pub;
ros::ServiceClient arming_client;
ros::ServiceClient set_mode_client;
ros::Subscriber state_sub;
ros::Subscriber pose_sub;

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

geometry_msgs::PoseStamped current_pose;
void pose_cb(const geometry_msgs::PoseStamped::ConstPtr& msg){
    current_pose = *msg;
}

void display(vector<vector<double>> waypoint){
    for (auto& x: waypoint){
        for (auto& y: x){
            cout<<y<<" ";
        }
        cout<<"\n";
    }
}

void arm(){
    ROS_INFO("ARMING");
    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;
    if (arming_client.call(arm_cmd) && arm_cmd.response.success){
        ROS_INFO("Vehicle armed");
    }
}

void setmode(){
    ROS_INFO("SETTING_MODE TO OFFBOARD");
    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";
    if( set_mode_client.call(offb_set_mode) && offb_set_mode.response.mode_sent){
        ROS_INFO("Offboard enabled");
    }
}

void takeoff(){
    geometry_msgs::PoseStamped pose;
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 10;
    ros::Rate rate(20);

    setmode();
    arm();
    bool Reached = false;
    while (!Reached){
        setpoint_pub.publish(pose);
        if (abs(pose.pose.position.z - current_pose.pose.position.z) < 1.0){
            Reached = true;
            ROS_INFO("REACHED ALTITUDE");
        }
        ros::spinOnce();
        rate.sleep();
    }
}

bool hasReached(geometry_msgs::PoseStamped start, geometry_msgs::PoseStamped goal){
    double x = start.pose.position.x - goal.pose.position.x; 
	double y = start.pose.position.y - goal.pose.position.y;
    double z = start.pose.position.z - goal.pose.position.z;
	double dist;

	dist = pow(x, 2) + pow(y, 2) + pow(z,2);       //calculating Euclidean distance
	dist = sqrt(dist);                  

	return dist <= 1.0;
}
void publish(){
    takeoff();
    ros::Rate rate(20);
    geometry_msgs::PoseStamped point;
    for (int i = 0; i < waypoints.size(); i++){
        point.pose.position.x = waypoints[i][0];
        point.pose.position.y = waypoints[i][1];
        point.pose.position.z = waypoints[i][2];
        while (!hasReached(current_pose,point)){
            setpoint_pub.publish(point);
            ros::spinOnce();
            rate.sleep();
        }
    }
}
 
int main(int argc, char **argv){

    ros::init(argc, argv, "preliminary");
    ros::NodeHandle n;
    waypoint_pub = n.advertise<g_planner::point>("trajectory/preliminary", 1000);
    setpoint_pub = n.advertise<geometry_msgs::PoseStamped>("mavros/setpoint_position/local",10);
    state_sub = n.subscribe<mavros_msgs::State>("mavros/state", 10, state_cb);
    pose_sub = n.subscribe<geometry_msgs::PoseStamped>("mavros/local_position/pose",10,pose_cb);
    arming_client = n.serviceClient<mavros_msgs::CommandBool>("mavros/cmd/arming");
    set_mode_client = n.serviceClient<mavros_msgs::SetMode>("mavros/set_mode");
    ros::Rate loop_rate(20);

    int PPI, pixel_length, pixel_width;
    float fro_ov, sid_ov, FOV;
    double x,y,z;


    vector<pair<double,pair<double,double>>> arr;

    cout<<"Input the Field of View of camera in terms of Degree\n";
    cin>>FOV;
    cout<<"Input Side and Front Overlap Percentage\n";
    cin>>sid_ov>>fro_ov;

    arr.push_back({-42, {-21,0}});
    arr.push_back({44, {52,0}});


    cout<<"Calculation is done considering an aspect ratio of 4:3\n";

    double drone_dist = 30.0;

    float dimension[2];
    preliminary_area_captured(FOV,dimension);

    // dimension[0] is width and dimension[1] is the length of the area seen by the image


    float distX = dimension[0] * (sid_ov/100);
    float distY = dimension[1] * (fro_ov/100);


    waypoints = find_preliminary_waypoints(dimension[0],dimension[1], arr, distX, distY, drone_dist, path_length);
    geometry_msgs::PoseStamped pose;
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 10;

    for(int i = 100; ros::ok() && i > 0; --i){
        setpoint_pub.publish(pose);
        ros::spinOnce();
        loop_rate.sleep();
    }
    // publish();
    // takeoff();
    mavros_msgs::MountControl gimbal;
    gimbal.mode = 2;
    gimbal.pitch = -90.0;
    gimbal.roll = 0.0;
    gimbal.yaw = 0.0;
    geometry_msgs::Point point;
    for (int i = 0; i < waypoints.size(); i++){
        point.x = waypoints[i][0];
        point.y = waypoints[i][1];
        point.z = waypoints[i][2];
        trajectory.surface1.push_back(point);
    }
    trajectory.length.push_back(path_length);
    trajectory.gimbal.push_back(gimbal);
    waypoint_pub.publish(trajectory);
    // display(waypoints);
    
    // while (ros::ok()){
    //     ros::spinOnce();
    //     loop_rate.sleep();
    // }
    return 0;
}