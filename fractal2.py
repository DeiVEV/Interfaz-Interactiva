# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definimos las dimensiones de la imagen (ancho x alto)
width = 800
height = 800
iterations = 200

# Creamos una imagen en blanco con las dimensiones especificadas
image = np.zeros((width, height))

# Definimos los parámetros para el conjunto de Julia
c = complex(-0.8, 0.156)

# Iteramos sobre cada pixel de la imagen
for x in range(width):
    for y in range(height):
        zx, zy = 1.5*(x - width/2)/(0.5*width), 1.0*(y - height/2)/(0.5*height)
        for i in range(iterations):
            if zx*zx + zy*zy > 4.0: break 
            tmp = zx*zx - zy*zy + c.real
            zy, zx = 2.0*zx*zy + c.imag, tmp
        # El color del pixel depende del número de iteraciones
        image[y, x] = i

# Mostramos la imagen
plt.imshow(image, cmap='viridis')
plt.show()
