import cv2

capture = cv2.VideoCapture(0)

formatVideo = cv2.VideoWriter.fourcc("H264")

saveCapture = cv2.VideoWriter("test.mp4",formatVideo, 20, (320,240)) #nama file, format video, fps, size

if not capture.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        ret, frame = capture.read()

        if ret:
            saveCapture.write(frame)
            cv2.imshow("Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read frame from webcam.")
            break

    capture.release()

    cv2.destroyAllWindows()

# cap.set() function
# CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
# CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# CAP_PROP_POS_AVI_RATIO Relative position of the video file
# CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# CAP_PROP_FPS Frame rate.
# CAP_PROP_FOURCC 4-character code of codec.
# CAP_PROP_FRAME_COUNT Number of frames in the video file.
# CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# CAP_PROP_SATURATION Saturation of the image (only for cameras).
# CAP_PROP_HUE Hue of the image (only for cameras).
# CAP_PROP_GAIN Gain of the image (only for cameras).
# CAP_PROP_EXPOSURE Exposure (only for cameras).
# CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# CAP_PROP_WHITE_BALANCE Currently unsupported
# CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)