import numpy as np
import cv2 as cv
import sys

# O código a seguir mostra como fazer uma operação de convolução usando open cv
# Leitura da imagem e conversão para monocromática

img = cv.imread("c:/Users/aluno/Downloads/gato-siames.jpg")
img = cv.resize(src=img, dsize=None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

while True:
    ch = cv.waitKey()
    if ch == 27:
        sys.exit()
        
    #  Gradiente de Prewitt
    
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    
    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])
    
    grad_x = cv.filter2D(gray, -1, kernel_x)
    grad_y = cv.filter2D(gray, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv.imshow('Prewitt', gray)

    # Operação de convolução

    kernel_x = cv.flip(kernel_x, 1)
    kernel_y = cv.flip(kernel_y, 0)
    
    print(kernel_x)
    print(kernel_y)

    grad_x = cv.filter2D(gray2, -1, kernel_x)
    grad_y = cv.filter2D(gray2, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray2 = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv.imshow('Prewitt on convolution', gray2)