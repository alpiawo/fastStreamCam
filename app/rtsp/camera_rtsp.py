import cv2
from app.rtsp.face_detector import detect_faces

class CameraRTSP:
    def __init__(self, rtsp_url, use_face_detection=False):
        self.cap = cv2.VideoCapture(rtsp_url)
        self.use_face_detection = use_face_detection
        self.frame_count = 0

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        if self.use_face_detection:
            self.frame_count += 1
            if self.frame_count % 5 == 0:
                frame = detect_faces(frame)

        _, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
