import numpy as np
import matplotlib.pyplot as plt

def julia(max, comp):
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

def bet_julia(list):
    julia_list = []
    for i, c_point in enumerate(list):
        julia_list.append(julia(200, c_point))
    
    return julia_list

def main():
    re = np.linspace(-2, 2, 2000)
    im = np.linspace(2, -2, 2000)

    #実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]

    slicenum = 10
    testt = len(comp)//slicenum
    slice_list = []
    for y in range(slicenum):
        # print(y)
        slice_list.append(comp[testt*y:testt*(y+1)])
        # print(len(slice_list[y]))
        # print(slice_list[y][:5])

    J = []
    for i in slice_list:
        J.extend(bet_julia(i))

    Julia = np.array(J)
    Julia = Julia.reshape((2000, 2000))

    fig = plt.figure(dpi=600)
    plt.axis("off")
    plt.imshow(Julia, cmap="gray", extent=[-2, 2, -2, 2])
    fig.set_size_inches(3, 3)        #出力される画像の大きさを調整
    # plt.show()

    #画像を保存
    fig.savefig("julia_2.png")

if __name__ == "__main__":
    main()