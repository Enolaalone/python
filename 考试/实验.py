import matplotlib.pyplot as plt

# 创建一个新的图形
plt.figure()

# 绘制箭头
plt.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='blue', ec='blue')

# 设置坐标轴的范围
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# 显示图形
plt.show()