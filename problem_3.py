#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from interpolation import LagrangePolynomal


# 補間する関数
def func_f(x):
    return [1/(1+25*(i*i)) for i in x]

# 等間隔にデータを生成
def make_x_list(segment,division):
    if (len(segment)!=2) or (division%2==0) or (division!=int(division) or (division < 1)):
        print("Error. ")
        return -1
    elif (division == 1):
        return sum(segment)/2

    # 等間隔dxを得る
    range_segment = abs(segment[0]) + abs(segment[1])
    dx = range_segment/(division-1)

    return [segment[0]+i*dx for i in range(division)]


# テストデータを作成
div_num = 5
x_data = make_x_list([-1,1],div_num)
y_data = func_f(x_data)

# データと真の関数をプロットしてみる
dx = 0.001
x_plot = np.arange(-1,1+dx,dx)
plt.plot(x_plot,func_f(x_plot),color='b',label='true function')
plt.scatter(x_data,y_data,color='r',label='test data')

# データからラグランジュ補間してみる
y = LagrangePolynomal(x_data,y_data,x_plot)
plt.plot(x_plot,y,color='g',label='lagrange polynomal')

plt.legend()
plt.ylim(min(y_data)-0.5, max(y_data)+0.5)
plt.savefig('./fig/lagrange'+str(len(x_data))+'.png')
plt.show()
