import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14

# 定义 alpha 和 beta 的值
alpha_values = [0.1, 0.2, 0.3, 0.4, 0.5]
beta_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# 创建 alpha 和 beta 的网格
alpha, beta = np.meshgrid(alpha_values, beta_values)

# 生成示例数据，替换为你的实际数据
hits = np.array([
    [28.7749, 29.1893, 29.1634, 29.1634, 29.0598],  # alpha=0.1
    [28.9044, 28.5936, 28.6713, 28.8008, 28.7749],  # alpha=0.2
    [28.8526, 28.9821, 28.8267, 28.9303, 28.8267],  # alpha=0.3
    [28.9303, 28.9821, 28.4382, 28.3346, 28.9303],  # alpha=0.4
    [28.2569, 27.9979, 27.8943, 28.0238, 28.49]   # alpha=0.5
])


# 创建三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维平面图，设置颜色映射为 'Blues'
surface = ax.plot_surface(beta, alpha, hits, cmap='Blues', edgecolor='white', linewidth=0.2)

# 添加颜色条，并设置相对长度为0.8，同时调整刻度位置和 pad 参数
colorbar = fig.colorbar(surface, label='Hits@100', shrink=0.6)
colorbar.ax.set_ylabel('Hits@100', fontsize=18)

# 调整整个图的角度，设置仰角为30度，方位角为45度（可以根据需要调整）
ax.view_init(elev=30, azim=45)

# 设置图形标题和轴标签
# ax.set_title('Alpha, Beta vs Hits')
ax.set_xlabel('Loss wight $\\alpha$', fontsize=20, labelpad=10)
ax.set_ylabel('Loss wight $\\beta$', fontsize=20, labelpad=10)
# ax.set_zlabel('Hits@100')

# 设置坐标轴刻度间隔为0.1
ax.set_xticks(np.arange(0.1, 0.6, 0.1))
ax.set_yticks(np.arange(0.1, 0.6, 0.1))
ax.set_zticks(np.arange(27.8, 29.2, 0.2))

# 设置坐标轴字体大小
ax.tick_params(axis='x', labelsize=15)  # x轴刻度字体大小
ax.tick_params(axis='y', labelsize=15)  # y轴刻度字体大小
ax.tick_params(axis='z', labelsize=15)  # x轴刻度字体大小

plt.tight_layout()
plt.savefig("../pics/3d_hits100.pdf", dpi=1000, bbox_inches='tight')
plt.show()
