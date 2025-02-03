import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        ret, frame = capture.read()

        if ret:
            cv2.imshow("Webcam", frame)  

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read frame from webcam.")
            break
        
    capture.release()
    cv2.destroyAllWindows()
