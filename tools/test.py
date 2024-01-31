import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

cs = plt.cm.get_cmap('tab20c').colors

fig, ax = plt.subplots(1, 1, sharex=True, figsize=(11, 9))
plt.subplots_adjust(wspace=0.3)

x_v1 = [0.7, 1.95, 3.2]
x_v2 = [1.0, 2.25, 3.5]
x_v3 = [1.3, 2.55, 3.8]
x_v4 = [1.6, 2.85, 4.1]

# # 调整柱状图横坐标的位置和宽度
# x_v1 = [0.7, 1.95, 3.2]
# x_v2 = [1.7, 3.05, 4.3]  # 调整这里的数值
# x_v3 = [2.7, 4.05, 5.3]  # 调整这里的数值
# x_v4 = [3.7, 5.05, 6.3]  # 调整这里的数值


y1_v1 = [60.18396667, 61.75596667, 62.11233333]
y1_v2 = [59.99756667, 61.9792, 62.0181]
y1_v3= [59.62886667, 61.60713333, 62.4139]
y1_v4 = [59.9449, 61.45836667, 61.941]

# error_v1 = [0.798393796, 0.24, 0.18]  # 误差棒数据，可以根据需要调整
# error_v2 = [0.614611913, 0.15, 0.13]
# error_v3 = [0.05, 0.12, 0.1]
# error_v4 = [0.05, 0.12, 0.1]

allfontsize = 40

ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.grid(color='lightgray', linestyle='--')

# 调整刻度线的宽度
ax.tick_params(labelsize=54, width=1)

ax.set_xticks([1.15, 2.4, 3.65])
ax.set_xticklabels(['Twitter', 'Christianity', 'Meme'], fontsize=allfontsize)

ax.bar(x_v1, y1_v1, color=cs[0], linewidth=1, width=.3, edgecolor='white', hatch='\\', label='Linear',  capsize=5)
ax.bar(x_v2, y1_v2, color=cs[1], linewidth=1, width=.3, edgecolor='white', hatch='/', label='Sqrt',  capsize=5)
ax.bar(x_v3, y1_v3, color=cs[2], linewidth=1, width=.3, edgecolor='white', hatch='-',  label='Exp',  capsize=5)
ax.bar(x_v4, y1_v4, color=cs[3], linewidth=1, width=.3, edgecolor='white', hatch='x',  label='Cosine',  capsize=5)

ax.set_ylim(59, 63)
ax.set_ylabel('Hits@100', fontsize=48)

# legend = ax.legend(fontsize=32, loc='upper left', bbox_to_anchor=(-0.004, 1.003), ncol=1, framealpha=1)
# for handle in legend.legendHandles:
#     handle.set_height(30)  # 设置图例中线的长度，使其垂直排列

fig.legend(fontsize=30, loc='upper center', bbox_to_anchor=(0.575, 0.95), frameon=False, ncol=4, columnspacing=0.5, handletextpad=0.2)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
figure = plt.gcf()  # get current figure
plt.tight_layout()
plt.savefig('./training.pdf', dpi=300)
plt.show()
