import cv2, time , pandas
import numpy as np
from datetime import datetime
import pandas
video = cv2.VideoCapture(0)
global df
def take_a_pic():
    video = cv2.VideoCapture(0)
    time.sleep(1)
    check, frame = video.read()
    frame = cv2.resize(frame, (int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (19, 19), 0)
    video.release()
    return frame

first_frame = take_a_pic()
global lst
lst = [None,None]
time = []


def draw_boundary():
    while True:
        status = 0

        check, frame = video.read()

        frame = cv2.resize(frame, (int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5)))
            # print(check)
            # print(frame)
            # print(frame.shape)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        grayblured = cv2.GaussianBlur(gray,(19,19),0)
        delta =cv2.absdiff(first_frame, grayblured)
        thresh_delta = cv2.threshold(delta, 40, 255, cv2.THRESH_BINARY)[1]  #threshold(src, thresh, maxval, type[, dst]) -> retval, dst
        dilated_image = cv2.dilate(thresh_delta, None, iterations=2)
        #findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> contours, hierarchy  retrieves only the extreme outer contours.

        cnts = cv2.findContours(dilated_image,mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)[0]
        for contour in cnts:
            cv2.drawContours(frame,  contour, -1, (255, 255, 0), 3)            # if cv2.contourArea(contour) < 1000:
            if cv2.contourArea(contour) < 10000:
                continue
            status = 1
            (x,y,w,h) =cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
        lst.append(status)
        if lst[-1] == 1 and lst[-2] == 0:
            time.append(datetime.now())
        if lst[-1] == 0 and lst[-2] == 1:
            time.append(datetime.now())

        cv2.imshow("original", frame)
        # cv2.imshow("difference", delta)
        # cv2.imshow("thresh",thresh_delta)
        cv2.imshow("dilated_frame", dilated_image)
        key = cv2.waitKey(1)
        if key == ord("q") or key == 27:
            if status == 1:
                time.append(datetime.now())
            break
        print(status)


def main():

    draw_boundary()

    print(lst)
    print(time)
    df = pandas.DataFrame(columns=["start", "End"])

    for i in range(0, len(time), 2):
        df = df.append({"start": time[i], "End": time[i + 1]}, ignore_index=True)
    df.to_csv("times.csv")

if __name__ == '__main__':
    main()


video.release()
cv2.destroyAllWindows()