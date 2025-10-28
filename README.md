# RTSP Streaming with Face Detection

This project is a FastAPI + OpenCV based system for real-time RTSP streaming with face detection.

---

## Features

- Real-time RTSP streaming via OpenCV
- Face detection using a pre-trained OpenCV model (`res10_300x300_ssd`)
- FastAPI backend with streaming and control endpoints

---

## Project Structure

```
project-root/
│
├── app/
│ ├── rtsp/
│ │ ├── camera_rtsp.py # RTSP stream handler
│ │ ├── face_detector.py # Face detection logic
│ │ └── main.py # FastAPI entry point
│ └── models/ # ML models (e.g., sleeping detection)
├── requirements.txt
└── README.md
```

---

## Requirements

Make sure the following are installed:

- Python 3.9+
- FFmpeg (for video handling)
- Virtual environment (venv) for dependency isolation

Check versions:

```bash
python --version
```

## Setup Environment

1. Clone the repo

```
git clone https://github.com/alpiawo/fastStreamCam.git
cd fastStreamCam
```

2. Create virtual env

```
python -m venv venv
```

3. Activate virtual env (Windows)

```
venv\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

## Run the Server

1. Change your rtsp URL in main.py
2. Start FastAPI

```
uvicorn app.rtsp.main:app --host 0.0.0.0 --port 8000
```

3. Access the web stream:
   - Base URL: http://127.0.0.1:8000
   - Stream endpoint: /video_feed
   - Stream + Face detection endpoint: /video_feed_faces
