import numpy as np
import cv2 as cv
import sys

def main():
    
    img = cv.imread('imagens1/peppers_gray_ruido.bmp')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27: #esc
            break

        averageBlur = cv.blur(img, (3, 3)) 
  
        # Showing the image 
        cv.imshow('Original', img) 
        cv.imshow('Average blur', averageBlur) 

        # In loop blur
        for i in range(2):
            averageBlur = cv.blur(averageBlur, (3, 3)) 
            cv.imshow('Average blur ' + str(i), averageBlur) 

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
