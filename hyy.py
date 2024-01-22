import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

x = np.linspace(1, 16, num=16)
cs = plt.cm.get_cmap('tab20c').colors
fig, ax = plt.subplots(ncols=2,  figsize=(9, 9), tight_layout=True)


x_v1 = [0.7, 1.9, 3.1,4.3]
x_v2 = [0.9, 2.1, 3.3,4.5]
x_v3 = [1.1, 2.3, 3.5,4.7]
x_v4 = [1.3, 2.5, 3.7,4.9]
x_v0 = [1.5, 2.7, 3.9,5.1]

y1_v1 = [0.714, 0.714, 0.71, 0.709]
y1_v2 = [0.762, 0.721, 0.727, 0.711]
y1_v3 = [0.773, 0.727, 0.733, 0.718]
y1_v4 = [0.683, 0.703, 0.68, 0.671]
y1_v0 = [0.781, 0.742, 0.744, 0.735]

y2_v1 = [0.914, 0.929, 0.947, 0.916]
y2_v2 = [0.946, 0.924, 0.942, 0.93]
y2_v3 = [0.925, 0.934, 0.949, 0.926]
y2_v4 = [0.907, 0.927, 0.941, 0.917]
y2_v0 = [0.975, 0.934, 0.95, 0.933]

ax[0].bar(x_v1, y1_v1, color=cs[3], linewidth=1, width=.2, edgecolor='white', hatch='-', zorder=5, label='DiffSL w/o cent')
ax[0].bar(x_v2, y1_v2, color=cs[2], linewidth=1, width=.2, edgecolor='white', hatch='\\', zorder=5, label='DiffSL w/o sp')
ax[0].bar(x_v3, y1_v3, color=cs[1], linewidth=1, width=.2, edgecolor='white',hatch='-',zorder=5, label='DiffSL w/o dmi')
ax[0].bar(x_v4, y1_v4, color=cs[1], linewidth=1, width=.2, edgecolor='white', hatch='/', zorder=5, label='DiffSL w/o diff')
ax[0].bar(x_v0, y1_v0, color=cs[0], linewidth=1, width=.2, edgecolor='white', zorder=5, label='DiffSL')

ax[1].bar(x_v1, y2_v1, color=cs[3], linewidth=1, width=.2, edgecolor='white', hatch='-', zorder=5)
ax[1].bar(x_v2, y2_v2, color=cs[2], linewidth=1, width=.2, edgecolor='white', hatch='\\', zorder=5)
ax[1].bar(x_v3, y2_v3, color=cs[1], linewidth=1, width=.2, edgecolor='white',hatch='-',zorder=5)
ax[1].bar(x_v4, y2_v4, color=cs[1], linewidth=1, width=.2, edgecolor='white', hatch='/', zorder=5)
ax[1].bar(x_v0, y2_v0, color=cs[0], linewidth=1, width=.2, edgecolor='white', zorder=5)
allfontsize = 24


for j in [0, 1]:
    ax[j].spines['right'].set_linewidth(2)
    ax[j].spines['top'].set_linewidth(2)
    ax[j].spines['bottom'].set_linewidth(2)
    ax[j].spines['left'].set_linewidth(2)
    ax[j].grid(color='lightgray', linestyle='--')
    ax[j].tick_params(labelsize=allfontsize)
    ax[j].set_xticks([1.1, 2.3, 3.5,4.7])
    ax[j].set_xticklabels(['Jazz','NS', 'Cora-ML','PG'])

ax[0].set_ylim(.6, .8)
ax[1].set_ylim(.8, .98)

ax[0,].set_xlabel('F1-Score', fontsize=allfontsize)
ax[1,].set_xlabel('AUC-ROC', fontsize=allfontsize)

ax[0].legend(fontsize=20, bbox_to_anchor=(.04, 1.06, 2.0, 0.15), loc='upper left', ncol=5, framealpha=1, mode='expand', borderaxespad=0., fancybox=False, )

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
figure = plt.gcf()  # get current figure
figure.set_size_inches(16, 5.5) # set figure's size manually to your full screen (32x18)

plt.savefig('./FigAblation.pdf')
plt.show()
