import cv2
import imutils

image = cv2.imread("05 Resize Image\\botol.jpg")

height, width = 256, 256

#using cv2 resize
imageResizeCv2 = cv2.resize(image, (height,width), interpolation=cv2.INTER_AREA)

#using imutils
imageResizeImutils = imutils.resize(image, height = height)
cv2.imshow("Resize OpenCV",imageResizeCv2)
cv2.imshow("Resize Imutils",imageResizeImutils)
cv2.waitKey(0)


#Standart Interpolation for resizing in openCV
# cv2.INTER_NEAREST : This is using a nearest-neighbor interpolation to shrink an image.
# cv2.INTER_LINEAR : This is primarily used when larging is required (default).
# cv2.INTER_AREA : This is used when we need need to shrink an image.
# cv2.INTER_CUBIC : This is slow for larging image, but more efficient (higer quality).