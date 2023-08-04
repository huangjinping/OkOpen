import cv2
import numpy as np


class OpenT2:
    def __init__(self):
        print("openT2")

    def onStart(self):
        print("onStart")
        # self.func1()
        # self.video_demo()
        # self.save_video()
        # self.read_video()
        # self.addTrackBar()
        # self.mouseControl()
        # self.CaptureShape()
        # self.FaceDetect()
        self.onFaceDetect()

    def func1(self):
        print("func1")

    def get_image_info(self, image):
        print("图像类型：", type(image))
        print("图像长x宽x通道数", image.shape)
        print("图像长宽通道数相乘所得值", image.size)
        print("图像像素值类型：", image.dtype)
        pixel_data = np.array(image)  # 将图片转换成数组
        print("像素大小：", pixel_data)

    def video_demo(self):
        capture = cv2.VideoCapture(0)
        print("类型", type(capture))
        while True:
            ret, frame = capture.read()
            frame = cv2.flip(frame, 1)
            print('1', ret)
            cv2.imshow("video", frame)
            c = cv2.waitKey(50)
            if c == 27:
                break

    def read_video(self):
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('video', 640, 480)
        video = cv2.VideoCapture('./images/3253_1690427157.mp4')
        width = int(video.get(propId=cv2.CAP_PROP_FRAME_WIDTH) / 2)
        height = int(video.get(propId=cv2.CAP_PROP_FRAME_HEIGHT) / 2)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter('./images/ouu.mp4', fourcc, 24, (width, height))
        fps = video.get(propId=cv2.CAP_PROP_FPS)
        print(fps, width, height)
        while video.isOpened():
            ret, frame = video.read()
            if ret is True:
                writer.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        video.release()
        writer.release()
        cv2.destroyAllWindows()

    def save_video(self):
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('video', 640, 360)
        capture = cv2.VideoCapture(0)
        width = int(capture.get(propId=cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(propId=cv2.CAP_PROP_FRAME_HEIGHT))

        print("==width===" + str(width) + "===height===" + str(height))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter("./dist/out.mp4", fourcc, 24.0, (width, height))
        fps = capture.get(propId=cv2.CAP_PROP_FPS)

        print(fps, width, height)
        # face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        while capture.isOpened():
            ret, frame = capture.read()
            if ret is True:
                out.write(frame)
                cv2.imshow('video', frame)
                cv2.resizeWindow('video', 320, 240)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        capture.release()
        out.release()
        cv2.destroyAllWindows()

    def addTrackBar(self):
        print("   addTrackBar  0")

        def callback(value):
            print(value)
            # trackbar控件

        cv2.namedWindow("trackbar", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("trackbar", 640, 480)
        cv2.createTrackbar("R", "trackbar", 0, 255, callback)
        cv2.createTrackbar("G", "trackbar", 0, 255, callback)
        cv2.createTrackbar("B", "trackbar", 0, 255, callback)
        bg = np.zeros((480, 640, 3), np.uint8)
        while True:
            r = cv2.getTrackbarPos("R", "trackbar")
            g = cv2.getTrackbarPos("G", "trackbar")
            b = cv2.getTrackbarPos("B", "trackbar")
            bg[:] = [b, g, r]
            cv2.imshow("trackbar", bg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        print("   addTrackBar  1")

    def mouseControl(self):
        # 鼠标控制

        print("mouseControl  0")

        print("mouseControl  1")

    def CaptureShape(self):
        img = cv2.imread("/Users/huhuijie/Downloads/ic_launcher.jpg", cv2.WINDOW_NORMAL)
        # 创建画布，按下指定键画指定图案
        cur_shape = 0
        # 初始坐标
        start_pos = (0, 0)

        def mouse_callback(event, x, y, flags, userdata):
            nonlocal start_pos, cur_shape
            # 鼠标按下
            if event == cv2.EVENT_LBUTTONDOWN:
                start_pos = (x, y)
            # 鼠标松开
            elif event == cv2.EVENT_LBUTTONUP:
                if cur_shape == 0:
                    cv2.line(img, start_pos, (x, y), (0, 255, 255), 2)
                elif cur_shape == 1:
                    cv2.rectangle(img, start_pos, (x, y), (0, 255, 255), 2)
                elif cur_shape == 2:
                    a = (x - start_pos[0])
                    b = (y - start_pos[1])
                    r = int((a ** 2 + b ** 2) ** 0.5)
                    cv2.circle(img, start_pos, r, (0, 255, 255), 2)
                else:
                    print("not support")

        cv2.namedWindow('draw', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('draw', mouse_callback)

        while True:
            # 按下l键画直线，按下r键画矩形，按下c键画圆
            cv2.imshow('draw', img)
            key = cv2.waitKey(1)
            if key == 27:
                break
            elif key == ord("l"):
                cur_shape = 0
            elif key == ord("r"):
                cur_shape = 1
            elif key == ord("c"):
                cur_shape = 2

        cv2.destroyAllWindows()

    # img = np.zeros([500,500,3],np.uint8)
    # CaptureShape(img)

    def FaceDetect(self):
        # 人脸检测
        face_detector = cv2.CascadeClassifier("./res/haarcascade_frontalface_default.xml")
        while True:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            # print(frame)
            gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
            face = face_detector.detectMultiScale(gray)
            print(len(face))
            for x, y, w, h in face:
                cv2.circle(frame, (x + w // 2, y + h // 2), w // 2, (0, 255, 255), 2)
            cv2.imshow("img", frame)
            key = cv2.waitKey(20)
            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    def onFaceDetect(self):
        face_detector = cv2.CascadeClassifier("./res/haarcascade_frontalface_alt.xml")
        img2 = cv2.imread('./res/a9d.jpeg', 1)
        gray = cv2.cvtColor(img2, code=cv2.COLOR_BGR2GRAY)
        face = face_detector.detectMultiScale(gray)
        for x, y, w, h in face:
            cv2.circle(img2, (x + w // 2, y + h // 2), w // 2, (0, 255, 255), 2)
            cv2.imshow("img", img2)
        cv2.waitKey(0)
        cv2.destroyWindow()
