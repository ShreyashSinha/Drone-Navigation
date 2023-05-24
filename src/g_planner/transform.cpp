#include <bits/stdc++.h>
#include <ros/ros.h>
#include "geometry_msgs/Point.h"
#include "mavros_msgs/PositionTarget.h"
#include "quadrotor_msgs/PositionCommand.h"


using namespace std;
ros::Publisher pub;

void transform_cb(const quadrotor_msgs::PositionCommand::ConstPtr& msg){
    mavros_msgs::PositionTarget point;
    point.coordinate_frame = 1;
    point.position.x = msg->position.x;
    point.position.y = msg->position.y;
    point.position.z = msg->position.z;
    point.yaw = msg->yaw;
    point.header.frame_id = "";
    for (int i = 100; i > 0; --i)
    {
        pub.publish(point);
    }
    
}


int main(int argc, char **argv){
    ros::init(argc, argv, "transform");
    ros::NodeHandle n;
    ros::Subscriber surface_feedback = n.subscribe<quadrotor_msgs::PositionCommand>("/planning/pos_cmd",1,transform_cb);
    pub = n.advertise<mavros_msgs::PositionTarget>("mavros/setpoint_raw/local", 10);

    ros::spin();
    // ros::Rate loop_rate(20);

    // while(ros::ok()){
    //     ros::spinOnce();
    //     loop_rate.sleep();
    // }
}
