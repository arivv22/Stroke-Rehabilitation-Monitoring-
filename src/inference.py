import cv2

from models.pose_estimator import PoseEstimator
from utils.visualization import Visualizer

video = "datasets/sample/test.mp4"

cap = cv2.VideoCapture(video)  # type: ignore

pose = PoseEstimator()

while True:

    success, frame = cap.read()

    if not success:
        break

    result = pose.estimate(frame)

    frame = pose.draw(frame, result)

    Visualizer.show("Pose Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

Visualizer.close()