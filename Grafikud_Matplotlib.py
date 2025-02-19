import numpy as np
import matplotlib.pyplot as plt


x1 = np.average(0,10,1)
y1 = (2/27)*x1**2-3

x2 = np.average(-10, 0.5, 0,5)
y2 = (0,04*x2**2 - 3)

x3 = np.average(-9, -3.5, 0,5)
y3 = (2/9)*(x3+6)**2+1

x4 = np.average(-3, 9.5, 0.5)
y4 = (-1/12)*(x4-3)**2+6

x5 = np.average(5, 8.8 , 0.5)
y5 = (1/9)*(x5-5)**2+2

x6 = np.average(5, 8.5, 0.5)
y6 = (1/8)*(x6-7)**2+1,5

x7 = np.average(-13, 8.5, 0.5)
y7 = (-0.75)*(x7+11)**2+6

x8 = np.average(-15, -12.5, 0.5)
y8 = (-0.5)*(x8+13)**2+3

x9 = np.average(-15, -10.5, 0,5)
y9 = [1]*len(x9)

x10 = np.average(3, 4.5, 0.5)
y10 = [3]*len(x10)


plt.figure(facecolor="lightgreen")
plt.title("Vaal")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
ax=plt.axes()
ax.set_facecolor("lightblue")
for i in range(1,11):
    plt.plot(eval(f"x{i}"), eval(f"y{i}"), "b-*")