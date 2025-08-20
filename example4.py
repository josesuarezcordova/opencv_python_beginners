#Import the library cv2
import cv2
import os

#Create the path variable
img_path = 'img/r0_0.jpg'

#This conditional load and show the image if exist
if os.path.exists(img_path):
	
	#variable to read the image
	img_ = cv2.imread(img_path)
	
	#Change the color of a pixel
	img_[100,100] = [255,255,255]
	
	#Loop number of rows of image
	for i, row in enumerate(img_):

		#change the color of pixels on the range 
		# y=i, x = 100 
		img_[i,100] = [255,255,255]

	#Show the image readed
	cv2.imshow('Image',img_)

	#Wait until a key pressed
	cv2.waitKey(0)

	#Close all the windows opened
	cv2.destroyAllWindows()
else:
	print('Image could not be read')



