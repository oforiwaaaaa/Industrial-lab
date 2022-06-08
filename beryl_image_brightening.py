#initialize the needed libraries
import cv2
import numpy

#read an image from the computer and name it as old
old = cv2.imread(r'Beryl.jpg')

#duplicate the original image and name it as new
new= old.copy()

#display old image in a windows called Beryl
cv2.imshow('Beryl', old)
while True:
    #close Beryl window if key B is pressed
    if cv2.waitKey(1) == ord("b"):
        break

 #set the brighness parameters for alpha and beta
alpha = 1.7
beta = 0
#adjust the old image to show the set parameters
new = cv2.convertScaleAbs(new, alpha=alpha, beta=beta)

#display the new image
cv2.imshow('birght Beryl',new)
while True:

#close all windows after displaying the new image
    if cv2.waitKey(2) == ord("b"):
        cv2.destroyAllWindows()
        break
