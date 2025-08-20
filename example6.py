#Import the library cv2
import cv2
import os

#Create the path variable
img_path = 'img/red_fruits.jpg'

#Verify if Image exist
if os.path.exists(img_path):

	#variable to read the image
	img_ = cv2.imread(img_path)

	print(img_.shape)

	a = img_[190:417, 227:457]

	img_[190,227] = [0,0,0]
	img_[417,457] = [0,0,0]

	# img_[100:100, 200:200] = a

	#Show the image readed
	cv2.imshow('Image',img_)
	cv2.imshow('Image2',a)

	#Wait until a key pressed
	cv2.waitKey(0)

	#Close all the windows opened
	cv2.destroyAllWindows()
else:
	print('Image could not be read')