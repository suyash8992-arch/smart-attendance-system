# Backend - Smart Attendance System

The **backend** is the core processing engine of the Smart Attendance System. It is responsible for receiving images from the Raspberry Pi, performing face recognition using **InsightFace**, recording attendance, and providing APIs for both the Raspberry Pi client and the web dashboard.

---

# Responsibilities

The backend performs the following tasks:

- 📷 Receives image frames from the Raspberry Pi
- 👤 Detects faces in each image
- 🧠 Recognizes registered users using InsightFace
- 📝 Records attendance
- 🚫 Prevents duplicate attendance entries
- 📊 Serves attendance data to the web dashboard
- 🔄 Returns recognition results to the Raspberry Pi

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| InsightFace | Face detection & recognition |
| OpenCV | Image processing |
| NumPy | Mathematical operations |
| ONNX Runtime | Runs the AI model |

---

# Folder Structure

```text
backend/
│
├── README.md
├── main.py
├── requirements.txt
└── known_faces/
    ├── README.md
    └── *.jpg
```

---

# API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/recognize` | POST | Receives an image and returns the recognized face(s). |
| `/attendance-today` | GET | Returns today's attendance count and names. |
| `/status` | GET | Returns the latest recognition status. |

---

# Request Flow

```text
Raspberry Pi
      │
      ▼
POST /recognize
      │
      ▼
FastAPI Backend
      │
      ▼
InsightFace Model
      │
      ▼
Face Matching
      │
      ▼
Attendance Logic
      │
      ▼
JSON Response
```

---

# Face Recognition Pipeline

1. The Raspberry Pi captures a webcam frame.
2. The image is sent to the `/recognize` endpoint.
3. The backend decodes the uploaded image using OpenCV.
4. InsightFace detects face(s) and generates embeddings.
5. Embeddings are compared with registered faces using cosine similarity.
6. If the confidence exceeds the configured threshold, the person is recognized.
7. The recognition result is returned to the Raspberry Pi.

---

# Attendance Logic

When a face is successfully recognized:

- The person's name is identified.
- The current date and time are recorded.
- Duplicate attendance for the same person on the same day is prevented.
- The attendance dashboard is updated through the API.

Attendance is stored in:

```text
attendance.csv
```

---

# Running the Backend

## 1. Activate the Conda environment

```bash
conda activate face-server
```

## 2. Navigate to the backend directory

```bash
cd backend
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Start the server

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

The backend will be available at:

```text
http://<YOUR_IP_ADDRESS>:8000
```

---

# Main Components

## main.py

Contains:

- FastAPI application
- API endpoints
- Face recognition logic
- Attendance management
- Dashboard APIs

## known_faces/

Stores images of registered users. During startup, each image is processed and converted into a face embedding for later comparison.

---

# Future Improvements

- Database integration (MySQL/PostgreSQL)
- Docker support
- JWT authentication
- Face registration API
- Cloud deployment
- Model configuration through environment variables

---

# Related Modules

This backend works together with:

- `raspberry-pi/live_client.py` – Captures webcam frames and communicates with the backend.
- `frontend/attendance.html` – Displays attendance information in real time.

---

For an overview of the complete project architecture, refer to the repository's main `README.md`.
