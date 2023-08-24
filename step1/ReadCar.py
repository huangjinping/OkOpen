import cv2
import numpy as np


class ReadCar:
    def __init__(self):
        pass

    def onStart(self):
        print("on Read Car On Start")
        # self.onReadVideoRemoveBackground()
        # self.onHarrisPoint()
        self.onTomasiPoint()

    def onReadVideo(self):
        cap = cv2.VideoCapture('./res/video/shoushi.mp4')
        while cap.isOpened():
            ret, frame = cap.read();
            if ret is True:
                print(frame)
                cv2.imshow('frame', frame)
                c = cv2.waitKey(25)
                if c == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()

    def onReadVideoRemoveBackground(self):
        cap = cv2.VideoCapture('./res/video/shoushi.mp4')

        bs = cv2.createBackgroundSubtractorMOG2()

        while cap.isOpened():
            ret, frame = cap.read();
            if ret is True:
                # print(frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (3, 3), 5)
                fg_mask = bs.apply(blur)
                cv2.imshow('frame', frame)
                cv2.imshow("blur", blur)
                cv2.imshow("fg_mask", fg_mask)
                c = cv2.waitKey(25)
                if c == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()

    def onHarrisPoint(self):
        # harris角点检测API
        blockSize = 5
        ksize = 3
        k = 0.04
        img = cv2.imread("./res/161.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dst = cv2.cornerHarris(gray, blockSize, ksize, k)
        img[dst > 0.01 * dst.max()] = [0, 0, 255]
        cv2.imshow("img", img)
        cv2.waitKey(0)

    def onTomasiPoint(self):
        # Tomasi角点检测API
        maxCorners = 1000
        ql = 0.01
        minDistance = 10
        img = cv2.imread("./res/161.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, maxCorners, ql, minDistance)
        corners = np.int0(corners)
        for i in corners:
            x, y = i.ravel()
            cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("img", img)
        cv2.waitKey(0)
