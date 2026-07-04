import cv2

class Visualizer:

    @staticmethod
    def show(window_name, frame):

        cv2.imshow(window_name, frame)

    @staticmethod
    def close():

        cv2.destroyAllWindows()