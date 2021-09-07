#MARIA PAULINA FLOREZ GARCIA Y PAULINA OROZCO RUIZ
#PUNTO 1
import numpy as np                                 
import matplotlib.pyplot as plt                   

# Función
def f(x, y):                                        
    return -x**4 + 4 +(x**2 - y**2) -3

x = np.linspace(-1, 1, 20)                      
y = np.linspace(-1, 1, 20)

x, y = np.meshgrid(x, y)                           
z = f(x, y)                                         

# Graficación
ax = plt.axes(projection='3d')                      # Definimos gráfica 3D
ax.set_xlabel("X")                                  # Título para el eje X
ax.set_ylabel("Y")                                  # Título para el eje Y
ax.set_zlabel("Z")                                  # Título para el eje Z
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')    
ax.set_title('Gráfico 3D')
plt.show()
