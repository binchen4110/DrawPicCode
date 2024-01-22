import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

# 设置marker
marker_edge = 'white'
marker_memes = '#FF4040'  ###FF4040 #F9CBC8 #F6563D
marker_twitter = '#E12D26'  #ED392B  D42121 E12D26
marker_weibo = '#B91419' #1D7EB7  CB7968  C8171C #AB1016 #B91419
marker_android = '#7E0610' ##085FA3   #67000D   980C13 #7E0610

# 设置x 和 y
x_ticks = [100, 200, 300, 400, 500]
y_ticks_twitter = [3.669883669, 3.563514468, 3.443794374, 3.620714766, 3.622937253]
y_ticks_android = [1.564188004, 1.532459641, 1.450981413, 1.591146708, 1.551506102]

fig, ax = plt.subplots(ncols=1, nrows=2, figsize=(5, 4))

# 在x=2这个地方放置一条虚线
ax[0].vlines(2, 0, 10, linestyles='dashed', colors='darkgrey', linewidth=2)
ax[1].vlines(2, 0, 10, linestyles='dashed', colors='darkgrey', linewidth=2)

# 设置两个折线
ax[0].plot(y_ticks_twitter, marker='s', color=marker_twitter, markeredgecolor=marker_edge, markersize=12, label='Twitter')
ax[1].plot(y_ticks_android, marker='h', color=marker_android, markeredgecolor=marker_edge, markersize=14, label='Android')

# 设置两个图y的范围
ax[0].set_ylim(3.3, 3.8)  # most of the data
ax[1].set_ylim(1.40, 1.70)  # most of the data

# 设置y的刻度
ax[0].set_yticks([3.30, 3.55, 3.80])
ax[1].set_yticks([1.40, 1.55, 1.70])

# 设置x轴范围和刻度位置
ax[0].set_xlim(-.2, len(y_ticks_twitter)-1+.2)
ax[1].set_xlim(-.2, len(y_ticks_twitter)-1+.2)
ax[0].set_xticks([i for i in range(len(y_ticks_twitter))], labels=[i for i in range(len(y_ticks_twitter))], size=18)
ax[1].set_xticks([i for i in range(len(y_ticks_twitter))], labels=[i for i in range(len(y_ticks_twitter))], size=18)

# 设置两个图的x轴坐标
ax[0].set_xticklabels([])
ax[1].set_xticklabels(x_ticks)

# 设置某些边框不可见
ax[0].spines['top'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].xaxis.tick_bottom()

# 创建图例
ax[0].legend(fontsize=20, loc='lower right', borderpad=0.15, handlelength=1.0, handletextpad=0.2)
ax[1].legend(fontsize=20, loc='lower right', borderpad=0.15, handlelength=1.0, handletextpad=0.2)

# 定义y轴斜线段的长度
d = .02

# 定义斜线段旋转以及颜色
kwargs = dict(transform=ax[0].transAxes, color='k', clip_on=False)
ax[0].plot((-d, +d), (1-d, 1+d), **kwargs)
ax[0].plot((- d, + d), (-d, +d), **kwargs)
kwargs.update(transform=ax[1].transAxes)
ax[1].plot((-d, +d), (1 - d, 1 + d), **kwargs)
ax[1].plot((- d, + d), (-d, +d), **kwargs)


for ax_ in [ax[0], ax[1]]:
    # 设置主刻度大小
    ax_.tick_params(axis='both', which='major', labelsize=16)
    # 加粗线段
    ax_.spines['bottom'].set_linewidth(2)
    ax_.spines['left'].set_linewidth(2)
    ax_.spines['top'].set_linewidth(2)
    ax_.spines['right'].set_linewidth(2)
    # 开启网格线
    ax_.grid(color='lightgray', linestyle='--')

# 隐藏ax[0]的坐标线
ax[0].tick_params(axis='x', colors='lightgray')

# 设置y label
fig.supylabel('MAP@10', fontsize=15, x=0.05)
# 调整布局
fig.tight_layout()
# 调整子图间距
plt.subplots_adjust(wspace =0, hspace =0.3)

plt.savefig("graph.pdf", dpi=600, bbox_inches='tight')
plt.show()