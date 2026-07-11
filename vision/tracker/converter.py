import numpy as np

class DetectionConverter:
    #convert directions produced by the detection
    # into format require by tracker

    @staticmethod
    def to_numpy(detections):
        # convert list or detetcion into numpy array
        #np.ndarray shape = (N,6)

        if len(detections) == 0:
            return np.empty((0,6), dtype=np.float32)
        return np.array(detections, dtype=np.float32)
    
