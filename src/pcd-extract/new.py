import copy
import numpy as np
import open3d as o3d

         

if __name__ == "__main__":

    print("Testing mesh in open3d ...")
    mesh = o3d.io.read_triangle_mesh("/Users/shreyashsinha/Desktop/cpdm-test/meshed-poisson.ply", enable_post_processing=True, print_progress=True)
    print(mesh)
    print(np.asarray(mesh.vertices))
    print(np.asarray(mesh.triangles))
    print("")
    print("Try to render a mesh with normals (exist: " +
        str(mesh.has_vertex_normals()) + ") and colors (exist: " +
        str(mesh.has_vertex_colors()) + ")")
    o3d.visualization.draw_geometries([mesh])
    print("A mesh with no normals and no colors does not seem good.")
    print("Computing normal and rendering it.")
    mesh.compute_vertex_normals()
    print(np.asarray(mesh.triangle_normals))
    o3d.visualization.draw_geometries([mesh])
    point_cloud = mesh.sample_points_uniformly(number_of_points=7000000)
    o3d.visualization.draw_geometries([point_cloud])
    print('run Poisson surface reconstruction')
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        new_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        point_cloud, depth=9)
    o3d.visualization.draw_geometries([new_mesh])
    o3d.io.write_triangle_mesh("downsampled_mesh.ply", new_mesh)


    
