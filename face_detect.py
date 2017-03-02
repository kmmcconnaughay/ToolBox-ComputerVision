"""This will grab video frames from the webcam and display them on screen"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #object that uses index to tell it how many cameras are
# being used

while True:
    # Capture frame by frame
    # if not cap.isOpened():
        # cap.open('/dev/video0')
        # print(cap.isOpened())
    read_correctly, frame = cap.read(0)
    assert read_correctly, "cap.read() failed"


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # waitKey displays the image for the specified number of ms
    if cv2.waitKey(10) & 0xFF == ord('q'): # clicking 'q' key will quit program
        break

# Release the capture when everything is done
"""cap.release() returns a boolean. If the frame has been read correctly, it
will be True."""
cap.release()
cv2.destroyAllWindows()
