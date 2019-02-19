import cv2
import numpy as np

img = cv2.imread('lena.png', 0)
toSave=np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)

sum=0
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		sum = sum + img[i][j]

avg = sum / (img.shape[0] * img.shape[1])

print ("Mean pixel intensity:", avg)

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if (img[i][j]>avg):
			toSave[i][j]=1*255
		else:
			toSave[i][j]=0*255
	
cv2.imwrite("binImage.png", toSave)
cv2.imshow('binImage', toSave)
cv2.waitKey(0)
cv2.destroyAllWindows()