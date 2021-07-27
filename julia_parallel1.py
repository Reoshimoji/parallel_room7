from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt

def julia(max, comp):
    re, im = comp[0], comp[1]
    c = complex(-0.7, -0.3)
    z = complex(re, im)

    for i in range(max):
        z = z*z + c
        if abs(z) >= 2:
            return i
    
    return max

def bet_julia(list):
    julia_list = []
    for i, c_point in enumerate(list):
        julia_list.append(julia(200, c_point))
    
    return julia_list


def main():
    re = np.linspace(-2, 2, 2000)
    im = np.linspace(2, -2, 2000)

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
    
    with Pool(processes=4) as p:
        result_list = p.map(func=bet_julia, iterable=slice_list)
        # print(result_list)
    
    for i in result_list:
        J.extend(i)

    Julia = np.array(J)
    Julia = Julia.reshape((2000, 2000))
    fig = plt.figure(dpi=600)
    plt.axis("off")
    plt.imshow(Julia, cmap="gray", extent=[-2, 2, -2, 2])
    fig.set_size_inches(3, 3)
    # plt.show()

    fig.savefig("julia_2.png")
    

if __name__ == "__main__":
    main()