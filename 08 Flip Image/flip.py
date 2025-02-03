import cv2

image = cv2.imread("08 Flip Image\\botol.jpg")

flipHorizontal = cv2.flip(image,1)
flipVertical = cv2.flip(image,0)
flipBothDirection = cv2.flip(image,-1)

cv2.imshow("Original", image)
cv2.imshow("Flip Horizontal",flipHorizontal)
cv2.imshow("Flip Vertical",flipVertical)
cv2.imshow("Flip Both",flipBothDirection)

cv2.waitKey(0)