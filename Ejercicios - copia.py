import numpy as np
import cv2
import os




class colorImage:
    def __init__(self):
        self.path = 'C:/Users/Juan Sebastian/Documents/Pontificia Universidad Javeriana/Decimo Semestre/Procesamiento de Imagenes'
        nombre='fondo.jpg'
        path_file= os.path.join(self.path, nombre)
        self.image=cv2.imread(path_file)
        cv2.imshow('Imagen a Color', self.image)
        cv2.waitKey(0)

    def displayProperties(self):
        self.camino = 'C:/Users/Juan Sebastian/Documents/Pontificia Universidad Javeriana/Decimo Semestre/Procesamiento de Imagenes'
        self.nombre = 'fondo.jpg'
        path_file = os.path.join(self.camino, self.nombre)
        self.imagen = cv2.imread(path_file)
        height, width, channels = self.imagen.shape
        print("El largo es: ", height)
        print("El ancho es: ", width)

    def makeGray(self):
        self.path = 'C:/Users/Juan Sebastian/Documents/Pontificia Universidad Javeriana/Decimo Semestre/Procesamiento de Imagenes'
        nombre='fondo.jpg'
        path_file= os.path.join(self.path, nombre)
        self.image=cv2.imread(path_file, 0)
        cv2.imshow('Escala de Grises', self.image)
        cv2.waitKey(0)
    def colorizeRGB(self):
        self.eleccion= input("Ingrese el color que quiere la Imagen")
        print("El color elegido es: ", self.eleccion)
        self.path = 'C:/Users/Juan Sebastian/Documents/Pontificia Universidad Javeriana/Decimo Semestre/Procesamiento de Imagenes'
        nombre='fondo.jpg'
        path_file= os.path.join(self.path, nombre)
        self.image =  cv2.imread(path_file)
        self.imager=  cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        C1 = self.imager[255:,:,0]
        C2 = self.imager[2:,:,1]
        C3 = self.imager[3:,:,2]

        if self.eleccion=='red':
            cv2.imshow('Rojiza', C1)
            cv2.waitKey(0)
        else:
            if self.eleccion=='green':
            cv2.imshow('Verdoza', C2)

            else:
            cv2.imshow('Azul', C3)




x=colorImage()
x.displayProperties()
x.makeGray()
x.colorizeRGB()

