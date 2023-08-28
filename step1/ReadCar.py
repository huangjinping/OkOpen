import cv2
import numpy as np
from pytesseract import pytesseract


class ReadCar:
    def __init__(self):
        pass

    def onStart(self):
        print("on Read Car On Start")
        # self.onReadVideoRemoveBackground()
        # self.onHarrisPoint()
        # self.onTomasiPoint()
        # self.onSIFTPoint()
        # self.onSURFPoint()
        # self.onORBPoint()
        # self.onBFMatcher()
        self.onPytesseract()

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

    def onSIFTPoint(self):
        # SIFT 最大的弊端就是慢
        img = cv2.imread("./res/161.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 创建sift对象
        sift = cv2.SIFT_create()
        # 进行检测
        kp = sift.detect(gray, None)
        # 计算描述子
        kp, des = sift.compute(img, kp)
        # 进行检测同时计算关键点和描述
        # kp, des = sift.detectAndCompute(gray, None)
        print(cv2.__version__)
        # 绘制关键点
        cv2.drawKeypoints(gray, kp, img)
        cv2.imshow("img", img)
        cv2.waitKey(0)

    def onSURFPoint(self):
        # SURF 最大的弊端就是慢,因为才有SURF
        img = cv2.imread("./res/161.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 创建sift对象
        sift = cv2.SURF_create()

        # 进行检测同时计算关键点和描述
        kp, des = sift.detectAndCompute(gray, None)
        print(cv2.__version__)
        # 绘制关键点
        cv2.drawKeypoints(gray, kp, img)
        cv2.imshow("img", img)
        cv2.waitKey(0)

    def onORBPoint(self):
        # SURF 最大的弊端就是慢,因为才有SURF
        img = cv2.imread("./res/161.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 创建ORB对象
        sift = cv2.ORB_create()

        # 进行检测同时计算关键点和描述
        kp, des = sift.detectAndCompute(gray, None)
        # 绘制关键点
        cv2.drawKeypoints(gray, kp, img)
        cv2.imshow("img", img)
        cv2.waitKey(0)

    def onBFMatcher(self):
        import cv2

        # 读取两幅图像
        image1 = cv2.imread('./res/mex_01head.jpg', cv2.IMREAD_GRAYSCALE)
        image2 = cv2.imread('./res/mex_01.jpg', cv2.IMREAD_GRAYSCALE)

        # 创建ORB特征检测器
        orb = cv2.ORB_create()

        # 在两幅图像上检测特征点和描述符
        keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
        keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

        # 创建暴力匹配器
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # 执行暴力匹配
        matches = bf.match(descriptors1, descriptors2)

        # 根据匹配程度进行排序
        matches = sorted(matches, key=lambda x: x.distance)

        # 绘制前几个匹配
        result = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None, flags=2)

        # 显示匹配结果
        cv2.imshow('Matches', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def onPytesseract(self):
        print("ocr")
        # 加载图像
        image_path = './res/mex_01.jpg'
        image = cv2.imread(image_path)
        # 图像预处理（例如，裁剪和缩放）
        # 文字识别
        text = pytesseract.image_to_string(image, lang='eng')
        # 输出识别的文字
        print(text)
        cv2.imshow("image", image)
        cv2.waitKey(0)
