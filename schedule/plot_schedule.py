import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 使用seaborn的color_palette函数生成协调的颜色
colors = ["#eed5b7", "#d44c3c", "#44757a", "#452a3d"]

data_name = "Twitter"
# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

# 数据和标签
H = ['Hits@10', 'Hits@50', 'Hits@100']
M = ['MAP@10', 'MAP@50', 'MAP@100']
HorM = H
fig, ax = plt.subplots(figsize=(8, 6), dpi=600)

x_positions = np.arange(3)
schedule = ['Linear', 'Cosine', 'Exp', 'Sqrt']
y_data = [
    [37.01226667, 52.59513333, 60.18396667],
    [37.0609, 52.28515, 59.81525],
    [37.32225, 51.9934, 59.4263],
    [36.82186667, 52.25883333, 59.99756667]
]

# 绘制柱状图
for k, method in enumerate(schedule):
    ax.bar(x_positions + k * 0.2, y_data[k], width=0.2, label=method, color=colors[k])

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
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=4)
plt.setp(legend.get_texts(), fontweight='bold')

# 设置y轴范围
plt.ylim(35, 64)

# 保存图形到文件
file_name = f'{data_name}_{HorM}.pdf'
plt.savefig(file_name, dpi=600, bbox_inches='tight')

# 显示图形（可选）
plt.show()