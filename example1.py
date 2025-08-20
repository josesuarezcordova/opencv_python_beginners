#Import the library cv2
import cv2

#Create the path variable
img_path = 'img/r0_0.jpg'

#Create a variable to load the original image
img_original = cv2.imread(img_path)

img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

#Create a variable to show the image on a window named 'Red Apple Original Color'
cv2.imshow('Red Apple Original Color', img_original)

cv2.imshow('Red Apple Gray Color', img_gray)

#Wait until press any Key
cv2.waitKey(0)

#Destroy all Windows opened
cv2.destroyAllWindows()
