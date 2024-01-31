import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 14
x_ticks = np.arange(1, 8)
# 设置横坐标轴的数据
x_data_origin = [2, 4, 8, 16, 32, 64, 128]
x_data = ['$2^{' + str(i) + '}$' for i in x_ticks]

y_android = [7.259933333, 7.277333333, 7.309066667, 7.270766667, 7.342833333, 7.0932, 7.242866667]
y_chris = [20.62106667, 20.38103333, 20.35526667, 20.23973333, 20.63543333, 20.44753333, 20.50733333]
y_twitter = [25.7037, 25.9969, 25.82223333, 25.7408, 26.16343333, 25.93006667, 25.6845]

fig, (ax3, ax2, ax1) = plt.subplots(3, 1, sharex=True, figsize=(12, 9))
fig.subplots_adjust(hspace=0.1)  # adjust space between axes

ax1.plot(x_data, y_android, marker='^', markeredgewidth=2, markersize=24, linestyle='-', color='black', markerfacecolor='#79b4a0', linewidth=2,label='Android')
ax2.plot(x_data, y_chris, marker='o', markeredgewidth=2, markersize=22, linestyle='-', color='black', markerfacecolor='#E76254', linewidth=2,label='Christianity')
ax3.plot(x_data, y_twitter, marker='D', markeredgewidth=2, markersize=18, linestyle='-', color='black', markerfacecolor='#6BAED6', linewidth=2,label='Twitter')

ax1.set_ylim(7.0, 7.45)
ax1.set_yticks(np.linspace(7.0, 7.40, 3))
ax1.set_yticklabels([f'{value:.2f}' for value in np.linspace(7.0, 7.40, 3)], fontsize=52)
ax2.set_ylim(20.1, 20.7)
ax2.set_yticks(np.linspace(20.1, 20.7, 3))
ax2.set_yticklabels([f'{value:.2f}' for value in np.linspace(20.1, 20.7, 3)], fontsize=52)
ax3.set_ylim(25.5, 26.5)
ax3.set_yticks(np.linspace(25.6, 26.4, 3))
ax3.set_yticklabels([f'{value:.2f}' for value in np.linspace(25.6, 26.4, 3)], fontsize=52)

ax1.tick_params(axis='y', labelsize=46)
ax2.tick_params(axis='y', labelsize=46)
ax3.tick_params(axis='y', labelsize=46)

# ax1.tick_params(axis='x', rotation=15, labelsize=46)

ax2.set_ylabel('MAP@100', fontsize=52, fontfamily='Times New Roman')

ax1.spines.top.set_visible(False)
ax2.spines.top.set_visible(False)
ax2.spines.bottom.set_visible(False)
ax3.spines.bottom.set_visible(False)

ax3.tick_params(axis='x', length=0)
ax2.tick_params(axis='x', length=0)
ax3.xaxis.tick_bottom()

ax1.grid(ls='--', alpha=0.5, linewidth=2)
ax2.grid(ls='--', alpha=0.5, linewidth=2)
ax3.grid(ls='--', alpha=0.5, linewidth=2)

ax1.xaxis.set_tick_params(width=2, length=8)
ax1.spines['bottom'].set_linewidth(2)
ax1.spines['left'].set_linewidth(2)
ax1.spines['right'].set_linewidth(2)
ax2.spines['left'].set_linewidth(2)
ax2.spines['right'].set_linewidth(2)
ax3.spines['top'].set_linewidth(2)
ax3.spines['left'].set_linewidth(2)
ax3.spines['right'].set_linewidth(2)

# 在x=2这个地方放置一条虚线
ax1.vlines(4, 7, 7.35, linestyles='dashed', colors='black', linewidth=2)
ax2.vlines(4, 0, 20.65, linestyles='dashed', colors='black', linewidth=2)
ax3.vlines(4, 0, 26.2, linestyles='dashed', colors='black', linewidth=2)

# 设置横坐标轴刻度的间距相同
ax1.set_xticks(x_data)
ax2.set_xticks(x_data)
ax3.set_xticks(x_data)

# 设置横坐标轴刻度标签
ax1.set_xticklabels(x_data, fontsize=52)
ax2.set_xticklabels(x_data, fontsize=52)
ax3.set_xticklabels(x_data, fontsize=52)

# d = 0.5
# kwargs = dict(marker=[(-1, -d), (1, d)], markersize=18,
#               linestyle="none", color='k', mec='k', mew=4, clip_on=False)
# ax1.plot([0, 1], [1, 1], transform=ax1.transAxes, **kwargs)
# ax2.plot([0, 1], [0, 0], transform=ax2.transAxes, **kwargs)
# ax2.plot([1, 0], [1, 1], transform=ax2.transAxes, **kwargs)
# ax3.plot([0, 1], [0, 0], transform=ax3.transAxes, **kwargs)

# 定义y轴斜线段的长度
d = 0.02

# 定义斜线段旋转以及颜色
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False, linewidth=4)
ax1.plot((-d, +d), (1-d, 1+d), **kwargs)

kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False, linewidth=4)
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
ax2.plot((- d, + d), (-d, +d), **kwargs)

kwargs = dict(transform=ax3.transAxes, color='k', clip_on=False, linewidth=4)
ax3.plot((-d, +d), (1-d, 1+d), **kwargs)
ax3.plot((- d, + d), (-d, +d), **kwargs)

# Create a single legend for all three subplots above the entire figure
fig.legend(fontsize=30, loc='upper center', bbox_to_anchor=(0.6, 0.995), frameon=False, ncol=3, columnspacing=0.5, handletextpad=0.2)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

_ = plt.xticks(x_data, x_data_origin)


plt.tight_layout()
plt.savefig('../pics/steps_map.pdf', dpi=1000, bbox_inches='tight')
plt.show()