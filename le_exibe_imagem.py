import numpy as np
import cv2 as cv
import sys

def main():
    
    img = cv.imread('c:/Users/Administrador/Downloads/fruits.png')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27:
            break

        averageBlur = cv.blur(img, (3, 3)) 
        medianBlur = cv.medianBlur(img, 3)
  
        # Showing the image 
        cv.imshow('Original', img) 
        cv.imshow('Average blur', averageBlur) 
        # cv.imshow('Median blur', medianBlur) 

        for i in range(3):
            averageBlur = cv.blur(averageBlur, (3, 3)) 
            cv.imshow('Average blur ' + str(i), averageBlur) 

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

