#include <iostream>
#include "g_planner/point.h"
#include "g_planner/camera.h"

using namespace std;

#ifndef STRUCT_H
#define STRUCT_H
typedef struct Waypoints
{
    g_planner::point lawnmow_points;
    g_planner::camera camera_points;
}trajectory;
#endif
