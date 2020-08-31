import numpy as np
from PIL import Image
import os
import cv2
import random
from math import sqrt

class ImageShape():
    def __init__(self):
        width =  int(input("Introduzca el ancho de la imagen: "))
        height = int(input("Introduzca el alto de la imagen: "))
        #Guarda los paramteros ingresados por el usuario
        self.width=width
        self.height=height
        if self.width>self.height:
            self.h=int(self.height/2)
        else:
            self.h=int(self.width/2)
        #Obtiene el menor de los numeros, los cuales son parametros de las figuras generadas
        self.w1=int(sqrt(self.h*self.h-int((self.h*self.h)/4)))

    def GenerateShape(self):
        self.img=cv2.imread("cuadro.png")
        self.a = random.randint(0, 3)                   #Generacion del numero aleatorio que define la figura
        self.dim = (self.width, self.height)
        self.imagenmod = cv2.resize(self.img, self.dim) #Redimensionamiento de la Ventana

        if self.a == 0:
            #Se dibujan las lineas del triangulo
            cv2.line(self.imagenmod,(int(self.width/2),int((self.height-self.w1)/2)),(int(self.width/2)+int(self.w1/2),(int((self.height-self.w1)/2)+self.w1)),(255,255,0),1)
            cv2.line(self.imagenmod,(int(self.width/2)+int(self.w1/2),int(self.height/2)+int(self.w1/2)),(int(self.width/2)-int(self.w1/2),int(self.height/2)+int(self.w1/2)),(255,255,0),1)
            cv2.line(self.imagenmod,(int(self.width/2)-int(self.w1/2),int(self.height/2)+int(self.w1/2)),(int(self.width/2),int((self.height-self.w1)/2)), (255,255,0),1)
            self.imagen=self.imagenmod

        if self.a == 1:
            # Se dibuja el cuadrado
            # Dimensiones del Cuadrado
            self.x=int((self.width-self.h)/2)
            self.y=int((self.height-self.h)/2)
            self.imagenmod=cv2.rectangle(self.imagenmod, (self.x, self.y), (self.x+self.h,self.y+self.h), (255,255,0), -1)
            M=cv2.getRotationMatrix2D((self.width//2,self.height//2),45,1)        #Rotaciond del cuadrado 45 grados
            self.imagen=cv2.warpAffine(self.imagenmod,M,(self.width,self.height)) #Almacena la imagen


        if self.a == 2:
            # Se dibuja el rectangulo
            # Dimensiones del Rectangulo

            self.log=int(self.width/4)
            self.alt=int(self.height/4)
            self.imagen=cv2.rectangle(self.imagenmod, (self.log, self.alt), (self.log+int(self.width/2), self.alt+int(self.height/2)), (255,255,0), -1) #Almacena la imagen


        if self.a == 3:
            # Se dibuja el Circulo
            # Dimensiones del Circulo

            self.rad=int(self.h/2)
            self.imagen = cv2.circle(self.imagenmod, ((int(self.width/2)), int(self.height/2)), self.rad, (255,255,0), -1) #Almacenamiento de la Imagen

    def showShape(self):

        cv2.imshow("Imagen Generada", self.imagen) #Se muestra la imagen en pantalla
        cv2.waitKey(5000) #Tiempo en el que se muestra la imagen

    def getShape(self):
        #Se clasifica la imagen generada por el numero en GenerateShape()

        if self.a == 0:
            self.resp="Triangulo"

        else:
            if self.a == 1:
                self.resp="Cuadrado"

            else:
                if self.a== 2:
                    self.resp="Rectangulo"

                else:
                    self.resp="Circulo"

        return self.resp  #Se devuelve el tipo de imagen

    def WhatShape(self):
        #Se le pide al usuario que ingrese la imagen, el path y el nombre
        self.path    = input("Ingrese el Path de su imagen: ")
        self.nombimg = input("Ingrese el nombre de su imagen: ")
        path_file= os.path.join(self.path, self.nombimg)
        self.imagenes=cv2.imread(path_file)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Transformacion a Escala de Grises
        self.image_gray = cv2.cvtColor(self.imagenes, cv2.COLOR_BGR2GRAY)

        #Binarización
        ret, self.Ibw_Cb = cv2.threshold(self.image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.Ibw_Cb = cv2.dilate(self.Ibw_Cb, None, iterations=1)
        self.Ibw_Cb = cv2.erode(self.Ibw_Cb, None, iterations=1)

        #Se dibuja el contorno de la imagen
        self.hola,self.contornos, = cv2.findContours(self.Ibw_Cb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        #Con este ciclo y las funciones adentro se cuenta el numero de vertices de la figura generada
        for i in self.hola:
            self.eps=0.01*cv2.arcLength(i, True)
            self.figura=cv2.approxPolyDP(i, self.eps, True)
            cv2.drawContours(self.imagenes, [self.figura], 0, (0, 255, 0), 2)
            x,y,w,h=cv2.boundingRect(self.figura)


        #Segun el numero de vertices se clasifica la figura ingresada por el usuario
        if(len(self.figura))==3:
            self.respuesta = 'Triangulo'

        else:
            if (len(self.figura))==4:

                if float(w/h)==1:
                    self.respuesta = "Cuadrado"

                else:
                    self.respuesta = "Rectangulo"
            else:
                self.respuesta = "Circulo"

        #Se devuelve el tipo de figura
        return self.respuesta


