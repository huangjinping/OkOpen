import cv2
import numpy as np


class NumPyT0:
    def __init__(self):
        pass

    def onStart(self):
        pass
        print("NumPyT0")
        # self.DrawGraph()
        self.fun1()

    def DrawGraph(self):
        bg = np.zeros([500, 500, 3], np.uint8)
        print(type(bg))
        bg[0:499, 0:499] = 255
        cv2.rectangle(bg, (100, 100), (200, 200), [0, 255, 0], 10)
        cv2.circle(bg, (200, 300), 100, [0, 255, 0], 2)
        cv2.putText(bg, "Num", (100, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 10)
        cv2.imshow("demo", bg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def fun1(self):
        pass
        print("fun1")
        # a = [1] * 10
        # print(a)
        # c = (1, 2, 3)
        # print(type(c))
        # arr=[]
        # print(arr)
        arr = [i for i in range(3)]
        print(arr)
        # del arr[0]
        # print(arr)
        # newarr = arr[0, 2]
        # print(newarr)
