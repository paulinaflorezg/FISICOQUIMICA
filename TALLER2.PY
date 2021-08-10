#PAULINA FLOREZ GARCIA Y PAULINA OROZCO RUIZ

import numpy as np
import matplotlib.pyplot as plt

c = 2
n = 6       
R = 8.314            
Ti = 400
Vi = 2        
Vf = 10              
V = np.arange (10,500,20)

W1 = R*Ti*n*np.log(V) - R*Ti*n*np.log(Vi)
W2 = -R*V*c*n + R*Vi*c*n + R*n*(Ti + Vi*c)*np.log(V) - R*n*(Ti + Vi*c)*np.log(Vi)

plt.plot(V, W1 ,label ="W1")
plt.plot(V, W2 ,label ="W2")
plt.xlabel('volumen(m^3)')
plt.ylabel('trabajo')
plt.title('comparacion de trabajos')
plt.legend()
plt.show()

