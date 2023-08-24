# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2

from step1.DlibT0 import TlibT0
from step1.FilterT0 import FilterT0
from step1.ImagePs import ImagePs
from step1.MatT0 import MatT0
from step1.NumPyT0 import NumPyT0
from step1.OpenT1 import OpenT1
from step1.OpenT2 import OpenT2
from step1.ReadCar import ReadCar
from step1.TransformT0 import Transform0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # cv2.waitKey(0)
    # print(img2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t0 = ReadCar()
    t0.onStart()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
