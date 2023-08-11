import cv2
import numpy as np


# https://mp.weixin.qq.com/s/CBVIcnBCLPY4EMILaMhigw
class ImagePs:
    def __init__(self):
        pass

    def onStart(self):
        pass
        print("onStart")
        # self.onChange1()
        # self.onChange2()
        # self.onChange3()
        self.decodeImage()

    def onChange(self):
        print("onChange")
        img0 = np.zeros((400, 400, 3), dtype=np.uint8)
        img0[50:200, 50:200] = [255, 255, 255]
        # img1 = cv2.bitwise_not(img0)
        # cv2.imshow("img1", img1)
        img1 = np.zeros((400, 400, 3), dtype=np.uint8)
        img1[150:300, 150:300] = [255, 255, 255]
        # img2 = cv2.bitwise_and(img1, img0)
        # img2 = cv2.bitwise_or(img1, img0)
        img2 = cv2.bitwise_xor(img1, img0)
        cv2.imshow("img0", img0)
        cv2.imshow("img1", img1)
        cv2.imshow("img2", img2)
        cv2.waitKey(0)

    def onChange1(self):
        print("onChange1")
        img = cv2.imread("./res/image.png")
        # cv2.imshow("img1", img)
        logo = np.zeros((200, 200, 3), np.uint8)
        mask = np.zeros((200, 200), np.uint8)

        logo[20:120, 20:120] = [250, 0, 0]
        logo[80:180, 80:180] = [0, 250, 0]

        mask[20:120, 20:120] = 255
        mask[80:180, 80:180] = 255

        m = cv2.bitwise_not(mask)

        roi = img[0:200, 0:200]
        print(type(roi))
        temp = cv2.bitwise_and(roi, roi, mask=m)

        dst = cv2.add(temp, logo)

        img[0:200, 0:200] = dst
        cv2.imshow("logo", logo)
        cv2.imshow("mask", mask)
        cv2.imshow("m", m)
        cv2.imshow("temp", temp)
        # cv2.imshow("dst", dst)
        # cv2.imshow("img", img)

        cv2.waitKey(0)

    def onChange2(self):
        img = cv2.imread("./res/image.png")
        mk = np.zeros((1300, 700), dtype=np.uint8)
        mk[100:200, 100:200] = 255
        # m = cv2.bitwise_not(mk)
        print(type(img))
        roi = img[0:1300, 0:700]
        temp = cv2.bitwise_and(roi, roi, mask=mk)
        print(img.shape)
        cv2.imshow("img", img)
        cv2.imshow("mark", mk)
        cv2.imshow("temp", temp)
        cv2.waitKey(0)

    def onChange3(self):
        img = cv2.imread("./res/logo.png")
        # res = cv2.resize(img, (200, 200))
        # res = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_AREA)
        res = cv2.resize(img, (10000, 10000))
        print(res.shape)
        cv2.imshow("img", img)
        cv2.imshow("res", res)
        cv2.waitKey(0)

    def decodeImage(self):
        img = cv2.imread("./res/yazi.jpg")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("yazi", img)
        cv2.imshow("hsv", hsv)
        cv2.waitKey(0)
