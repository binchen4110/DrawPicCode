import matplotlib.pyplot as plt
import numpy as np

# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

# 数据
x = ['Hits@10', 'Hits@50', 'Hits@100', 'MAP10', 'MAP50', 'MAP100']
line1 = [9.9456, 20.2797, 28.3087, 6.303066667, 6.742966667, 6.854833333]
line2 = [10.8003, 21.3934, 29.5778, 6.765966667, 7.2285, 7.342833333]
line3 = [10.5154, 20.7718, 28.3864, 6.540666667, 6.984366667, 7.0897]

error_line1 = [0.411149754, 1.173244271, 0.427938232, 0.395650418, 0.416866433, 0.408917722]
error_line2 = [0.411149754, 0.628041623, 0.314020811, 0.043754924, 0.016876907, 0.018500367]
error_line3 = [0.350368706, 0.237377421, 0.272873432, 0.137255832, 0.167896228, 0.169232473]

mark_color32 = "#eed5b7"
mark_color64 = "#d44c3c"
mark_color128 = "#44757a"

# 设置各组条形图的位置和宽度
barWidth = 0.2
r1 = np.arange(len(line1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# 创建柱状图
plt.figure(figsize=[10, 8])

error_kw=dict(ecolor='black', capsize=2)
plt.bar(r1, line1, width=barWidth, color=mark_color32, edgecolor='white', label='size = 32', yerr=error_line1, **error_kw)
plt.bar(r2, line2, width=barWidth, color=mark_color64, edgecolor='white', label='size = 64', yerr=error_line2, **error_kw)
plt.bar(r3, line3, width=barWidth, color=mark_color128, edgecolor='white', label='size = 128', yerr=error_line3, **error_kw)

# 加粗边框
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 添加图例
plt.legend()

# 设置x轴标签和标题
plt.xlabel('Metrics', fontweight='bold')
plt.title('Android')

# 设置x轴刻度标签
plt.xticks([r + barWidth for r in range(len(line1))], x)

# 设置子图横坐标（X轴）标签加粗
for label in ax.get_xticklabels():
    label.set_fontweight('bold')

# 设置子图纵坐标（Y轴）标签加粗
for label in ax.get_yticklabels():
    label.set_fontweight('bold')

# 设置图例正中央 加粗
# 设置图例正中央
legend = ax.legend()
plt.setp(legend.get_texts(), fontweight='bold')

plt.savefig('../pics/bar_chart.pdf', dpi=1000, bbox_inches='tight')
# 显示图形
plt.show()