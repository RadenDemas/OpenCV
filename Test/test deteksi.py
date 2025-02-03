import cv2
import imutils
import numpy as np

imageBackground = cv2.imread("Test\\botol.jpg")
imageObject = cv2.imread("Test\\botol2.JPG")

imageBackgroundGray = cv2.cvtColor(imageBackground, cv2.COLOR_BGR2GRAY)
imageObjectGray = cv2.cvtColor(imageObject,cv2.COLOR_BGR2GRAY)

imageBackgroundGray = imutils.resize(image=imageBackgroundGray,width=560)
imageObjectGray = imutils.resize(image=imageObjectGray,width=560)

print(imageBackgroundGray.shape)
print(imageObjectGray.shape)

cv2.imshow("Background",imageBackgroundGray)
cv2.imshow("Object",imageObjectGray)

if not np.array_equal(imageBackgroundGray, imageObjectGray):
    print("Object Terdeteksi")
else:
    print("Tidak Ada Object Yang Terdeteksi")

# cv2.imshow("Background",imageBackground)
# cv2.imshow("Object",imageObject)

cv2.waitKey(0)