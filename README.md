### README.md

## Object Detection using MobileNet SSD with OpenCV

This Python script uses OpenCV and MobileNet SSD to perform real-time object detection on a video feed from a camera. Detected objects are labeled and a bounding box is drawn around them. The detected objects are saved in a directory named `detected_objects`.

### Prerequisites

- Python 3.x
- OpenCV (cv2)
- NumPy

### Installation

1. Install OpenCV and NumPy using pip:

    ```bash
    pip install opencv-python numpy
    ```

2. Download the MobileNet SSD model files:
    - `MobileNetSSD_deploy.prototxt`
    - `MobileNetSSD_deploy.caffemodel`

### How to Run the Script

1. Place the `MobileNetSSD_deploy.prototxt` and `MobileNetSSD_deploy.caffemodel` files in the same directory as the script.
2. Create a directory named `detected_objects` in the same directory to save the detected objects.
3. Run the script:

    ```bash
    python object_detection.py
    ```

### Brief Explanation of the Code

- **Imports**:
    - `cv2` and `numpy` are imported for image processing and array operations.
    - `os` is imported to manage directories and files.

- **MobileNet SSD Initialization**:
    - The MobileNet SSD model is loaded using `cv2.dnn.readNetFromCaffe`.

- **Video Capture**:
    - OpenCV's `VideoCapture` is used to capture video from the default camera (change `0` to a video file path to use a video file).

- **Object Detection**:
    - Each frame from the video feed is resized to 300x300 and passed through the MobileNet SSD model.
    - Detected objects with confidence greater than 0.2 are identified and labeled.
    - Bounding boxes are drawn around the detected objects on the frame.

- **Saving Detected Objects**:
    - The detected objects are cropped from the frame and saved as individual image files in the `detected_objects` directory.

- **Display and Exit**:
    - The resulting frame with detected objects is displayed.
    - Press `q` to exit the application.

