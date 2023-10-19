import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')

cv.imshow('cat',img)

cv.waitKey(0)

print('Hello')