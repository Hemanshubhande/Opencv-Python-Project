import cv2
import numpy as np
import os

# Create a directory to save detected objects
if not os.path.exists('detected_objects'):
    os.makedirs('detected_objects')

# Load MobileNet SSD
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")

# List of classes for MobileNet SSD
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Open video capture device
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Resize frame to 300x300 for object detection
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    
    # Pass blob through network
    net.setInput(blob)
    detections = net.forward()
    
    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # Check confidence threshold
        if confidence > 0.2:
            class_id = int(detections[0, 0, i, 1])
            
            # Get bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")
            
            # Draw bounding box and label on frame
            label = "{}: {:.2f}%".format(CLASSES[class_id], confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Save detected objects
            object_img = frame[startY:endY, startX:endX]
            cv2.imwrite(f'detected_objects/object_{i}.jpg', object_img)
    
    # Display the resulting frame
    cv2.imshow('Object Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
