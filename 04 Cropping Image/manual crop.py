import cv2 

image = cv2.imread("04 Cropping Image\\botol.jpg")
cv2.imshow("Image",image)

#Cropping Image
#Array Image -> (Height, Width)
#Untuk cropping image -> (min height:max height, min width : maxwidth)
#Jika terjadi overflow pada array, maka akan diambil nilai semula pada image asli

minHeight = 0
maxHeight = 100
minWidth = 0
maxWidth = 100

cropping_image = image[minHeight:maxHeight,minWidth:maxWidth]

cv2.imshow("Cropped Image", cropping_image)

cv2.waitKey(0)