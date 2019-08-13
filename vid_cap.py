import cv2

class VideoCap:
    def __init__(self):
        self.name = "Video Capture"
    def camera(self):
        return cv2.VideoCapture(0)