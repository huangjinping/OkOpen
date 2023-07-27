import cv2
import numpy as np


class OpenT2:
    def __init__(self):
        print("openT2")

    def onStart(self):
        print("onStart")
        # self.func1()
        # self.video_demo()
        self.save_video()
        # self.read_video()

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
        out = cv2.VideoWriter("./images/xiaoguo.mp4", fourcc, 24.0, (width, height))
        fps = capture.get(propId=cv2.CAP_PROP_FPS)

        print(fps, width, height)
        # face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        while capture.isOpened():
            ret, frame = capture.read()
            if ret is True:
                out.write(frame)
                cv2.imshow('video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        capture.release()
        out.release()
        cv2.destroyAllWindows()
