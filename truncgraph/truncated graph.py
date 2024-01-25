import numpy as np
import matplotlib.pyplot as plt

# 两个数据集
x_values = np.array([1, 2, 3, 4, 5])
y_values1 = np.array([30, 35, 38, 32, 40])
y_values2 = np.array([10, 12, 13, 11, 15])

# 计算方差
variance1 = np.array([1, 0.5, 1.2, 0.8, 0.6])  # 举例，实际应根据数据计算
variance2 = np.array([0.8, 1, 0.7, 0.9, 1.5])  # 举例，实际应根据数据计算

# 创建两个绘图坐标轴；调整两个轴之间的距离，即轴断点距离
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.05)  # adjust space between axes

# 在两个轴上绘制折线图，并指定图例样式
line1, = ax1.plot(x_values, y_values1, linestyle='-', marker='D', markersize=10, color='skyblue', label='Line 1')
line2, = ax2.plot(x_values, y_values2, linestyle='--', marker='H', markersize=12, color='orange', label='Line 2')

# 添加阴影表示方差
ax1.fill_between(x_values, y_values1 - variance1, y_values1 + variance1, alpha=0.2, color='skyblue')
ax2.fill_between(x_values, y_values2 - variance2, y_values2 + variance2, alpha=0.2, color='orange')

# 调整两个y轴的显示范围
ax1.set_ylim(30, 40)  # 适当调整范围
ax2.set_ylim(10, 15)  # 适当调整范围

# 隐藏两个坐标轴系列之间的横线
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()

# 隐藏y轴刻度
ax1.tick_params(axis='x', length=0)

# 添加网格线
ax1.grid(ls='--', alpha=0.5, linewidth=1)
ax2.grid(ls='--', alpha=0.5, linewidth=1)

# 创建轴断刻度线，d用于调节其偏转角度
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)  # 注释掉这行
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)  # 保留这行

# 修改图例
ax1.legend(handles=[line1], labels=['Custom Line 1'], loc='upper left')
ax2.legend(handles=[line2], labels=['Custom Line 2'], loc='upper left')

# 去掉右边和上边框
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# 添加标题和标签
ax1.set_title('Line 1 with Variance Shading')
ax2.set_title('Line 2 with Variance Shading')
ax2.set_xlabel('X-axis Label')

# 显示图形
plt.savefig('../pics/trunc.pdf', dpi=1000, bbox_inches='tight')
plt.show()