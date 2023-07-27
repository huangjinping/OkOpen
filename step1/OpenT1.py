import cv2


class OpenT1:
    def __init__(self):
        print("OpenT1")

    def onStart(self):
        print("onStart")
        self.func1()

    def func1(self):
        img = cv2.imread("/Users/huhuijie/Downloads/ic_launcher.png", cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        key = cv2.waitKey(0)
        print(key)
        if (key & 0xFF == ord('q')):
            cv2.destroyAllWindows()
