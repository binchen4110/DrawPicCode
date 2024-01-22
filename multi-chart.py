import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 使用seaborn的color_palette函数生成协调的颜色
colors = sns.color_palette("husl", 4)
# 创建一个包含四个子图的图形
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))

# 假设你有三个采样方式的数据
H = ['H@10', 'H@50', 'H@100']
M = ['M@10', 'M@50', 'M@100']

# 假设你有三个采样方式的数据，每个采样方式有4组数据
data1 = np.random.rand(3)
data2 = np.random.rand(3)
data3 = np.random.rand(3)
data4 = np.random.rand(3)

# 设置横坐标
x_positions = np.arange(3)

# 设置不同的标记样式
marker_method1 = 'o'
marker_method2 = '^'
marker_method3 = 's'
marker_method4 = 'D'

# 00子图
TL00 = [37.01226667, 52.59513333, 60.18396667]
TC00 = [37.0609, 52.28515, 59.81525]
TE00 = [37.32225, 51.9934, 59.4263]
TS00 = [36.82186667, 52.25883333, 59.99756667]
axes[0, 0].bar(x_positions, TL00, width=0.2, label='Linear', color=colors[0])
axes[0, 0].bar(x_positions + 0.2, TC00, width=0.2, label='Cosine', color=colors[1])
axes[0, 0].bar(x_positions + 0.4, TE00, width=0.2, label='Exp', color=colors[2])
axes[0, 0].bar(x_positions + 0.6, TS00, width=0.2, label='Sqrt', color=colors[3])
axes[0, 0].set_xticks(x_positions + 0.3)
axes[0, 0].set_xticklabels(H)
axes[0, 0].legend()
axes[0, 0].set_title('Twitter')

# 01 子图
TL01 = [31.0733, 51.90706667, 62.11233333]
TC01 = [30.93106667, 51.65173333, 61.941]
TE01 = [30.92593333, 51.77856667, 62.4139]
TS01 = [30.80426667, 51.72713333, 62.0181]
axes[0, 1].bar(x_positions, TL01, width=0.2, label='Linear')
axes[0, 1].bar(x_positions + 0.2, TC01, width=0.2, label='Cosine')
axes[0, 1].bar(x_positions + 0.4, TE01, width=0.2, label='Exp')
axes[0, 1].bar(x_positions + 0.6, TS01, width=0.2, label='Sqrt')
axes[0, 1].set_xticks(x_positions + 0.3)
axes[0, 1].set_xticklabels(H)
axes[0, 1].legend()
axes[0, 1].set_title('Meme')


# 02子图
TL02 = [10.6967, 21.1603, 29.0857]
TC02 = [10.8262, 20.9013, 29.0598]
TE02 = [10.7744, 21.0567, 29.5519]
TS02 = [10.8003, 21.3934, 29.5778]
axes[0, 2].bar(x_positions, TL02, width=0.2, label='Linear')
axes[0, 2].bar(x_positions + 0.2, TC02, width=0.2, label='Cosine')
axes[0, 2].bar(x_positions + 0.4, TE02, width=0.2, label='Exp')
axes[0, 2].bar(x_positions + 0.6, TS02, width=0.2, label='Sqrt')
axes[0, 2].set_xticks(x_positions + 0.3)
axes[0, 2].set_xticklabels(H)
axes[0, 2].legend()
axes[0, 2].set_title('Android')

# 03子图
TL03 = [31.5476, 52.90176667, 61.75596667]
TC03 = [31.91963333, 52.60413333, 61.45836667]
TE03 = [31.6964, 52.9762, 61.60713333]
TS03 = [32.2917, 52.8274, 61.9792]
axes[0, 3].bar(x_positions, TL03, width=0.2, label='Linear')
axes[0, 3].bar(x_positions + 0.2, TC03, width=0.2, label='Cosine')
axes[0, 3].bar(x_positions + 0.4, TE03, width=0.2, label='Exp')
axes[0, 3].bar(x_positions + 0.6, TS03, width=0.2, label='Sqrt')
axes[0, 3].set_xticks(x_positions + 0.3)
axes[0, 3].set_xticklabels(H)
axes[0, 3].legend()
axes[0, 3].set_title('Christianity')

# 10子图
TL10 = [25.6005, 26.2937, 26.402]
TC10 = [25.1324, 25.8279, 25.9381]
TE10 = [25.31546667, 26.0011, 26.10743333]
TS10 = [25.15236667, 25.86086667, 25.97276667]
axes[1, 0].bar(x_positions, TL10, width=0.2, label='Linear')
axes[1, 0].bar(x_positions + 0.2, TC10, width=0.2, label='Cosine')
axes[1, 0].bar(x_positions + 0.4, TE10, width=0.2, label='Exp')
axes[1, 0].bar(x_positions + 0.6, TS10, width=0.2, label='Sqrt')
axes[1, 0].set_xticks(x_positions + 0.3)
axes[1, 0].set_xticklabels(M)
axes[1, 0].legend()
axes[1, 0].set_title('Twitter')


# 11子图
TL11 = [16.54293333, 17.50506667, 17.65133333]
TC11 = [16.629, 17.585, 17.73216667]
TE11 = [16.46986667, 17.4338, 17.58566667]
TS11 = [16.48156667, 17.4531, 17.5996]
axes[1, 1].bar(x_positions, TL11, width=0.2, label='Linear')
axes[1, 1].bar(x_positions + 0.2, TC11, width=0.2, label='Cosine')
axes[1, 1].bar(x_positions + 0.4, TE11, width=0.2, label='Exp')
axes[1, 1].bar(x_positions + 0.6, TS11, width=0.2, label='Sqrt')
axes[1, 1].set_xticks(x_positions + 0.3)
axes[1, 1].set_xticklabels(M)
axes[1, 1].legend()
axes[1, 1].set_title('Meme')


# 12子图
TL12 = [6.723233333, 7.200266667, 7.313533333]
TC12 = [6.784866667, 7.235966667, 7.352366667]
TE12 = [6.714766667, 7.178266667, 7.298666667]
TS12 = [6.765966667, 7.2285, 7.342833333]
axes[1, 2].bar(x_positions, TL12, width=0.2, label='Linear')
axes[1, 2].bar(x_positions + 0.2, TC12, width=0.2, label='Cosine')
axes[1, 2].bar(x_positions + 0.4, TE12, width=0.2, label='Exp')
axes[1, 2].bar(x_positions + 0.6, TS12, width=0.2, label='Sqrt')
axes[1, 2].set_xticks(x_positions + 0.3)
axes[1, 2].set_xticklabels(M)
axes[1, 2].legend()
axes[1, 2].set_title('Android')

# 13子图
TL13 = [19.40693333, 20.41826667, 20.5403]
TC13 = [19.5435, 20.51423333, 20.63556667]
TE13 = [19.5366, 20.53596667, 20.65523333]
TS13 = [19.55393333, 20.5087, 20.63543333]
axes[1, 3].bar(x_positions, TL13, width=0.2, label='Linear')
axes[1, 3].bar(x_positions + 0.2, TC13, width=0.2, label='Cosine')
axes[1, 3].bar(x_positions + 0.4, TE13, width=0.2, label='Exp')
axes[1, 3].bar(x_positions + 0.6, TS13, width=0.2, label='Sqrt')
axes[1, 3].set_xticks(x_positions + 0.3)
axes[1, 3].set_xticklabels(M)
axes[1, 3].legend()
axes[1, 3].set_title('Christianity')


# 调整图例位置
for ax in axes.flatten():

    leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=4, handlelength=1.5, \
                    columnspacing=0.5, markerscale=3)
    leg.set_in_layout(False)  # 让图例不受布局影响，以确保正确显示

    ax.set_ylim(0, 1.1 * ax.get_ylim()[1])

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
