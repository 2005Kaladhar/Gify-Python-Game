from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_uidesign import Ui_MainWindow
import sys,random

class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.movie = QMovie("loader.gif")
        self.ui.gifLabel.setMovie(self.movie)

        self.screenGeo = QApplication.desktop().screenGeometry()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.scores = 0
        self.movie_is_running = False
        self.movie_all_frames = []

        self.default_geometry = QRect(87, 83, 1119, 555)
        self.setGeometry(self.default_geometry)

        self.ui.clickButton.clicked.connect(self.clickButtonProcess)
        self.ui.CloseButton_2.clicked.connect(self.closer)
        self.ui.Minimizebtn_2.clicked.connect(self.mini_button)
        self.ui.Maximizebtn_2.clicked.connect(self.maxi_button)

        self.ui.celebrate_label.hide()

        def moveWindow(e):
            FRAME = QApplication.desktop().screenGeometry()
            if not (FRAME == self.geometry()):
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.TitleBar_2.mouseMoveEvent = moveWindow

        self.show()


    def clickButtonProcess(self):

        if not self.movie_is_running:
            self.movie.start()
            self.ui.celebrate_label.hide()
            self.button_start()
            self.movie_is_running = True

            while len(self.movie_all_frames)!= self.movie.frameCount():
                QApplication.processEvents()
                if not self.movie.currentImage() in self.movie_all_frames:
                    self.movie_all_frames.append(self.movie.currentImage())

            self.random_raw_image = random.choice(self.movie_all_frames)
            self.random_image = QPixmap.fromImage(self.random_raw_image)
            self.ui.imageLabel.setPixmap(self.random_image)

        else:
            if self.movie.currentImage() == self.random_raw_image:
                print("Wohooooooo both the images are same....")
                print(f"YOur Score is {self.scores}")
                self.button_stopped()
                self.movie.stop()
                self.scores += 1
                self.ui.celebrate_label.show()
                self.ui.scoreBoard.setText(f"Score :{str(self.scores)}")
                self.movie_is_running = False

    def mousePressEvent(self, event) -> None:
        self.clickPosition = event.globalPos()

    def closer(self):
        self.close()
        quit()

    def mini_button(self):
        if self.isMinimized():
            self.setGeometry(self.default_geometry)
        else:
            self.showMinimized()

    def maxi_button(self):
        fullscreen = self.screenGeo == self.geometry()
        print("is it in full screen ?:",fullscreen)
        print("screen geometry is ",self.screenGeo)
        if fullscreen:
            self.setGeometry(self.default_geometry)
        elif not fullscreen:
            self.setGeometry(self.screenGeo)


    def button_start(self):
        normal_stylesheet = '''
                    QPushButton{
                    border-radius:10px;
                    background-color: rgb(0, 255, 127);

                    }

                    QPushButton::hover{
                    background-color: rgb(255, 0, 0);

                    }
                    '''
        self.ui.clickButton.setText('Click!')
        self.ui.clickButton.setStyleSheet(normal_stylesheet)

    def button_stopped(self):
        pause_stylesheet = '''
                             QPushButton{
                            border-radius:10px;
                            background-color: rgb(0, 255, 127);

                            }

                            QPushButton::hover{
                            	background-color: rgb(255, 255, 0);
                            }

                    '''
        self.ui.clickButton.setStyleSheet(pause_stylesheet)
        self.ui.clickButton.setText("Continue")


if __name__ == '__main__':
    app = QApplication()
    window = Application()
    sys.exit(app.exec_())