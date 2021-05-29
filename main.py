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

        self.score = 0
        self.deFaultGeo = QRect(95, 85, 1128, 555)
        self.setGeometry(self.deFaultGeo)

        self.movie_all_frames = []

        self.movie_is_runnning = False

        self.movie = QMovie("loader.gif")
        self.ui.gifLabel.setMovie(self.movie)

        self.ui.clickButton.clicked.connect(self.clickProcess)

        self.show()

    def clickProcess(self):

        print(self.movie_is_runnning)

        if not self.movie_is_runnning:
            self.button_start()
            self.movie.start()
            self.ui.imageLabel.setPixmap(None)
            self.movie_all_frames.clear()

            while len(self.movie_all_frames)!= self.movie.frameCount():
                QApplication.processEvents()
                if not (self.movie.currentImage() in self.movie_all_frames):
                    self.movie_all_frames.append(self.movie.currentImage())

            self.random_raw_image = random.choice(self.movie_all_frames)
            self.random_img = QPixmap.fromImage(self.random_raw_image)
            self.ui.imageLabel.setPixmap(self.random_img)
            self.movie_is_runnning = True

        else:

            if self.movie.currentImage() == self.random_raw_image:
                self.movie.stop()
                self.button_stopped()
                print("Yes!! Both the images are same ")
                self.score += 1
                self.ui.scoreBoard.setText(f"Score :{str(self.score)}")
                self.movie_is_runnning = False






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