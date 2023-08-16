import cv2
import numpy as np


class FilterT0:
    def __init__(self):
        pass

    def onStart(self):
        pass
        # self.onCanny()
        # self.onThreholds()
        # self.onAdaptiveThreshold()
        # self.onErode()
        # self.onDilate()
        # self.getStructuringElement()
        # self.morphologyEx_OPEN()
        # self.morphologyEx_CLOSE()
        # self.morphologyEx_GRADIENT()
        # self.morphologyEx_TOPHEADER()
        self.morphologyEx_BLACKHAT()
        print("提交信息")

    def onCanny(self):
        img = cv2.imread('./res/311.jpg')
        dst = cv2.Canny(img, 100, 200)
        cv2.imshow("img", img)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def onThreholds(self):
        img = cv2.imread("./res/1513.jpg")
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_TOZERO_INV)
        print(dst.shape)
        cv2.imshow("img", img)
        cv2.imshow("img1", img1)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def onAdaptiveThreshold(self):
        img = cv2.imread("./res/1513.jpg")
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dst = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
        cv2.imshow("img", img)
        cv2.imshow("img1", img1)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def onErode(self):
        img = cv2.imread("./res/1513.jpg")
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.zeros([6, 6], dtype=np.uint8)
        dst = cv2.erode(img1, kernel, 0)
        cv2.imshow("img", img)
        cv2.imshow("img1", img1)
        cv2.imshow("erode", dst)
        cv2.waitKey(0)

    def onDilate(self):
        img = cv2.imread("./res/zhi.jpg")
        img = cv2.resize(img, (1000, 500))
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.zeros([6, 6], dtype=np.uint8)
        dst = cv2.dilate(img1, kernel, 0)
        cv2.imshow("img", img)
        cv2.imshow("img1", img1)
        cv2.imshow("dilate", dst)
        cv2.waitKey(0)

    def getStructuringElement(self):
        # 获取卷积核 卷积核越大处理的 处理的噪点颗粒越大
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        print(kernel)
        dst = cv2.erode(img, kernel, iterations=1)
        dst1 = cv2.dilate(dst, kernel, iterations=1)
        cv2.imshow("dst", dst)
        cv2.imshow("dst1", dst1)
        cv2.waitKey(0)

    def morphologyEx_OPEN(self):
        # 开运算
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def morphologyEx_CLOSE(self):
        # 闭运算
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def morphologyEx_GRADIENT(self):
        # 梯度运算
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def morphologyEx_TOPHAT(self):
        # 顶帽算法=原图-开运算
        # 原图减开运算，得到大图形外的小图形
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)

    def morphologyEx_BLACKHAT(self):
        # 黑帽算法=原图-闭运算
        # 原图减闭运算，得到大图形的小图形
        img = cv2.imread("./res/zhi.jpg")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)
