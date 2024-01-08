# pulchihd@raspberrypi:~ $ libcamera-still -o test.jpg
# pulchihd@raspberrypi:~ $ sudo apt-get install python3-opencv

from picamera2 import Picamera2
import time
import cv2 as cv

# Using an object to compartmentalize initialization processes
class ChessBoard:
    #initialize picamera2 library
    def __init__(self, width: int, height: int):
        self.cam = Picamera2()
        camera_config = self.cam.create_still_configuration(main={"size": (width, height)})
        self.cam.configure(camera_config)
        self.request_home()
        self.snap_pic()
        self.photo = "board.jpg"

    # toggle camera flash
    def flash(self):
        pass

    # request x,y,z motor positions to be set to the home position
    def request_home(self):
        pass

    # take photo and overwrite board.jpg with the current state-representing photo
    def snap_pic(self):
        self.request_home()
        self.flash()
        self.cam.start()
        time.sleep(2)
        self.cam.capture_file("board.jpg")
        self.flash()

def inspect():
    pass

picam = ChessBoard(2000, 2000)
