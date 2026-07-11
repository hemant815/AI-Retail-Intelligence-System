import cv2

from config import (
    BOX_COLOR,
    BOX_THICKNESS,
    TEXT_COLOR,
    FONT_SCALE,
)
class Visualizer:
    def draw_detection(self,frame, detections):
        for detection in detections:
            x1,y1,x2,y2 = detection['bbox']
            confidence = detection['confidence']
            #DRAW BOX
            cv2.rectangle(
                frame,
                (x1,y1),
                (x2,y2),
                BOX_COLOR,
                BOX_THICKNESS
            )
            #draw confidence
            cv2.putText(
                frame,
                f"Person {confidence:.2f}",
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                TEXT_COLOR,
                2
            )
        return frame
    