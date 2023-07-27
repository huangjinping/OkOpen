import cv2
import numpy as np


class OpenT0:
    def __init__(self):
        print("OpenT0init1")

    def onStart(self):
        print("onStart")
        print(cv2)
        self.bitwise_demo()
        # self.read_demo()

    def read_demo(self):
        img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        cv2.imshow("img1", img2)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def color_space_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        img2 = cv2.imread('/Users/huhuijie/Downloads/taile1.jpg', 1)
        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        cv2.imshow("gray", gray)
        cv2.imshow("hsv", hsv)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def mat_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/taile1.jpg')
        print(image.shape)
        # roi=image[100:200,100:200,:]
        # blank= np.zeros_like(image)
        blank = np.copy(image)
        cv2.imshow("blank", blank)
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def nothing(x):
        print(x)

    def pixel_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/taile1.jpg')

        print("pixel_demo---=1")
        h, w, c = image.shape
        print(image.shape)
        for row in range(h):
            for col in range(w):
                b, g, r = image[row, col]
                image[row, col] = (255 - b, g, r)
        cv2.imshow('roust', image)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def math_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/river/taile.jpg')
        print("pixel_demo---=1")
        cv2.imshow("input", image)
        h, w, c = image.shape
        blank = np.zeros_like(image)
        blank[:, :] = [50, 50, 50]

        cv2.imshow("blank", blank)
        result = cv2.multiply(image, blank)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def math1_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/river/taile.jpg')
        cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar("lightness", "input", 0, 100, self.nothing())
        print("pixel_demo---=1")
        cv2.imshow("input", image)
        h, w, c = image.shape
        blank = np.zeros_like(image)
        blank[:, :] = [50, 50, 50]

        cv2.imshow("blank", blank)
        result = cv2.multiply(image, blank)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def color_map_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/river/m1975.png')
        cv2.imshow("input", image)
        while True:
            c = cv2.waitKey(1)
            print(c)
            if c == 49:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imshow("result", gray)
            if c == 50:
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                cv2.imshow("result", hsv)
            if c == 51:
                invert = cv2.bitwise_not(image)
                cv2.imshow("result", invert)
            if c == 27:
                break
        cv2.destroyAllWindows()

    def color_pic_demo(self):
        # img2 = cv2.imread('/Users/huhuijie/Downloads/m1975.png', 1)
        image = cv2.imread('/Users/huhuijie/Downloads/river/m1975.png')
        cv2.imshow("input", image)
        colormap = [
            cv2.COLORMAP_MAGMA,
            cv2.COLORMAP_INFERNO,
            cv2.COLORMAP_PLASMA,
            cv2.COLORMAP_VIRIDIS,
            cv2.COLORMAP_CIVIDIS,
            cv2.COLORMAP_TWILIGHT,
            cv2.COLORMAP_TWILIGHT_SHIFTED,

        ]
        index = 0
        while True:
            dest = cv2.applyColorMap(image, colormap[index % len(colormap)])
            index += 1
            cv2.imshow("color style", dest)
            c = cv2.waitKey(1000)
            if c == 27:
                break
        cv2.destroyAllWindows()

    def addTrackBer_demo(self):
        # https: // blog.csdn.net / KID_yuan / article / details / 89495613
        image = cv2.imread("/Users/huhuijie/Downloads/river/taile.jpg")
        cv2.imshow("Saber", image)

        trackbarName1 = "Ratio_a"
        trackbarName2 = "Bright_g"
        windowName = "dstImage"
        print("addTrackBer")
        a = 1  # 设置a的初始值
        g = 10  # 设置g的初值
        count1 = 20  # 设置a的最大值
        count2 = 50  # 设置g的最大值
        # 给滑动窗口命名，该步骤不能缺少！而且必须和需要显示的滑动条窗口名称一致。
        cv2.namedWindow(windowName)

        def contrast_Ratio_brightness(arg):
            # arg参数：为接收新变量地址
            # a为对比度，g为亮度
            # cv.getTrackbarPos获取滑动条位置处的值
            # 第一个参数为滑动条1的名称，第二个参数为窗口的名称。
            a = cv2.getTrackbarPos(trackbarName1, windowName)
            g = cv2.getTrackbarPos(trackbarName2, windowName)
            h, w, c = image.shape
            mask = np.zeros([h, w, c], image.dtype)
            # cv.addWeighted函数对两张图片线性加权叠加
            dstImage = cv2.addWeighted(image, a, mask, 1 - a, g)
            cv2.imshow("dstImage", dstImage)

        # 第一个参数为滑动条名称，第二个参数为窗口名称，
        # 第三个参数为滑动条参数，第四个为其最大值，第五个为需要调用的函数名称。
        cv2.createTrackbar(trackbarName1, windowName, a, count1, contrast_Ratio_brightness)
        cv2.createTrackbar(trackbarName2, windowName, g, count2, contrast_Ratio_brightness)
        # 下面这步调用函数，也不能缺少。
        # contrast_Ratio_brightness(0)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def drawing_demo(self):
        b1 = np.zeros((512, 512, 3), dtype=np.uint8)
        cv2.rectangle(b1, (50, 50), (400, 400), (0, 0, 255), 2, 8, 0)
        cv2.circle(b1, (200, 200), 100, (255, 0, 0), 2, 8, 0)
        cv2.line(b1, (0, 0), (512, 512), (255, 0, 0), 2, 8, 0)
        cv2.line(b1, (0, 512), (512, 0), (255, 0, 0), 2, 8, 0)
        cv2.imshow("input", b1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def bitwise_demo(self):
        b1 = cv2.imread("/Users/huhuijie/Downloads/river/m1975.png")
        print(b1.shape)
        cv2.imshow("input", b1)
        cv2.imshow("b1", b1[:, :, 2])
        mv = cv2.split(b1)
        mv[0] = 255
        result = cv2.merge(mv)
        cv2.imshow("result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def bitwise_demo(self):
        b1 = np.zeros((400, 400, 3), dtype=np.uint8)
        b1[:, :] = (255, 0, 255)
        b2 = np.zeros((400, 400, 3), dtype=np.uint8)
        b2[:, :] = (0, 255, 255)
        cv2.imshow("b1", b1)
        cv2.imshow("b2", b2)

        dst1 = cv2.bitwise_and(b1, b2)
        dst2 = cv2.bitwise_or(b1, b2)
        cv2.imshow("bitwise_and", dst1)
        cv2.imshow("bitwiset_or", dst2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
