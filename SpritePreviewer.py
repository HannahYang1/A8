#Author : Hannah Yang u1424308
#Ver.0.1 : Added menu & slide bar to the window
#ver.0.2 : Added Image to the window (just 1 image)

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
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.image = QImage('spriteImages/sprite_00.png')
        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        # Add a menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # Add a menu tab
        file_menu = menubar.addMenu('&File')
        # Add a menu item to a menu tab
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(exit_action)
        # An application needs a central widget
        frame = QWidget()
        layout = QHBoxLayout()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

        # Add other widgets to this frame through its layout
        self.image_view = QLabel()
        self.image_view.setPixmap(QPixmap(self.image))
        layout.addWidget(self.image_view)

        self.scale_slider = QSlider()
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(50)
        layout.addWidget(self.scale_slider)

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.setCentralWidget(frame)

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