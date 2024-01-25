import matplotlib.pyplot as plt
import numpy as np

# 设置字体为 Times New Roman和字号14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 18

# data
x_ticks = np.arange(1, 8)
y_data = [45, 47, 52, 55, 84, 121, 213]

# create LaTeX style labels
x_labels = ['$2^{' + str(i) + '}$' for i in x_ticks]

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(x_ticks, y_data, marker='o', linestyle='dashed', markersize=12)

plt.xticks(ticks=x_ticks, labels=x_labels)

# Modify the line width of the axes
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)


plt.ylabel('Time (s/epoch)')
plt.xlabel('Diffusion Steps')
plt.grid(True)

plt.savefig('../pics/cost_time.pdf', dpi=1000, bbox_inches='tight')
plt.show()