import numpy as np
from PIL import Image
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
        self.imagen = self.image
        height, width, channels = self.imagen.shape
        self.image=cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)
        self.nuevaimg=self.image
        C1=self.nuevaimg[:,:,0]
        C2=self.nuevaimg[:,:,1]
        C3=self.nuevaimg[:,:,2]

        if self.eleccion=='blue':
            C2 = 0
            C3 = 0
            cv2.imshow("Hola", self.nuevaimg)
            cv2.waitKey(0)

        if self.eleccion=='red':
            C1 = 0
            C2 = 0
            cv2.imshow("Hola", self.nuevaimg)
            cv2.waitKey(0)

        if self.eleccion == 'green':
            C1=0
            C3=0
            cv2.imshow("Hola", self.nuevaimg)
            cv2.waitKey(0)

    def makeHue(self):
        self.path = 'C:/Users/Juan Sebastian/Documents/Pontificia Universidad Javeriana/Decimo Semestre/Procesamiento de Imagenes'
        nombre = 'fondo.jpg'
        path_file = os.path.join(self.path, nombre)
        self.image = cv2.imread(path_file)
        self.imagen = self.image
        self.imagen=cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
        C1=self.imagen[:,:,0]=0
        C2=self.imagen[:,:,1]
        C3=self.imagen[:,:,2]
        self.imagen2=cv2.cvtColor(self.imagen, cv2.COLOR_HSV2RGB)
        cv2.imshow("Imagen Tonos Hue", self.imagen2)
        cv2.waitKey(0)

x=colorImage()
x.displayProperties()
x.makeGray()
x.colorizeRGB()
x.makeHue()
