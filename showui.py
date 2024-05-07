# coding=utf-8
# @FileName      :showUI
# @Time          :2023/8/31 21:56
# @Author        :AhrIlI
# @Contact       :906629272@qq.com

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
from ui import DriveMWindow


def get_host_app():
    app = QApplication.activeWindow()
    while True:
        parent = app.parent()
        if parent:
            app = parent
        else:
            break
    return app


class ShowWin(DriveMWindow):

    def __init__(self, parent = get_host_app()):
        super(ShowWin, self).__init__(parent)


uv_drive_window = None


def show():
    """
    显示界面
    :return:
    """
    global uv_drive_window
    if uv_drive_window is None:
        uv_drive_window = ShowWin()
    uv_drive_window.show()


