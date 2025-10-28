from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.rtsp.camera_rtsp import CameraRTSP

app = FastAPI()

camera_url = "rtsp://10.208.88.36:8554/cam"

def generate_frames(use_face_detection=False):
    cam = CameraRTSP(camera_url, use_face_detection=use_face_detection)
    while True:
        frame = cam.get_frame()
        if frame is None:
            break
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )

@app.get("/")
def root():
    return {"message": "RTSP Stream Server Aktif"}

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(False),
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video_feed_faces")
def video_feed_faces():
    return StreamingResponse(generate_frames(True),
                             media_type="multipart/x-mixed-replace; boundary=frame")