import matplotlib.pyplot as plt
import numpy as np

# 两个数据集
x_values = np.array([1, 2, 3, 4, 5])
y_values1 = np.array([10, 12, 5, 8, 15])
y_values2 = np.array([30, 35, 38, 32, 40])

# 计算方差
variance1 = np.array([1, 0.5, 1.2, 0.8, 0.6])  # 举例，实际应根据数据计算
variance2 = np.array([0.8, 1, 0.7, 0.9, 1.5])  # 举例，实际应根据数据计算

# 添加阴影表示方差
plt.fill_between(x_values, y_values1 - variance1, y_values1 + variance1, alpha=0.2)
plt.fill_between(x_values, y_values2 - variance2, y_values2 + variance2, alpha=0.2)

# 绘制两条折线，并指定图例样式
line1, = plt.plot(x_values, y_values1, linestyle='-', marker='D', markersize=10, label='Line 1')  # 调整菱形大小
line2, = plt.plot(x_values, y_values2, linestyle='--', marker='H', markersize=12, label='Line 2')  # 调整六边形大小

# 添加虚线网格线
plt.grid(True, linestyle='--')

# 添加标题和标签
plt.title('Lines with Variance Shading')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label - Line 1')

# 指定图例样式
plt.legend(handles=[line1, line2], labels=['Custom Line 1', 'Custom Line 2'])

# 创建第二个纵坐标轴，共享X轴
ax2 = plt.gca().twinx()
ax2.set_ylabel('Y-axis Label - Line 2')

# 截断纵坐标轴范围
plt.ylim(10, 20)
ax2.set_ylim(30, 40)

# 去掉右边和上边框
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# 显示图形
plt.show()
