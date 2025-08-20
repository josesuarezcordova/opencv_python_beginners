#Import the library cv2
import cv2

#Create the path variable
img_path = 'img/rgb.png'

#variable to read the image
img_ = cv2.imread(img_path)

b,g,r = cv2.split(img_)

cv2.imshow('Blue channel',b)
cv2.imshow('Green channel',g)
cv2.imshow('Red channel',r)

original_img = cv2.merge((b,g,r))
cv2.imshow('Merged',original_img)

cv2.imwrite('img/blue_channel.jpg',b)
cv2.imwrite('img/green_channel.jpg',g)
cv2.imwrite('img/red_channel.jpg',r)

cv2.waitKey(0)

cv2.destroyAllWindows()






