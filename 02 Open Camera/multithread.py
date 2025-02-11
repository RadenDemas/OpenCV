import cv2
import threading
import time

class VideoCaptureThread:
    def __init__(self, src=0, width=640, height=480):
        # Gunakan DirectShow (khusus Windows) atau backend lain sesuai kebutuhan
        self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.grabbed, self.frame = self.cap.read()
        self.running = True
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                self.running = False
                break
            self.frame = frame

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()

# Inisialisasi capture menggunakan thread
cap_thread = VideoCaptureThread(0)
prev_time = time.time()
while True:
    frame = cap_thread.read()
    if frame is None:
        continue  # Jika frame belum siap, lewati iterasi
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_thread.stop()
cv2.destroyAllWindows()
