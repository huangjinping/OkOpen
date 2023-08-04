import cv2


class OpenT1:
    def __init__(self):
        print("OpenT1")

    def onStart(self):
        print("onStart")
        # self.func1()
        self.func2()

    def func1(self):
        img = cv2.imread("./res/311.jpg", cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        key = cv2.waitKey(0)
        print(key)
        if (key & 0xFF == ord('q')):
            cv2.destroyAllWindows()


    def func2(self):
        print("增加调色板")

        def callback(e):
            pass

        cv2.namedWindow("color", cv2.WINDOW_NORMAL)
        img = cv2.imread("./res/311.jpg")
        colorSpaces = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2YUV,
                       cv2.COLOR_BGR2HSV_FULL]
        print(len(colorSpaces))
        cv2.createTrackbar("curColor", 'color', 0, len(colorSpaces), callback)
        while True:
            index = cv2.getTrackbarPos('curColor', 'color')
            cvt_img = cv2.cvtColor(img, colorSpaces[index - 1])
            cv2.imshow('color', cvt_img)
            key = cv2.waitKey(20)
