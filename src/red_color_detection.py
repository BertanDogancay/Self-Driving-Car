import numpy as np
import cv2
        
class ColorDetector:
    def __init__(self, accumWeight=0.5):
        self.accumWeight = accumWeight
        self.bg = None

    def update(self, image):
        if self.bg is None:
            self.bg = image.copy().astype("float")
            return
        cv2.accumulateWeighted(image, self.bg, self.accumWeight)


    def detect(self, image):
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)

        contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)

            x_medium = int((x + x + w) / 2)
            y_medium = int((y + y + h) / 2)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return (x_medium, y_medium)

        return None