import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 14
x_ticks = np.arange(1, 8)
x_data = ['$2^{' + str(i) + '}$' for i in x_ticks]

y_android = [28.49, 29.1634, 29.0339, 28.49, 29.5778, 29.2929, 29.1634]
y_chris = [61.60716667, 61.60713333, 61.83036667, 61.1607, 61.9792, 61.60716667, 61.60713333]
y_twitter = [60.31766667, 60.46353333, 59.63696667, 60.2042, 60.265, 60.08266667, 60.01376667]

fig, (ax3, ax2, ax1) = plt.subplots(3, 1, sharex=True, figsize=(12, 9))
fig.subplots_adjust(hspace=0.1)  # adjust space between axes

ax1.plot(x_data, y_android, marker='^', markeredgewidth=2, markersize=24, linestyle='-', color='black', markerfacecolor='#79b4a0', linewidth=2,label='Android')
ax2.plot(x_data, y_chris, marker='o', markeredgewidth=2, markersize=22, linestyle='-', color='black', markerfacecolor='#E76254', linewidth=2,label='Christianity')
ax3.plot(x_data, y_twitter, marker='D', markeredgewidth=2, markersize=18, linestyle='-', color='black', markerfacecolor='#6BAED6', linewidth=2,label='Twitter')

ax1.set_ylim(28.30, 29.70)
ax1.set_yticks(np.linspace(28.40, 29.60, 3))
ax1.set_yticklabels([f'{value:.2f}' for value in np.linspace(28.40, 29.60, 3)], fontsize=52)
ax2.set_ylim(60.9, 62.2)
ax2.set_yticks(np.linspace(61.0, 62.0, 3))
ax2.set_yticklabels([f'{value:.2f}' for value in np.linspace(61.0, 62.0, 3)], fontsize=52)
ax3.set_ylim(59.6, 61.0)
ax3.set_yticks(np.linspace(59.5, 61.0, 3))
ax3.set_yticklabels([f'{value:.2f}' for value in np.linspace(59.6, 60.5, 3)], fontsize=52)

ax1.tick_params(axis='y', labelsize=46)
ax2.tick_params(axis='y', labelsize=46)
ax3.tick_params(axis='y', labelsize=46)

ax1.tick_params(axis='x', rotation=15, labelsize=46)

ax2.set_ylabel('Hits@100', fontsize=52, fontfamily='Times New Roman')

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

d = 0.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=18,
              linestyle="none", color='k', mec='k', mew=4, clip_on=False)
ax1.plot([0, 1], [1, 1], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [0, 0], transform=ax2.transAxes, **kwargs)
ax2.plot([1, 0], [1, 1], transform=ax2.transAxes, **kwargs)
ax3.plot([0, 1], [0, 0], transform=ax3.transAxes, **kwargs)

# Create a single legend for all three subplots above the entire figure
fig.legend(fontsize=25, loc='upper center', bbox_to_anchor=(0.6, 0.97), frameon=False, ncol=3)
ax1.set_xlabel('Diffusion Step', fontsize=45)
plt.tight_layout()
plt.savefig('../pics/steps_hits.pdf', dpi=600, bbox_inches='tight')
plt.show()
