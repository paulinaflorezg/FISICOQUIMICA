import numpy as np                                 
import matplotlib.pyplot as plt                   

dx = 0.1                                                 
dy = 0.1                                                 
xr = np.arange(-1, 1, dx)                                 
yr = np.arange(-1, 1, dy)                                 


x, y = np.meshgrid (xr, yr, indexing = 'ij')


z = -x**4 + 4 +(x**2 - y**2) -3

gradx, grady = np.gradient (z, dx, dy)

n = 10                                                    
l = np.array([0.0, 0.5, 1.0, 1.5, 2.0])                   

plt.contourf(x, y, z, n)                                
ax=plt.contour(x, y, z, levels = l, colors = 'k', linewidths = 1, linestyles = 'solid')   
plt.title("Gradiente", size = 18)
plt.xlabel("X", size = 16,)
plt.ylabel("Y", size = 16)
plt.quiver(x, y, gradx , grady)                          
plt.show()

