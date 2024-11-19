import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
#model = YOLO("best_full_integer_quant_edgetpu.tflite")
model = YOLO("yolov5su.pt")
while cap.isOpened():
    
    ret, frame = cap.read()
    
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv5",annotated_frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()