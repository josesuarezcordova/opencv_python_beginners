#Import the libraries
import cv2
import os

#Create the path variable
img_path = 'img/shapes.png'

#Verify if Image exist
if os.path.exists(img_path):

	#variable to read the image
	img_ = cv2.imread(img_path)

	#Set the range for the shape required
	red_circle = img_[10:185, 10:192]

	#load image on a Window
	cv2.imshow('Image2',red_circle)

	#Wait until a key pressed
	cv2.waitKey(0)

	#Close all the windows opened
	cv2.destroyAllWindows()

	#Save it as new image on the folder img/
	cv2.imwrite("img/red_circle.jpg", red_circle)

else:
	print('Image could not be read')
