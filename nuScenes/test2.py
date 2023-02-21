import open3d as o3d
import numpy as np
from PIL import Image

pcd = o3d.io.read_point_cloud("point_cloud.ply")
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.get_render_option().load_from_json("render_option.json")

# 设置循环次数
num_frames = 10

for i in range(num_frames):
    # 更新场景和渲染器
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()

    # 捕获当前帧
    image = vis.capture_screen_float_buffer(do_render=True)
    image = np.asarray(image)

    # 将浮点数缓冲区转换为图像，并保存为文件
    image = Image.fromarray((image * 255).astype(np.uint8))
    image.save("frame_{:05d}.png".format(i))
