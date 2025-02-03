import cv2
import imutils

image = cv2.imread("07 Rotate Image\\botol.jpg")

angleRotate = 90
rotatedImage = imutils.rotate(image=image, angle=angleRotate)

cv2.imshow("Image", image)
cv2.imshow("Rotated Image", rotatedImage)

cv2.waitKey(0)
