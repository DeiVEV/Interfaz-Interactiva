import numpy
import pygame 
import tkinter as tk
from tkinter import ttk
from turtle import right, width
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class FractalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Fractales")
        self.geometry("800x600")
        
        #Crear un área para la visualización del fractal
        self.fractal = Figure(figsize=(6, 5), dpi=100)
        self.fractalCanvas = FigureCanvasTkAgg(self.fractal, master=self)
        self.fractalCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #Controles para seleccionar el tipo de fractal 
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        self.tipofractal = tk.StringVar()
        opciFractal = ["Mandelbrot", "Julia", "Helecho de Barnsley"]
        dropFractal = ttk.Combobox(control_frame, textvariable=self.tipofractal, values=opciFractal, state="readonly")
        dropFractal.current(0)
        dropFractal.pack(side=tk.LEFT, padx=5)
        
        generarBoton = ttk.Button(control_frame, text="Generar", command=self.generar_fractal)
        generarBoton.pack(side=tk.LEFT, padx=5)
    
    def generar_fractal(self):
        tipoFractal = self.tipofractal.get()
        if tipoFractal == "Mandelbreot":
            self.generar_Mandelbrot()
        elif tipoFractal == "Julia":
            self.generar_Julia()
        elif tipoFractal == "Helecho de Barnsley":
            self.generar_Barnsley()
        
        pass
    
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
    
def generar_Julia(self):
# Definimos las dimensiones de la imagen (ancho x alto)


ancho = 800
alto = 600
iterations = 200

# Creamos una imagen en blanco con las dimensiones especificadas
image = np.zeros((ancho, alto))

# Definimos los parámetros para el conjunto de Julia
c = complex(-0.8, 0.156)

# Iteramos sobre cada pixel de la imagen
for x in range(ancho):
    for y in range(alto):
        zx, zy = 1.5*(x - ancho/2)/(0.5*ancho), 1.0*(y - alto/2)/(0.5*alto)
        for i in range(iterations):
            if zx*zx + zy*zy > 4.0: break 
            tmp = zx*zx - zy*zy + c.real
            zy, zx = 2.0*zx*zy + c.imag, tmp
        # El color del pixel depende del número de iteraciones
        image[y, x] = i

# Mostramos la imagen
plt.imshow(image, cmap='viridis')
plt.show()

pass

def generar_helecho_Barnsley(self):
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
pass