import numpy as np
import matplotlib.pyplot as plt

# 使用seaborn的color_palette函数生成协调的颜色
# colors = ["#eed5b7", "#d44c3c", "#44757a", "#452a3d"]
# colors = ["#79b4a0", "#e76254", "#6BAED6", "#452a3d"]

# colors = ["#8ECFC9", "#FFBE7A", "#FA7F6F", "#82B0D2"]
cs = plt.cm.get_cmap('tab20c').colors
# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20

x_ticks = ['Twitter', 'Christianity', 'Meme']
x_positions = np.arange(3)
schedule = ['Linear', 'Sqrt', 'Exp', 'Cosine']
# y_data = [
#     [60.18396667, 59.99756667, 59.62886667, 59.9449],
#     [61.75596667, 61.9792, 61.60713333, 61.45836667],
#     [62.11233333, 62.0181, 62.4139, 61.941]
# ]

# y_data = [
#     [60.18396667, 61.75596667, 62.11233333],
#     [60.62, 62.26, 62.0181],
#     [59.62886667, 61.60713333, 62.4139],
#     [59.9449, 61.45836667, 61.941]
# ]

y_data = [
    [60.18396667, 61.75596667, 62.11233333],
    [59.99756667, 61.9792, 62.0181],
    [59.62886667, 61.60713333, 62.4139],
    [59.9449, 61.45836667, 61.941]
]

fig, ax = plt.subplots(figsize=(8, 6), dpi=800)
# 绘制柱状图
ax.bar(x_positions + 0.2, y_data[0], color=cs[0], linewidth=1, width=.2, edgecolor='white', hatch='\\', label='Linear',  capsize=5)
ax.bar(x_positions + 0.4, y_data[1], color=cs[1], linewidth=1, width=.2, edgecolor='white', hatch='\\', label='Sqrt',  capsize=5)
ax.bar(x_positions + 0.6, y_data[2], color=cs[2], linewidth=1, width=.2, edgecolor='white', hatch='\\', label='Exp',  capsize=5)
ax.bar(x_positions + 0.8, y_data[3], color=cs[3], linewidth=1, width=.2, edgecolor='white', hatch='\\', label='Cosine',  capsize=5)

# for k, method in enumerate(schedule):
#     ax.bar(x_positions + k * 0.2, y_data[k], width=0.2, label=method, color=cs[k])

# 设置X轴标签和标题
ax.set_xticks(x_positions + 0.5)
ax.set_xticklabels(x_ticks, fontsize=25)
ax.set_ylabel('Hits@100', fontsize=25)
# 设置纵轴坐标数值为粗体
# ax.yaxis.label.set_fontweight('bold')
# 设置y轴范围
plt.ylim(59, 63)
# 添加图例
# Create a single legend for all three subplots above the entire figure
fig.legend(fontsize=20, loc='upper center', bbox_to_anchor=(0.55, 0.95), frameon=False, ncol=4, columnspacing=0.5, handletextpad=0.2)

plt.tight_layout()
plt.savefig('../pics/schedule@Hits100.pdf', dpi=100)
# 显示图形
plt.show()
