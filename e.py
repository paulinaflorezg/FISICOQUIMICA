#TRABAJO DE PAULINA FLOREZ GARCIA Y PAULINA OROZCO RUIZ
import numpy as np
import math
import matplotlib.pyplot as plt

m_O2 = 4.65 * 10 ** -26       # Masa de una molecula de oxígeno, en kg

k_B = 1.38e-23                # Constante de Boltzamann en Joules/Kelvin

T1 = 500                  # Temperatura en Kelvin

v = np.arange(10, 3000, 20)

n_O2T1 = 4 * math.pi * (m_O2 / (2 * math.pi * k_B * T1)) ** (3 / 2) * (v**2) * np.exp(-m_O2 * v** 2 / (2 * k_B * T1))






plt.plot(v, n_O2T1, label = " TEMPERATURA BAJA")

plt.plot(v, n_O2T2, label = "TEMPERATURA MEDIA")

plt.plot(v, n_O2T3, label = "TEMPERATURA ALTA")



plt.xlabel('Velocidad (m/s)')                                # Título en el eje horizontal
plt.ylabel('n(v)')                                              # Título en el eje vertical

plt.title('Distribución de Velocidad de Maxwell-Boltzmann')     # Título para la gráfica
plt.legend()                                                    # Leyenda
plt.show()                                                      # Mostrar gráfica
