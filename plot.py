import numpy as np
import matplotlib.pyplot as plt


d = np.linspace(-2,16,300)
x,y = np.meshgrid(d,d)
plt.imshow( ((y>=2) & (2*y<=25-x) & (4*y>=2*x-8) & (y<=2*x-5)).astype(int) ,
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

x = np.linspace(0, 16, 2000)
# y >= 2
y1 = (x*0) + 0
# 2y <= 25 - x
y2 = (25-x)/2.0
# 4y >= 2x - 8
y3 = (2*x-8)/4.0
# y <= 2x - 5
y4 = 2 * x -5

plt.plot(x, 2*np.ones_like(y1))
plt.plot(x, y2, label=r'$y\leq25-x$')
plt.plot(x, y3, label=r'$y\geq 2x - 1$')
plt.plot(x, y4, label=r'$y\leq 2x-5$')
plt.xlim(0,16)
plt.ylim(0,11)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()