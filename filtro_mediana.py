import numpy as np
import cv2 as cv
import sys

def main():
    
    img = cv.imread('/workspace/Filtragem-de-imagens/imagens1/peppers_gray_ruido.bmp')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27: #esc
            break

        medianBlur = cv.medianBlur(img, 3)
  
        # Showing the image 
        cv.imshow('Original', img) 
        cv.imshow('Median blur', medianBlur) 

        # In loop medianBlur
        for i in range(3):
            medianBlur = cv.blur(medianBlur, 3)
            cv.imshow('Median blur ' + str(i), medianBlur) 

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

