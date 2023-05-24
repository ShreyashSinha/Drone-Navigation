import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

         

if __name__ == "__main__":

    pcd = o3d.io.read_point_cloud('fused.ply')
    o3d.visualization.draw_geometries([pcd])
    print(pcd)
    print(np.asarray(pcd.points))

    # Convert points to a numpy array so that you can process it
    pointcloud_as_array = np.asarray(pcd.points)
    Zmin = 3.89
    Zmax = 4.2
    d = 0.1
    final_pointcloud_array = []
    for point in pointcloud_as_array:
        if  Zmin - d < point[2] < Zmax + d:
            final_pointcloud_array.append(point)
    final_pointcloud = o3d.geometry.PointCloud()
    final_pointcloud.points = o3d.utility.Vector3dVector(final_pointcloud_array)
    o3d.visualization.draw_geometries([final_pointcloud])
    with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(
            final_pointcloud.cluster_dbscan(eps=0.05, min_points=4, print_progress=True))

    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    final_pointcloud.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([final_pointcloud])
    print(labels.shape)