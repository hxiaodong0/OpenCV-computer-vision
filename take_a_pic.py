import cv2, time

def take_a_pic():
    first_frame = None
    video = cv2.VideoCapture(0)
    time.sleep(2)
    check, frame = video.read()
    frame = cv2.resize(frame, (int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5)))
    video.release()
    return frame

cv2.imshow("test",take_a_pic())
key = cv2.waitKey()
cv2.destroyAllWindows()