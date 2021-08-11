# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool
from contextlib import closing

def julia(comp):
    max = 200
    re, im = comp[0], comp[1]
    #実部が-0.7、虚部が-0.3の複素数cを作成(ここの数値を変えればさまざまなジュリア集合を作れる)
    c = complex(-0.7, -0.3)

    #実部がre、虚部がimの複素数zを作成
    z = complex(re, im)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            return i        #発散する場合には何回目のループで終わったかを返す
    
    return max     #無限大に発散しない場合にはmaxを返す
def main():
    t1 = time.time()   #実行時間測定開始
    
    re = np.linspace(-2, 2, 1000)
    im = np.linspace(2, -2, 1000)
    
    #実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]
    
    #計算結果を格納するための零行列を作成
    Julia = np.zeros(len(comp))
    
    
    
    
    #マンデルブロ集合に属するかの計算
    #Pool
    with closing(Pool(processes=4)) as p:
    	x = p.map(func=julia, iterable=comp)
    
    for i in range(len(x)):
        Julia[i] = x[i]
 
    Julia = Julia.reshape((1000, 1000))
    
    fig = plt.figure(dpi=200)
    plt.axis("off")
    plt.imshow(Julia, cmap="bone", extent=[-2, 2, -2, 2])
    fig.set_size_inches(3, 3)        #出力される画像の大きさを調整
    plt.show()
    
    #画像を保存
    fig.savefig("julia.png")
    
    t2 = time.time()  #実行時間測定終了
    
    elapsed_time = t2 -t1
    print("経過時間：{0}".format(elapsed_time))
    
if __name__ == "__main__":
    main()
    
    
    