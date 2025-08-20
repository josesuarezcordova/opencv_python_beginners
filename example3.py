#Import the library cv2
import cv2

#Create the path variable
img_path = 'img/r0_0.jpg'

#Create a variable to load the original image
img_original = cv2.imread(img_path)

#Convert the image from BGR to RGB
img_RGB = cv2.cvtColor(img_original,cv2.COLOR_BGR2RGB)

#Show the image converte to confirm changes
cv2.imshow('Imagen RGB', img_RGB)

#Wait until a key pressed
cv2.waitKey(0)

#Close all the windows opened
cv2.destroyAllWindows()

#Save it as new image on the folder img/
cv2.imwrite("img/newimage_RGB.jpg", img_RGB)