import cv2


class MatT0:
    def __init__(self):
        pass

    def onStart(self):
        pass
        # self.onSplit()
        # self.onAdd()
        # self.onCopy()
        self.onMat()

    def onSplit(self):
        print("onSplit")
        img = cv2.imread('./res/tuijian.png')
        b, g, r = cv2.split(img)
        # cv2.imshow("b", b)
        # cv2.imshow("g", g)
        # cv2.imshow("r", r)
        res = cv2.merge((b, g, r))
        print(img)
        cv2.imshow("img1", res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def onAdd(self):
        img1 = cv2.imread('./res/tuijian.png')
        img2 = cv2.imread('./res/tuijian2.png')
        img = cv2.add(img1, img2)
        cv2.imshow("img1", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def onCopy(self):
        img = cv2.imread('./res/tuijian.png')
        img2 = img.copy()
        img[0:200, 0:200] = [0, 0, 255]
        print(type(img2))
        cv2.imshow("img1", img)
        cv2.imshow('img2', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def onMat(self):
        pass
        img = cv2.imread('./res/tuijian.png')
        print(img.shape)
        print(img.size)
        print(img.dtype)
