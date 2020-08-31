from Ejercicios import colorImage
import numpy as np
from PIL import Image
import cv2
import os

colorImage.__init__().path=input("Introduzca la ruta que quiere: ")
colorImage.__init__().nombre=input("Introduzca el nombre de la imagen")
print("El ancho de un imagen es ", colorImage.displayProperties())
print("Su imagen en escala de grises ", colorImage.makeGray())
colorImage.colorizeRGB().eleccion='red'
print("Su imagen rojiza  ", colorImage.makeGray())
print("Sus tonos resaltados  ", colorImage.makeHue())


