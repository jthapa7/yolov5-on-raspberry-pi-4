# yolov5-on-raspberry-pi-4
Running yolov5 model on Raspberry Pi 4 using a webcam

# Clone the YOLOv5 Repository
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
```
Install the necessary Python dependencies
```
pip install -r requirements.txt
```
Run the YOLOv5 using Python code below:
```python
import torch
import cv2
from yolov5 import YOLOv5

# Load YOLOv5 model (using a smaller version for better performance on Pi)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)

    # Render results
    results.render()  # Draw bounding boxes on the frame
    cv2.imshow("YOLOv5 Webcam", results.imgs[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```
