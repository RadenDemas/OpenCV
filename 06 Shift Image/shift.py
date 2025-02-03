import cv2
import imutils

image = cv2.imread("06 Shift Image\\botol.jpg")

xShift,yShift = 50,50

shiftedImage = imutils.translate(image=image,x=xShift,y=yShift)

cv2.imshow("image", image)
cv2.imshow("Shifted Iamge", shiftedImage)

cv2.waitKey(0)