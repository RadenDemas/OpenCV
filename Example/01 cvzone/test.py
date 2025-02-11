from cvzone.ClassificationModule import Classifier
import cv2
import time

cap = cv2.VideoCapture(0)# Initialize video capture
cap.set(cv2.CAP_PROP_FPS,60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
path = "model\\"
maskClassifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')
prev_time = time.time()
while True:
    _, img = cap.read()  # Capture frame-by-frame
    prediction = maskClassifier.getPrediction(img)
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, f"FPS: {fps:.2f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Wait for a key press