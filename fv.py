from cProfile import label
import numpy as np
import matplotlib.pyplot as plt



x1 = np.arange(-9, -1.5, 0.5)
y1 = (-1/8)*(x1+9)**2+8

x2 = np.arange(1,9.5,0.5)
y2 = (-1/8)*(x2-9)**2+8

x3 = np.arange(-9,-8.5,0.5)
y3 = 7*(x3+8)**2+1

x4 = np.arange(8,9.5,0.5)
y4 = 7*(x4-8)**2+1

x5 = np.arange(-8,-1.5,0.5)
y5 = (1/49)*(x5+1)**2

x6 = np.arange(1,8.5,0.5)
y6 = (1/49)*(x6-1)**2

x7 = np.arange(-8,-1.5,0.5)
y7 = (-4/49)*(x7+1)**2

x8 = np.arange(1,8.5,0.5)
y8 = (-4/49)*(x8-1)**2  

x9 = np.arange(-8,-2.5,0.5)
y9 = (1/3)*(x9+5)**2-7

x10 = np.arange(2,8.5,0.5)
y10 = (1/3)*(x10-5)**2-7

x11 = np.arange(-2,-1.5,0.5)
y11 = -2*(x11+1)**2-2

x12 = np.arange(1,2.5,0.5)
y12 = -2*(x12-1)**2-2

x13 = np.arange(-1,1.5,0.5)
y13 = -4*(x13**2)+2

x14 = np.arange(-1,1.5,0.5)
y14 = 4*(x14**2)-6

x15 = np.arange(-2,0.5,0.5)
y15 = -1.5*x15+2

x16 = np.arange(0,2.5,0.5)
y16 = 1.5*x16+2

plt.figure(facecolor="lightgreen")
plt.title("Liblikas")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
ax=plt.axes()
ax.set_facecolor("lightblue")

        #для каждой отдельно -> plt.plot(x1,y1, "r:o")
        # сделать разноцветной ->  

colors=["c" , "m" , "y" , "r" , "g" , "b", "w", "k", "k", "k", "c" , "m" , "y" , "r" , "g" , "b" ]

for i in range(1,17):
    plt.plot(eval(f"x{i}"), eval(f"y{i}"), colors[i-1]+"-*", label=f"Liblikas {i} osa")
    
plt.show()