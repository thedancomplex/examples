import cv2 as cv

imagePath = sys.argv[1]
cascPath = sys.argv[2]

faceCascade = cv.CasecascadeClassifier(cascPath)
image = cv.imread(imagePath)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale( gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv.cv.CV_HAAR_SCALE_IMAGE)
