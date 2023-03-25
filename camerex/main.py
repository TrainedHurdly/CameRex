import pyvirtualcam
import numpy as np
import cv2



class Rex:
    def __init__(self):
        self.no_image = cv2.imread('pics/test-1280x720.jpg')
    def no_video(self):
        with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
            print(f'Using virtual camera: {cam.device}')
            b_channel = self.no_image[:,::-1,0]
            g_channel = self.no_image[:,::-1,1]
            r_channel = self.no_image[:,::-1,2]
            frame = cv2.merge((b_channel, g_channel, r_channel))
            while True:
                cam.send(frame)
                cam.sleep_until_next_frame()

if __name__ == "__main__":
    camera = Rex()
    camera.no_video()