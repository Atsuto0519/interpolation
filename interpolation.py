#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# ラグランジュの補間法
def LagrangePolynomal(x_data,y_data,x_test):
    """
    概要:　   ラグランジュ補間したデータを返す関数
    @param x_data:離散データの入力
    @param y_data:離散データの出力
    @param x_test:補間するデータの総入力
    @return :補完したデータの総出力
    """

    # z_kを全て求める
    def calc_coe(x):
        z = np.ones([n])
        for k in range(n):
            for i in range(n):
                if (i != k):
                    z[k] *= (x - x_data[i])/(x_data[k] - x_data[i])
        return z

    # yを求める
    def calc_y(z):
        y = np.dot(y_data,z)
        return y


    n = len(x_data)
    # リストの大きさが等しければ続行
    if (n != len(y_data)):
        print("Error. (list size ummatch)")
        return -1

    # z_kを求める
    z = [calc_coe(i) for i in x_test]

    # 補間点のyを求める
    y = [calc_y(i) for i in z]

    return y
