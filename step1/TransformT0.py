import numpy as np

import cv2


# https://mp.weixin.qq.com/s/Fw1BA57lp88xS-TPNceq5Q
class Transform0:
    def __init__(self):
        pass
        print("变换")

    def onStart(self):
        print("onStart")
        # self.onToushi()
        # self.onAffine()
        # self.onMartrix()
        # self.onTansform01()
        self.onInvert()

    def onInvert(self):
        print("onInvert")
        img = cv2.imread("./res/311.jpg")
        dst1 = cv2.flip(img, 0)
        res1 = np.vstack((img, dst1))

        dst2 = cv2.flip(img, 1)
        res2 = np.vstack((img, dst2))

        dst3 = cv2.flip(img, -1)
        res3 = np.vstack((img, dst3))
        result = np.hstack((res1, res2, res3))

        cv2.imshow("result", result)
        cv2.imwrite("./dist/result_flip.png", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def onRotate(self):
        img = cv2.imread("./res/311.jpg")
        dst1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("dst1", dst1)
        cv2.imshow("img", img)

        cv2.waitKey(0)

    def onTansform01(self):
        print(1)
        img = cv2.imread("./res/640.png")
        h, w, ch = img.shape
        M = np.float32([[1, 0, 500], [0, 1, 500]])
        new = cv2.warpAffine(img, M, (w, h))
        cv2.imshow("new", new)
        cv2.waitKey(0)

    def onMartrix(self):
        print(1)
        img = cv2.imread("./res/640.png")
        h, w, ch = img.shape
        M = cv2.getRotationMatrix2D((w / 2, h / 2), -15, 1.0)
        new = cv2.warpAffine(img, M, (w, h))
        cv2.imshow("new", new)
        cv2.waitKey(0)

    def onAffine(self):
        # 仿射变换
        print("1")
        img = cv2.imread("./res/640.png")
        h, w, chi = img.shape
        print(img.shape)
        src = np.float32([[0, 211], [639, 255], [82, 678]])
        dst = np.float32([[0, 0], [600, 0], [0, 600]])
        M = cv2.getAffineTransform(src=src, dst=dst)
        new = cv2.warpAffine(img, M, (w, h))
        cv2.imshow("640", img)
        cv2.imshow("new", new)
        cv2.waitKey(0)

    def onToushi(self):
        # 透视变换
        print("1")
        img = cv2.imread("./res/640.png")
        h, w, chi = img.shape
        print(img.shape)
        src = np.float32([[0, 211], [639, 255], [82, 678], [543, 695]])
        dst = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
        M = cv2.getPerspectiveTransform(src=src, dst=dst)
        new = cv2.warpPerspective(img, M, (600, 600))
        cv2.imshow("640", img)
        cv2.imshow("new", new)
        cv2.waitKey(0)
