import cv2
import numpy as np
import math

img = cv2.imread('lena.png', 0)

maxv = 256

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		v = img[i][j]
		if (v < maxv * 0.125):
			v = 0
		elif (v < maxv * 0.25):
			v = maxv * 0.125
		elif (v < maxv * 0.375):
			v = maxv * 0.25
		elif (v < maxv * 0.5):
			v = maxv * 0.375
		elif (v < maxv * 0.625):
			v = maxv * 0.5
		elif (v < maxv * 0.75):
			v = maxv * 0.625
		elif (v < maxv * 0.875):
			v = maxv * 0.75
		else:
			v = maxv * 0.875
		img[i][j] = np.uint(v)

cv2.imwrite("q8.png", img)
cv2.imshow('q8', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
