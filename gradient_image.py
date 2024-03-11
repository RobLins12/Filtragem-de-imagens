import numpy as np
import cv2 as cv
import sys

# O código a seguir mostra como aplicar filtros de realce usando open cv
# Leitura da imagem e conversão para monocromática

img = cv.imread("c:/Users/aluno/Downloads/erik-jan-leusink-IbPxGLgJiMI-unsplash-scaled.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

while True:
    ch = cv.waitKey()
    if ch == 27:
        sys.exit()
        
    # Gradiente normal
    
    kernel_x = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, -1, 0]])
    
    kernel_y = np.array([[0, 0, 0],
                         [0, 1, -1],
                         [0, 0, 0]])
    
    grad_x = cv.filter2D(gray, -1, kernel_x)
    grad_y = cv.filter2D(gray, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv.imshow('Normal', gray)
    
    # Gradiente de Roberts
    
    kernel_x = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, -1]])
    
    kernel_y = np.array([[0, 0, 0],
                         [0, 0, 1],
                         [0, -1, 0]])
    
    grad_x = cv.filter2D(gray2, -1, kernel_x)
    grad_y = cv.filter2D(gray2, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray2 = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv.imshow('Roberts', gray2)
    
    # Gradiente de Sobel
    
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    
    grad_x = cv.Sobel(gray3, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray3, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv.imshow('Sobel', grad)
