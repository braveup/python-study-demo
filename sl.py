import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


 # 创建在一定范围内间隔均匀数字列表
x = np.linspace(0, 90, 100) 
 # 绘制每个x点的正弦值
plt.plot(x, np.sin(x))  

plt.show()