# yolov5-on-raspberry-pi-4
Running yolov5 model on Raspberry Pi 4 using a webcam

# Update your Raspberry Pi
```
sudo apt update
sudp apt upgrade
```
Install `ultralytics` pip package with optional dependencies
```
pip install ultralytics[export]
```
Reboot
```
sudo reboot
```

Run the YOLOv5 using Python code below:
```python
import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
capture = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv5", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
```
