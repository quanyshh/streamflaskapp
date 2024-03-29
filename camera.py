import cv2
from base_camera import BaseCamera


class Camera1(BaseCamera):
    video_source = 0


    @staticmethod
    def set_video_source(source):
        Camera1.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera1.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
