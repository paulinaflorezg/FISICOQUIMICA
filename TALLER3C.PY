from re import X
from sympy.vector import CoordSys3D, gradient, divergence         # Permite llamar a los comando gradiente y divergente

# Para usar los comandos gradient y divergence de simpy es necesario crear un indicador de variable
v = CoordSys3D('v')

# Definimos la función usando el indicador v
z = (v. x) **4 + 4 +(v.x) **2 - (v.y) **2 -3
print("Nuestra función es:", z)
print("--------------------------")

# Sacamos gradiente y lo guardams en una variable
g = gradient(z)
print("El gradiente de nuestra función es:", g)                                                   # Imprimimos el gradiente
print("--------------------------")

# Sacamos el divergente del gradiente, lo que equivale sacar el Laplaciano de nuestra función
d = divergence(g)
print("El Laplaciano de nuestra función es:", d)           