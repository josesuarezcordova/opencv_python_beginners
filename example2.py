import cv2

img_path = 'img/r0_0.jpg'

img_original = cv2.imread(img_path)

print('data type:', img_original.dtype)
print('image shape:', img_original.shape)
print('image size:', img_original.size)


