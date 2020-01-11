# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-1, 1, 50)
# y = 2*x + 1
#
# plt.figure()
# plt.plot(x, y)
# plt.show()


from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 设置字体
#my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图片
plt.plot(x, y)

# 设置x州的刻度
# 调整x轴的刻度
_xtick_labels = ["10:{}".format(i) for i in range(60)] + ["11:{}".format(i) for i in range(60)]
# 取步长，数字和字符一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=-90)

# 设置添加描述信息
plt.xlabel('time')
plt.ylabel('temperature')
plt.title("10 clock~12clock temperature changes every minute")

# 展示图片
plt.show()
