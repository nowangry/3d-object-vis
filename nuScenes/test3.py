import open3d as o3d

# 创建 visualizer 对象
vis = o3d.visualization.Visualizer()
vis.create_window()

# 加载点云数据
pcd = o3d.io.read_point_cloud("pointcloud.pcd")

# 加载 view_trajectory.json
view_trajectory = o3d.io.read_view_trajectory("view_trajectory.json")

# 将相机位姿转换为相机矩阵
camera_intrinsics = vis.get_render_option().intrinsics
camera_poses = []
for view in view_trajectory.views:
    camera_pose = view.camera_pose
    intrinsic = view.intrinsic
    intrinsic.set_intrinsics(camera_intrinsics.width, camera_intrinsics.height, intrinsic.intrinsic_matrix[0, 0], intrinsic.intrinsic_matrix[1, 1], camera_intrinsics.width / 2, camera_intrinsics.height / 2)
    camera_poses.append(camera_pose)
camera_matrices = o3d.camera.PinholeCameraTrajectory.convert_pinhole_camera_intrinsics_to_matrix(camera_intrinsics, camera_poses)

# 设置视角
vis.get_view_control().convert_from_pinhole_camera_parameters(camera_matrices[0])
vis.update_renderer()

# 保存当前视角
vis.capture_screen_image("image.png")

# 关闭窗口
vis.destroy_window()
