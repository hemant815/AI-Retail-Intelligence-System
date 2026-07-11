import cv2


class Camera:
    # handle webcam, videofile, cctv
    def __init__(self,source):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Unable to connect with {self.source}"
            )
        
    def read(self):
        #read  frame from video

        #Return tuple(res, frame)
        return self.cap.read()
    
    def release(self):
        if self.cap.isOpened():
            self.cap.release()



