import numpy as np
import matplotlib.pyplot as plt

# Parametrizamos la cuadrícula en el plano donde estará el gradiente y divergente del gradiente
# Ajuste de la cuadrícula para el gráfico de contorno
lim = 0.5
dx = 0.1                                                  # Definimos los deltas en x
dy = 0.1                                                  # Definimos los deltas en y
xr = np.arange(-lim, lim, dx)                             # Definición de valores en un rango para x
yr = np.arange(-lim, lim, dy)                             # Definición de valores en un rango para y

# Permite obtener una matriz con las coordenadas de los vectores creados
x, y = np.meshgrid (xr, yr, indexing = 'ij')

# No existe en numpy un comando para sacar el divergente. Se crea el código, una función para el operador divergente.
def divergence(f, h):                                # Comando de dos parámetros f: es la función vectorial y h nos permite definir los diferenciales
    num_dims = len(f)                                # Sacamos el número de elementos de la lista que representa a la función vectorial f. Aquí es igual a 2, es decir, 2D, x e y
    return np.ufunc.reduce(np.add, [np.gradient(f[i], h[i], axis=i) for i in range(num_dims)])
    
    # Desde un ciclo for se utiliza el comando np.gradient sobre cada componente x e y de la función vectorial f, para sacar derivadas,
    # respecto a x e y, luego se suman con np.add para obtener el divergente del gradiente o Laplaciano, pero reduciéndolo a
    # una dimensión (un escalar) usando el comando np.ufunc.reduce().

# Ejemplo:

# Definición de la función
z =x**3 + 4 +(x**2 + y**2) +2

gradx, grady = np.gradient (z, dx, dy)    # Sacamos el gradiente de la z = función

Fx  = gradx       # Componente del gradiente para x
Fy  = grady       # Componente del gradiente para y

F = [Fx, Fy]      # Gradiente en su forma vectorial con sus componentes
h = [dx, dy]      # Indicadores de diferenciales, respecto a x (i.e. dx) e y (i.e. dy)

g = divergence(F, h)   # Aplicamos el divergente sobre el gradiente, es decir, tomamos el Laplaciano para z = función

# "Adornos para la gráfica"
plt.pcolormesh(x, y, g, shading='nearest', cmap=plt.cm.get_cmap('coolwarm'))
plt.title("Gradiente y Laplaciano", size = 18)
plt.xlabel("X", size = 16,)
plt.ylabel("Y", size = 16)
cbar = plt.colorbar()
plt.quiver(x, y, Fx , Fy)
plt.show()