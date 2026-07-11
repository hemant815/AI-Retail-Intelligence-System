import cv2
from vision.camera.camera import Camera
from config import CAMERA_SOURCE, WINDOW_NAME, BOX_COLOR,BOX_THICKNESS,TEXT_COLOR,FONT_SCALE
from vision.detector.detector import PersonDetector
from vision.visualizer.visualizer import Visualizer


def main():

    camera = Camera(CAMERA_SOURCE)
    detector = PersonDetector()
    visualizer = Visualizer()

    while True:
        ret, frame = camera.read()

        if not ret:
            print("failed to read frame")
            break
        detections = detector.detect(frame)
        frame = visualizer.draw_detection(frame, detections)

        cv2.imshow(WINDOW_NAME,frame)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    camera.release()
    cv2.destroyWindows()


if __name__ == '__main__':
    main()



                    