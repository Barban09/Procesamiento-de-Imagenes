import Taller2
import cv2


if __name__ == '__main__':
#Script el cual es utilizado para el punto 4 del taller
    x=Taller2.ImageShape() #Se le pide al usuario las dimensiones de la imagen
    x.GenerateShape()      #Se genera la figura
    x.showShape()          #Se muestra la figura generada
    clasifimagen=x.getShape()
    print("La Figura generada es un", clasifimagen)  #Se imprime el tipo de figura
    cv2.destroyAllWindows()
    resultimagen=x.WhatShape()      #Se muestra la imagen ingresada por el usuario y el tipo de figura que es
    print("La Figura del usuario es", resultimagen)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
