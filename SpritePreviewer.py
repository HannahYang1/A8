#Author : Hannah Yang, Games
#Ver.0.1 : Added menu & slide bar to the window
#ver.0.2 : Added Image to the window (just 1 image)
#ver.0.3 : animation effect has been done by Qtimer
#ver.1.0 : Added animation start @ stop button , FPS control slide button, based on QWidget frame

import math
import threading

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import QTimer

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.cur_frame = 0
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Timer
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1초마다
        self.timer.timeout.connect(self.draw_image)

        self.setupUI()

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        # frame = QFrame()

        # An application needs a central widget
        frame = QWidget()
        layout = QHBoxLayout()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

        #label for image display
        self.image_view = QLabel()
        self.draw_image()
        layout.addWidget(self.image_view)

        #button for Animation start & stop by timer
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        layout.addWidget(self.stop_button)

        #slide bar for Animation playing speed (FPS)
        self.scale_slider = QSlider(Qt.Orientation.Vertical)
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(100)
        self.scale_slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.scale_slider.valueChanged.connect(self.FPS)
        layout.addWidget(self.scale_slider)

        self.FPS_view = QLabel("FPS: 1",self)
        self.FPS_view.setStyleSheet("font-size: 10px; text-align: center;")
        self.FPS_view.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add other widgets to this frame through its layout

        # Connect the slider to an action

       # self.scale_slider.valueChanged.connect(self.num_frames)

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

    def draw_image(self):
        self.cur_frame = self.cur_frame + 1
        if self.cur_frame == 21:  # repeat animation
            self.cur_frame = 0
        self.image_view.setPixmap(QPixmap(self.frames[self.cur_frame]))

    def start_timer(self):
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def FPS(self,fps):
        #print(fps)
        self.stop_timer()
        interval = int(1000/fps)
        self.timer.setInterval(interval)
        self.FPS_view.setText("FPS: "+str(fps))

    def quit_program(self):
        QApplication.quit()

    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()

    app.exec()


if __name__ == "__main__":
    main()