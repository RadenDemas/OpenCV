from ultralytics import YOLO
import cv2
import time
import torch

# Load a model
model = YOLO("yolo11x-cls.pt")  # load an official model
model = YOLO("runs\\classify\\train\\weights\\best.pt")  # load a custom model

prev_time = time.time()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    result = model(frame)
    
    
    # current_time = time.time()
    # fps = 1 / (current_time - prev_time)
    # prev_time = current_time
    # cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), 
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    
    object = result[0].probs.data
    object = torch.argmax(object)
    
    cv2.putText(frame, f"Object: {result[0].names[object.item()]}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
    
    cv2.imshow("Real-time Classification", frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()