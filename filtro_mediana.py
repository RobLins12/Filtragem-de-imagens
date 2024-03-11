import numpy as np
import cv2 as cv
import sys

# O código a seguir mostra como aplicar o filtro da medina usando open cv

def main():
    
    img = cv.imread('imagens1/peppers_gray_ruido.bmp')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27: #esc
            break

        medianBlur = cv.medianBlur(img, 3)
  
        # Mostrando a imagem
        cv.imshow('Original', img) 
        cv.imshow('Median blur', medianBlur) 

        # Fazendo a operação em loop
        for i in range(2):
            medianBlur = cv.medianBlur(medianBlur, 3)
            cv.imshow('Median blur ' + str(i), medianBlur) 

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

