#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include "lawnmow.h"
#include "calibration.h"
#include "corner_points.h"
#include <ros/ros.h>
#include "geometry_msgs/Point.h"
#include "g_planner/point.h"
#include "g_planner/camera.h"
#include "struct.h"
#include <std_msgs/Bool.h>
#include <mavros_msgs/MountControl.h>
using namespace std;

// g_planner::point trajectory;
trajectory path;
vector<vector<vector<double>>> lawnmow_waypoints;
vector<vector<vector<double>>> camera_waypoints;
float path_length[5] = {0,0,0,0,0};
ros::Publisher lawnmow_pub;
ros::Publisher camera_pub;


int surface_index = 0;
// int path_index = 0;

bool feedback = false;


// struct Point {
//     float x;
//     float y;
//     float z;
// };

void display(vector<vector<double>> waypoint){
    for (auto& x: waypoint){
        for (auto& y: x){
            cout<<y<<" ";
        }
        cout<<"\n";
    }
}

void feedback_cb(const std_msgs::Bool::ConstPtr& fb){
    feedback = fb->data;
    if (feedback){
    
        geometry_msgs::Point point;
        for (int j = 0; j < camera_waypoints[surface_index].size(); j++){
            point.x = camera_waypoints[surface_index][j][0];
            point.y = camera_waypoints[surface_index][j][1];
            point.z = camera_waypoints[surface_index][j][2];
            path.camera_points.camera_waypoints.push_back(point);
            // my_array[j] = point;
        }
        camera_pub.publish(path.camera_points);
        surface_index++;
        // for(int k = 0; k < 100; k++){
        //     ros::spinOnce();
        //     loop_rate.sleep();
        // }
    }
}

void publish(){

    geometry_msgs::Point point;
    mavros_msgs::MountControl gimbal;
    gimbal.mode = 2;
    gimbal.pitch = 0.0;
    gimbal.roll = 0.0;
    for (int j = 0; j < lawnmow_waypoints[0].size(); j++){
        point.x = lawnmow_waypoints[0][j][0];
        point.y = lawnmow_waypoints[0][j][1];
        point.z = lawnmow_waypoints[0][j][2];
        path.lawnmow_points.surface1.push_back(point);
    }
    path.lawnmow_points.length.push_back(path_length[0]);
    gimbal.yaw = -90.0;
    path.lawnmow_points.gimbal.push_back(gimbal);
    for (int j = 0; j < lawnmow_waypoints[1].size(); j++){
        point.x = lawnmow_waypoints[1][j][0];
        point.y = lawnmow_waypoints[1][j][1];
        point.z = lawnmow_waypoints[1][j][2];
        path.lawnmow_points.surface2.push_back(point);
    }
    path.lawnmow_points.length.push_back(path_length[1]);
    gimbal.yaw = -180;
    path.lawnmow_points.gimbal.push_back(gimbal);
    for (int j = 0; j < lawnmow_waypoints[2].size(); j++){
        point.x = lawnmow_waypoints[2][j][0];
        point.y = lawnmow_waypoints[2][j][1];
        point.z = lawnmow_waypoints[2][j][2];
        path.lawnmow_points.surface3.push_back(point);
    }
    path.lawnmow_points.length.push_back(path_length[2]);
    gimbal.yaw = -270.0;
    path.lawnmow_points.gimbal.push_back(gimbal);
    for (int j = 0; j < lawnmow_waypoints[3].size(); j++){
        point.x = lawnmow_waypoints[3][j][0];
        point.y = lawnmow_waypoints[3][j][1];
        point.z = lawnmow_waypoints[3][j][2];
        path.lawnmow_points.surface4.push_back(point);
    }
    path.lawnmow_points.length.push_back(path_length[3]);
    gimbal.yaw = 0.0;
    path.lawnmow_points.gimbal.push_back(gimbal);
    for (int j = 0; j < lawnmow_waypoints[4].size(); j++){
        point.x = lawnmow_waypoints[4][j][0];
        point.y = lawnmow_waypoints[4][j][1];
        point.z = lawnmow_waypoints[4][j][2];
        path.lawnmow_points.surface5.push_back(point);
    }
    path.lawnmow_points.length.push_back(path_length[4]);
    gimbal.pitch = -90.0;
    path.lawnmow_points.gimbal.push_back(gimbal);
    lawnmow_pub.publish(path.lawnmow_points);
    // trajectory.length = path_length[path_index];
    // surface_index++;
    // path_index++;
    // for(int k = 0; k < 50; k++){
    //     pub.publish(trajectory);
    //     ros::spinOnce();
    //     loop_rate.sleep();
    // }
}

 
int main(int argc, char **argv){

    ros::init(argc, argv, "main");
    ros::NodeHandle n;
    ros::Subscriber camera_feedback = n.subscribe<std_msgs::Bool>("camera_feedback",1,feedback_cb);
    lawnmow_pub = n.advertise<g_planner::point>("trajectory/global", 1000);
    camera_pub = n.advertise<g_planner::camera>("trajectory/camera", 1000);

    ros::Rate loop_rate(20);

    int PPI, pixel_length, pixel_width;
    float fro_ov, sid_ov, FOV;
    double x,y,z;
    ifstream inFile;


    vector<pair<double,pair<double,double>>> arr;


    cout<<"Input PPI range between 70 - 90\n";
    cin>>PPI;
    cout<<"Input the needed resolution in terms of length and width\n";
    cin>>pixel_length>>pixel_width;
    cout<<"Input the Field of View of camera in terms of Degree\n";
    cin>>FOV;
    cout<<"Input Side and Front Overlap Percentage\n";
    cin>>sid_ov>>fro_ov;

    cout<<"Reading Corner Points\n";

    inFile.open("./src/g_planner/points-cons.txt");
    if (!inFile) {
        cout << "Unable to open file\n";
        exit(1); // terminate with error
    }
    while (inFile >>x>>y>>z){
        arr.push_back({x, {y,z}});
    }

    inFile.close();

    vector<pair<double,pair<double,double>>> surface_1 = get_surface1(arr);
    vector<pair<double,pair<double,double>>> surface_2 = get_surface2(arr);
    vector<pair<double,pair<double,double>>> surface_3 = get_surface3(arr);
    vector<pair<double,pair<double,double>>> surface_4 = get_surface4(arr);
    vector<pair<double,pair<double,double>>> surface_5 = get_surface5(arr);
    // surface_display(surface_3);
    // surface_display(surface_4);

    // vector<vector<pair<double,pair<double,double>>>> surfaces;
    // surfaces.push_back(surface_1);
    // surfaces.push_back(surface_4);
    // surfaces.push_back(surface_2);
    // surfaces.push_back(surface_3);
    // surfaces.push_back(surface_5);

    cout<<"Calculation is done considering an aspect ratio of 4:3\n";

    double drone_dist = dist_to_drone(PPI,pixel_length,pixel_width,FOV);
    printf("For %d PPI the Distance of the Drone to the Structure must be %lf meters\n",PPI,drone_dist);


    float dimension[2];
    area_captured(PPI,pixel_length,pixel_width,FOV,dimension);

    // dimension[0] is width and dimension[1] is the length of the area seen by the image


    float distX = dimension[0] * (sid_ov/100);
    float distY = dimension[1] * (fro_ov/100);

    bool ascending = true;
    bool neg = true;
    bool mirror_xz = false;
    bool mirror_yz = true;
    bool mirror_xy = false;
    bool camera_mirror_xz = false;
    bool camera_mirror_yz = true;
    bool camera_mirror_xy = false;



    if (ascending and neg){
        lawnmow_waypoints.push_back(find_lawnmow_waypoint(dimension[0],dimension[1], surface_3, distX, distY, ascending, -drone_dist, mirror_xz, path_length[0]));
        camera_waypoints.push_back(find_camera_waypoint(dimension[0],dimension[1], surface_3, distX, distY, ascending, -drone_dist, camera_mirror_xz, path_length[0]));
        neg = false;
        ascending = false;
    }
    if(!ascending and !neg){
        vector<vector<double>> tmp_lawn = find_lawnmow_waypoint(dimension[0],dimension[1], surface_2, distX, distY, ascending, drone_dist, mirror_yz, path_length[1]);
        tmp_lawn.pop_back(); 
        vector<vector<double>> tmp_camera = find_camera_waypoint(dimension[0],dimension[1], surface_2, distX, distY, ascending, drone_dist, camera_mirror_yz, path_length[1]);
        tmp_camera.pop_back(); 
        lawnmow_waypoints.push_back(tmp_lawn);
        camera_waypoints.push_back(tmp_camera);
        ascending = true;
    }
    if(ascending and !neg){
        lawnmow_waypoints.push_back(find_lawnmow_waypoint(dimension[0],dimension[1], surface_4, distX, distY, ascending, drone_dist, mirror_xz, path_length[2]));
        camera_waypoints.push_back(find_camera_waypoint(dimension[0],dimension[1], surface_4, distX, distY, ascending, drone_dist, camera_mirror_xz, path_length[2]));
        ascending = false;
        neg = true;
    }
    if (!ascending and neg){
        vector<vector<double>> tmp_lawn = find_lawnmow_waypoint(dimension[0],dimension[1], surface_1, distX, distY, ascending, -drone_dist, mirror_yz, path_length[3]);
        tmp_lawn.pop_back();
        vector<vector<double>> tmp_camera = find_camera_waypoint(dimension[0],dimension[1], surface_1, distX, distY, ascending, -drone_dist, camera_mirror_yz, path_length[3]);
        tmp_camera.pop_back();  
        lawnmow_waypoints.push_back(tmp_lawn);
        camera_waypoints.push_back(tmp_camera);
        ascending = true;
        neg = false;
    }
    lawnmow_waypoints.push_back(find_lawnmow_waypoint(dimension[0],dimension[1], surface_5, distX, distY, ascending, drone_dist, mirror_xy, path_length[4]));
    camera_waypoints.push_back(find_camera_waypoint(dimension[0],dimension[1], surface_5, distX, distY, ascending, drone_dist, camera_mirror_xy, path_length[4]));

    
    // for (int i = 0; i < camera_waypoints.size(); i++){
    //     cout<<lawnmow_waypoints[i].size()<<endl;
    //     cout<<camera_waypoints[i].size()<<endl;
    // }

    // display(lawnmow_waypoints[0]);
    publish();

    geometry_msgs::Point point;
    for (int j = 0; j < camera_waypoints[surface_index].size(); j++){
        point.x = camera_waypoints[surface_index][j][0];
        point.y = camera_waypoints[surface_index][j][1];
        point.z = camera_waypoints[surface_index][j][2];
        path.camera_points.camera_waypoints.push_back(point);
    }
    surface_index++;
    camera_pub.publish(path.camera_points);

    while (ros::ok()){
        ros::spinOnce();
        loop_rate.sleep();
    }
        
    return 0;
}