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
    [7.1585, 7.297833333, 7.2978, 7.332266667, 7.343633333],  # alpha=0.1
    [7.288833333, 7.271133333, 7.302333333, 7.307533333, 7.228333333],  # alpha=0.2
    [7.313933333, 7.291133333, 7.325033333, 7.318233333, 7.295633333],  # alpha=0.3
    [7.295, 7.295966667, 7.245633333, 7.253966667, 7.298766667],  # alpha=0.4
    [7.180866667, 7.258533333, 7.2509, 7.2308, 7.1838]   # alpha=0.5
])


# 创建三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维平面图，设置颜色映射为 'Blues'
surface = ax.plot_surface(beta, alpha, hits, cmap='Blues', edgecolor='white', linewidth=0.2)

# 添加颜色条，并设置相对长度为0.8（可以根据需要调整）
colorbar = fig.colorbar(surface, label='Hits@100', shrink=0.6)
colorbar.ax.set_ylabel('MAP@100', fontsize=18)
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
ax.set_zticks(np.arange(7.10, 7.40, 0.05))

# 设置坐标轴字体大小
ax.tick_params(axis='x', labelsize=15)  # x轴刻度字体大小
ax.tick_params(axis='y', labelsize=15)  # y轴刻度字体大小
ax.tick_params(axis='z', labelsize=15)  # x轴刻度字体大小



plt.tight_layout()

plt.savefig("../pics/3d_map100.pdf", dpi=1000, bbox_inches='tight')
plt.show()
