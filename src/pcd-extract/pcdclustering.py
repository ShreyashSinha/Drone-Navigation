import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import pandas as pd
import os
import copy

path = "/home/impact4impact/IMAGES/rgb/dense/"

def rotate(pcd):
    pcd_r = copy.deepcopy(pcd)
    R = mesh.get_rotation_matrix_from_xyz((np.pi/180 * (0), np.pi/180 * (0),np.pi/180 * (-90)))
    pcd_r.rotate(R, center=(0, 0, 0))
    # mesh_r = copy.deepcopy(mesh)
    # mesh_r.rotate(mesh.get_rotation_matrix_from_xyz((np.pi/180 * (0), np.pi/180 * (0),np.pi/180 * (90))),
    #           center=(0, 0, 0))
    return pcd_r

def static_transform(pcd):
    x_offset = 1.0
    y_offset = 16.58
    # z_offset = -1.13
    z_offset = 0

    offsets = np.array([x_offset, y_offset, z_offset])
    pcd_points_np= np.array(pcd.points)
    # print(pcd_points_np.shape)
    pcd_points_np += offsets
    pcd.points = o3d.utility.Vector3dVector(np.array(pcd_points_np))
    return pcd

def scale(pcd):
    pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) * np.array([8.79, 8.98, 9.12]))
    return pcd

def bb_scale(bb_points):
    points_np = np.asarray(bb_points) * np.array([1.5,1.5,1])
    return points_np

    

pcd = o3d.io.read_point_cloud(os.path.join(path + "meshed-poisson.ply"))
o3d.visualization.draw_geometries([pcd])
print(pcd)


mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
pcd_r = copy.deepcopy(pcd)
R = mesh.get_rotation_matrix_from_xyz((np.pi/180 * (183), np.pi/180 * (-1.5),np.pi/180 * (-2.25)))
pcd_r.rotate(R, center=(0, 0, 0))
pcd_tz = copy.deepcopy(pcd_r).translate((-0.23, 0.1, 3.15))
print(f'Center of mesh: {mesh.get_center()}')
o3d.visualization.draw_geometries([pcd_tz,mesh])

pcd_r = rotate(pcd_tz)
aa = pcd_r.get_axis_aligned_bounding_box()
aa.color = (1,0,0)
pcd_points = aa.get_box_points()
pcd_points = np.array(pcd_points)
print(pcd_points)
o3d.visualization.draw_geometries([pcd_r,aa])


pcd_rs = scale(pcd_r)
aabb = pcd_rs.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)
scaled_pcd_points = aabb.get_box_points()
scaled_pcd_points = np.array(scaled_pcd_points)
print(scaled_pcd_points)
o3d.visualization.draw_geometries([pcd_rs])
# max = aabb.get_max_bound()
# min = aabb.get_min_bound()
# print(max)

bounds = np.array([[-15,-12,0],[13,-12,0],[13,36,0],[-15,36,0],[-15,-12,20.0],[13,-12,20.0],[13,36,20.0],[-15,36,20.0]])
points = o3d.utility.Vector3dVector(bounds)
cropdim = o3d.geometry.AxisAlignedBoundingBox.create_from_points(points)
cropped_pcd = pcd_rs.crop(cropdim)
o3d.visualization.draw_geometries([cropped_pcd])


with o3d.utility.VerbosityContextManager(
    o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(
        cropped_pcd.cluster_dbscan(eps=0.4, min_points=75, print_progress=True))
    
max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap()(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
cropped_pcd.colors = o3d.utility.Vector3dVector(colors[:,:3])
o3d.visualization.draw_geometries([cropped_pcd])

my_points = np.asarray(cropped_pcd.points).tolist()
df = pd.DataFrame(list(zip(my_points, labels.tolist())), columns=['points', 'label'])
new_df = df.groupby('label').agg(list).reset_index()[['label', 'points']]
label_to_points = new_df.set_index('label').to_dict()['points']

# for i in label_to_points:
#     demo_pc = o3d.geometry.PointCloud()
#     demo_pc.points = o3d.utility.Vector3dVector(np.array(label_to_points[i]))
#     o3d.visualization.draw_geometries([demo_pc])

# # cluster to pick from i = 0,1

cluster1 = o3d.geometry.PointCloud()
cluster1.points = o3d.utility.Vector3dVector(np.array(label_to_points[0]))
cluster1 = static_transform(cluster1)
tf = cluster1.get_axis_aligned_bounding_box()
cluster1_bb_points = tf.get_box_points()
cluster1_bb_points_np = np.array(cluster1_bb_points)
print(tf.get_center())

cluster2 = o3d.geometry.PointCloud()
cluster2.points = o3d.utility.Vector3dVector(np.array(label_to_points[1]))
cluster2 = static_transform(cluster2)

cluster1_bb = cluster1.get_axis_aligned_bounding_box()
cluster2_bb = cluster2.get_axis_aligned_bounding_box()

# cluster1_bb_scale = cluster1_bb.scale(1.5,cluster1_bb.get_center())

cluster1_bb.color = (0, 1, 0)
cluster2_bb.color = (0, 0, 1)
# cluster1_bb_scale.color = (1, 0, 1)



o3d.visualization.draw_geometries([cluster1,cluster1_bb])
# o3d.visualization.draw_geometries([cluster1,cluster1_bb_scale])
o3d.visualization.draw_geometries([cluster2,cluster2_bb])

cluster1_bb_points = cluster1_bb.get_box_points()
cluster2_bb_points = cluster2_bb.get_box_points()

cluster1_bb_points_np = np.array(cluster1_bb_points)
cluster2_bb_points_np = np.array(cluster2_bb_points)


print(cluster1_bb_points_np)
print(cluster2_bb_points_np)









