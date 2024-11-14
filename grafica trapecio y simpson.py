import matplotlib.pyplot as plt
import numpy as np

# Datos del ejercicio
t = [0, 1, 2, 3, 4, 5, 6, 7]
v = [0, 14, 39, 69, 95, 114, 129, 139]

# Cálculo de la distancia con el método del Trapecio
distancia_trapecio = (1/2) * (v[0] + v[-1] + 2 * sum(v[1:-1]))

# Cálculo de la distancia con el método de Simpson
distancia_simpson = (1/3) * (v[0] + v[-1] + 4 * sum(v[1::2]) + 2 * sum(v[2::2]))

print(f"Distancia por método del Trapecio: {distancia_trapecio:.2f} m")
print(f"Distancia por método de Simpson: {distancia_simpson:.2f} m")

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, v, 'o-', color='blue', label='Velocidad')
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Velocidad (m/s)')
ax.set_title('Gráfica de Velocidad vs Tiempo')
ax.legend()

# Agregar líneas verticales para marcar los puntos de datos
for i in t:
    ax.axvline(x=i, color='gray', linestyle='--', alpha=0.5)

plt.show()