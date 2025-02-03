import cv2

x_start,x_end,y_start,y_end = 0,0,0,0
def crop_image(event,x,y,flags,param): #-> parameter default dari cv2
    global x_start,x_end,y_start,y_end
    
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start,y_start,x_end,y_end = x,y,x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        x_end,y_end = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        croppedImage = image[y_start:y_end,x_start:x_end]
        cv2.imshow("Cropped Image", croppedImage)

image = cv2.imread("04 Cropping Image\\botol.jpg")
windowName = "Original Image"

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName,crop_image)

while True:
    cv2.imshow(windowName,image)
    if(cv2.waitKey(1) == ord('q')):
        break
    
cv2.destroyAllWindows