import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 使用seaborn的color_palette函数生成协调的颜色
colors = ["#dedcdb", "#9dbdff", "#e7d7ce", "#d4dbe6"]
colors2 = ["#ef896b", "#d44c3c", "#44757a", "#452a3d"]
colors_scatter = ['#DF634E', '#D44E41', '#5977e3', '#3F52C6']
scatter_marker = ['^', 'D', 's', 'p']

data_name = "Twitter"
# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

# 数据和标签
H = ['100%', '90%', '80%', '70%', '60%', '50%']
M = ['MAP@10', 'MAP@50', 'MAP@100']
HorM = H
fig, ax = plt.subplots(figsize=(8, 6), dpi=600)

x_positions = np.arange(6)
schedule = ['Hyfea', 'UHAN', 'MHF', 'Seaformer']
y_data = [
    [1.6623, 1.7057, 1.7343, 1.7518, 1.7891, 1.8329],
    [1.4833, 1.5369, 1.7070, 1.8112, 1.8531, 1.9158],
    [1.5433, 1.6029, 1.7359, 1.8518, 1.8991, 1.9389],
    [1.3396, 1.341, 1.3596, 1.3799, 1.3928, 1.4123]
]

y2_data = [
    [0, 2.61, 4.33, 5.38, 7.62, 10.26],
    [0, 3.61, 15.08, 22.09, 24.92, 29.15],
    [0, 3.86, 12.47, 19.98, 23.05, 25.63],
    [0, 0.89, 1.87, 3.07, 4.96, 7.19]
]

# 绘制柱状图
for k, method in enumerate(schedule):
    ax.bar(x_positions + k * 0.2, y_data[k], width=0.2,label=method, color=colors[k])

# 设置图形属性
ax.set_xticks(x_positions + 0.3)
ax.set_xticklabels(HorM)
ax.spines['top'].set_linewidth(1.5)  # 顶部边框
ax.spines['right'].set_linewidth(1.5)  # 右侧边框
ax.spines['bottom'].set_linewidth(1.5)  # 底部边框
ax.spines['left'].set_linewidth(1.5)  # 左侧边框

# 设置子图横坐标（X轴）标签加粗
for label in ax.get_xticklabels():
    label.set_fontweight('bold')

# 设置子图纵坐标（Y轴）标签加粗
for label in ax.get_yticklabels():
    label.set_fontweight('bold')

ax.set_title(data_name)

# 设置子图标题加粗
ax.set_title(ax.get_title(), fontweight='bold')

# 设置图例正中央

# fig.legend(fontsize=20)


# 设置y轴范围
# plt.ylim(1, 3)
ax.set_ylim(1, 2.2)

#ax2
ax2 = ax.twinx()
for k, method in enumerate(schedule):
    ax2.plot(x_positions + k * 0.2, y2_data[k], label=method, color=colors2[k], linestyle='--', linewidth=0.8, marker=scatter_marker[k])
    # ax2.scatter(x_positions + k * 0.2, y2_data[k], label=method, color=colors_scatter[k], marker=scatter_marker[k], zorder=2)
ax2.set_ylim(-2, 35)
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=4, fontsize=11)

legend2 = ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 0.93), ncol=4, fontsize=11)


plt.setp(legend.get_texts(), fontweight='bold')
plt.setp(legend2.get_texts(), fontweight='bold')

# 保存图形到文件
# file_name = f'../pics/{data_name}_{HorM}.pdf'
# plt.savefig(file_name, dpi=600, bbox_inches='tight')

# 显示图形（可选）
plt.show()
