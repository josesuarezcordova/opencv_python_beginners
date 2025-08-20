#Import the library cv2
import cv2

#Create the path variable
img_path = 'img/frutas.jpg'

#variable to read the image
img_ = cv2.imread(img_path)

#if condition returns False, AssertionError is raised:
assert img_ is not None, "file could not be read"

#array color [B,G,R]
RED = [0,0,255]

#applying border to image read
border_constant= cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_CONSTANT,value=RED)
border_reflect = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REFLECT)
border_replicate = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REPLICATE)
border_reflect101 = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REFLECT_101)
border_wrap = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_WRAP)

#Show the original image
cv2.imshow('Original',img_)

#Show the image with border
cv2.imshow('Border Constant',border_constant)
cv2.imshow('Border Reflect',border_reflect)
cv2.imshow('Border Replicate',border_replicate)
cv2.imshow('Border Reflect 101',border_reflect101)
cv2.imshow('Border Wrap',border_wrap)

#Wait until press any key
cv2.waitKey(0)

#Destroy all Windows opened
cv2.destroyAllWindows()



# cv2.imshow('Replicate',replicate)
# cv2.imshow('Reflect',reflect)
# cv2.imshow('Wrap',wrap)


# replicate = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img_,20,20,20,20,cv2.BORDER_WRAP)