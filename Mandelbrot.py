import numpy as np
import matplotlib.pyplot as plt



def main():
    x = np.linspace(-2, 1, 1000)
    y = np.linspace(-1.5, 1.5, 1000)
    xx_start, yy_start = np.meshgrid(x, y, indexing='ij')
    M_set = np.zeros_like(xx_start)
    xx = np.copy(xx_start)
    yy = np.copy(yy_start)

    for i in range(100):
        xx_1 = xx**2-yy**2+xx_start
        yy_1 = 2*xx*yy+yy_start
        xx = xx_1
        yy = yy_1

        M_set[(xx**2+yy**2)<2] += 1
        xx[(xx**2+yy**2)>2] = 10
        yy[(xx**2+yy**2)>2] = 5


    plt.imshow(M_set, origin='lower')
    plt.colorbar()
    plt.show()





if __name__ == "__main__":
    main()
