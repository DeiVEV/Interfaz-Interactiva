# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definimos las dimensiones de la imagen (ancho x alto)
width = 800
height = 800

# Creamos una imagen en blanco con las dimensiones especificadas
image = np.zeros((width, height))

# Definimos los parámetros para el Helecho de Barnsley
f1 = lambda x, y: (0., 0.16*y)
f2 = lambda x, y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
f3 = lambda x, y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
f4 = lambda x, y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
fs = [f1, f2, f3, f4]

# Inicializamos las variables x e y
x, y = 0, 0

# Iteramos sobre cada pixel de la imagen
for i in range(100000):
    f = np.random.choice(fs, p=[0.01, 0.85, 0.07, 0.07])
    x, y = f(x,y)
    ix, iy = int(width / 2 + x * width / 10), int(y * height / 12)
    image[iy, ix] = 1

# Mostramos la imagen
plt.imshow(image[::-1, :], cmap='Greens')
plt.show()
