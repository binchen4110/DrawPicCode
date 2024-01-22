import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.array([1, 2, 3])
y = np.array([10, 20, 15])

# 创建包含8个子图的图形
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))

# 模拟8个子图的数据
data = np.random.rand(8, 3)

# 设置 y 轴范围
for i, ax in enumerate(axes.flatten()):
    ax.bar(x, data[i, :])
    if i == 1:
        ax.set_ylim(0, 2)  # 在这里设置每个子图的 y 轴范围
    ax.set_ylim(0.5, 1)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
