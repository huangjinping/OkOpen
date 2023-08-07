import cv2
import numpy as np


class NumPyT0:
    def __init__(self):
        pass

    def onStart(self):
        pass
        print("NumPyT0")
        # self.DrawGraph()
        # self.fun1()
        # self.fun2()
        # self.fun3()
        self.fun4()

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

    def fun2(self):
        pass
        bg = np.zeros((400, 800, 3), dtype=np.uint8)
        count = 0
        # while count < 200:
        #     bg[count, 200] = [0, 0, 255]
        #     count = count + 1
        rio = bg[100:300, 100:300]
        rio[:, :] = [0, 0, 255]
        rio[50:80, 60:100] = [0, 255, 0]
        cv2.imshow("np", bg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def fun3(self):
        arr = np.array([1, 2, 3])
        print(type(arr))
        one1 = np.ones((1, 3), dtype=np.uint8)
        print(one1)
        furl = np.full((800, 800, 3), 255, dtype=np.uint8)
        print(furl)
        cv2.imshow("ful", furl)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def fun4(self):
        pass
        array1 = np.array([[1, 2, 3], [4, 5,6], [7, 8, 9]], ndmin=3)
        print(array1)
        array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin=3)
        print(array2)
        # 逐元素矩阵乘法
        # result = np.multiply(array1, array2)
        # 矩阵乘积运算
        result = np.matmul(array1, array2)
        # 矩阵点乘运算
        result = np.dot(array1, array2)


        print(result)
