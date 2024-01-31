import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

cs = plt.cm.get_cmap('tab20c').colors

fig, ax = plt.subplots(1, 1, sharex=True, figsize=(11, 9))
plt.subplots_adjust(wspace=1)

x_v1 = [0.7, 1.95, 3.2]
x_v2 = [1.0, 2.25, 3.5]
x_v3 = [1.3, 2.55, 3.8]
x_v4 = [1.6, 2.85, 4.1]

y1_v1 = [60.18396667, 61.75596667, 62.11233333]
y1_v2 = [59.99756667, 61.9792, 62.0181]
y1_v3= [59.62886667, 61.60713333, 62.4139]
y1_v4 = [59.9449, 61.45836667, 61.941]

# 调整刻度线的宽度
ax.tick_params(labelsize=54, width=1)

ax.set_xticks([1.15, 2.4, 3.65])
ax.set_xticklabels(['Twitter', 'Christianity', 'Meme'], fontsize=42)

ax.bar(x_v1, y1_v1, color=cs[0], linewidth=1, width=.3, edgecolor='white', hatch='\\', label='Linear',  capsize=5)
ax.bar(x_v2, y1_v2, color=cs[1], linewidth=1, width=.3, edgecolor='white', hatch='/', label='Sqrt',  capsize=5)
ax.bar(x_v3, y1_v3, color=cs[2], linewidth=1, width=.3, edgecolor='white', hatch='-',  label='Exp',  capsize=5)
ax.bar(x_v4, y1_v4, color=cs[3], linewidth=1, width=.3, edgecolor='white', hatch='x',  label='Cosine',  capsize=5)




plt.show()