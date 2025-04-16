#Author : Hannah Yang, u1424308
#Ver.0.1 : Added menu & slide bar to the window
#ver.0.2 : Added Image to the window (just 1 image)
#ver.0.3 : animation effect has been done by Qtimer
#ver.1.0 : Added animation start snd stop 2 buttons , FPS control slide button, based on QWidget frame
#ver.1.1 : Changed Start & Stop 1 button, debugged slide change error while playing animation
#          Added menu (Pause, Exit)

import math

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
        self.setGeometry(100, 100, 300, 200)
        self.setFixedSize(QSize(300, 200))

        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.cur_frame = 0
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Timer
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1초마다
        self.timer.timeout.connect(self.draw_image)

        # Animation playing flag
        self.on_play = False

        self.setupUI()

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame1 = QFrame()

        # Add a menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # Add a menu tab
        menu = menubar.addMenu('&Menu')
        # Add a menu item to a menu tab
        pause_action = QAction('&Pause', self)
        pause_action.triggered.connect(self.control_timer)
        menu.addAction(pause_action)

        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        menu.addAction(exit_action)

        # An application needs a central widget
        frame = QWidget()
        layout = QHBoxLayout()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

        #label for image display
        self.image_view = QLabel()
        self.draw_image()
        layout.addWidget(self.image_view)

        #button for Animation start & stop by timer control
        self.start_stop_button = QPushButton("Start", self)
        self.start_stop_button.clicked.connect(self.control_timer)
        layout.addWidget(self.start_stop_button)

        #slide bar for Animation playing speed (FPS)
        self.scale_slider = QSlider(Qt.Orientation.Vertical)
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(100)
        self.scale_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.scale_slider.valueChanged.connect(self.FPS)
        layout.addWidget(self.scale_slider)

        self.FPS_view = QLabel("FPS: 1",self)
        self.FPS_view.setStyleSheet("font-size: 10px; text-align: center;")
        self.FPS_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.FPS_view)

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

    def control_timer(self):
        if self.on_play == False:
            self.timer.start()
            self.start_stop_button.setText("Stop")
            self.on_play = True
        else:
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.on_play = False

    def stop_timer(self):
        self.timer.stop()

    def FPS(self,fps):
        #print(fps)
        if self.on_play==True:
           self.stop_timer()
           self.start_stop_button.setText("Start")
           self.on_play = False

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