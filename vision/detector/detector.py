from ultralytics import YOLO

from config import (
    YOLO_MODEL,
    CONFIDENCE_THRESHOLD,
    PERSON_CLASS_ID
)

class PersonDetector:
    # yolo person detector
    def __init__(self):
        print('[INFO] loading yolo model')
        self.model = YOLO(YOLO_MODEL)
        print('[INFO] loaded Sucessfully')

    def detect(self,frame):
        #detect person in frame
        # return list of dictionary
        results = self.model.predict(frame,
                                    conf = CONFIDENCE_THRESHOLD,
                                    verbose = False
                                ) 
        detection = []

        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])


                #ignore evrything execpt person

                if class_id != PERSON_CLASS_ID:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                detection.append({
                    "bbox":(x1,y1,x2,y2),
                    "confidence":confidence
                })
        return detection
    

