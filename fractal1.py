import numpy 
import matplotlib.pyplot as plt

def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j 
    
    for i in range(max_iter):
        z = z*z + c 
        if(z.real*z.real + z.imag*z.imag) >= 4:
            return i 
        
    return max_iter

columnas = 2000
filas = 2000 

resultado = numpy.zeros([filas, columnas])
for filasIndex, Re in enumerate(numpy.linspace(-2, -1, num=filas)):
    for colunmasIndex, Im in enumerate(numpy.linspace(-1, 1, num=columnas)):
        resultado[filasIndex, colunmasIndex] = mandelbrot(Re, Im, 100)

plt.figure(dpi=100)
plt.imshow(resultado.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()