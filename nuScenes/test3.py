import open3d as o3d

# 加载点云
pcd = o3d.io.read_point_cloud("cloud.pcd")

# 创建visualizer
vis = o3d.visualization.Visualizer()
vis.create_window()

# 设置视角并添加点云
ctr = vis.get_view_control()
vis.add_geometry(pcd)
ctr.rotate(30.0, 20.0)

# 保存视角
trajectory = o3d.camera.PinholeCameraTrajectory()
intrinsic = ctr.convert_to_pinhole_camera_parameters().intrinsic
extrinsic = ctr.convert_to_pinhole_camera_parameters().extrinsic
trajectory.parameters.append(o3d.camera.PinholeCameraParameters(intrinsic, extrinsic))
o3d.io.write_pinhole_camera_trajectory("view.json", trajectory)

# 加载视角并应用
loaded_trajectory = o3d.io.read_pinhole_camera_trajectory("view.json")
ctr.convert_from_pinhole_camera_parameters(loaded_trajectory.parameters[0])
vis.poll_events()
vis.update_renderer()
