import cv2 as cv
img = cv.imread('cat.jpg')
cv.imshow('The Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
