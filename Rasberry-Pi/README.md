# Raspberry Pi Client

The **Raspberry Pi** acts as the client device in the Smart Attendance System. It is responsible for capturing images from a USB webcam, sending them to the FastAPI backend for face recognition, displaying recognition results on a 16×2 LCD, and receiving attendance responses in real time.

---

# Responsibilities

The Raspberry Pi performs the following tasks:

- 📷 Captures live frames from a USB webcam
- 🌐 Sends images to the FastAPI backend over HTTP
- 📥 Receives face recognition results
- 📟 Displays the recognized person's name on a 16×2 LCD
- 📝 Marks attendance through the backend
- 🔄 Repeats the process continuously for real-time recognition

---

# Hardware Used

| Component | Purpose |
|-----------|---------|
| Raspberry Pi Zero 2 W | Client device |
| USB Webcam | Image capture |
| 16×2 LCD Display (I²C) | Display recognition status |
| MicroSD Card | Raspberry Pi OS |
| Wi-Fi | Communication with backend |

---

# Software Stack

| Technology | Purpose |
|-----------|---------|
| Python | Programming language |
| OpenCV | Webcam capture |
| Requests | HTTP communication |
| RPLCD | LCD control |
| smbus2 | I²C communication |
| FastAPI | Backend communication |

---

# Folder Structure

```text
raspberry-pi/
│
├── README.md
├── requirements.txt
└── live_client.py
```

---

# Workflow

```text
USB Webcam
      │
      ▼
Capture Frame
      │
      ▼
Compress Image (JPEG)
      │
      ▼
Send HTTP POST Request
      │
      ▼
FastAPI Backend
      │
      ▼
Receive JSON Response
      │
      ▼
Display Name on LCD
      │
      ▼
Repeat
```

---

# How It Works

1. OpenCV captures frames from the USB webcam.
2. Each frame is resized and encoded as JPEG.
3. The frame is sent to the backend using an HTTP POST request.
4. The backend recognizes the face and returns a JSON response.
5. If a known person is detected:
   - Their name is shown on the LCD.
   - Attendance is recorded by the backend.
6. If the face is unknown, the LCD displays an appropriate message.
7. The process repeats continuously.

---

# Running the Raspberry Pi Client

## Install dependencies

```bash
pip install -r requirements.txt
```

## Update the backend IP

Edit `live_client.py` and set the backend URL:

```python
url = "http://<BACKEND_IP>:8000/recognize"
```

Replace `<BACKEND_IP>` with the IP address of the computer running the FastAPI backend.

## Run the client

```bash
python3 live_client.py
```

---

# LCD Behaviour

The LCD provides immediate feedback to the user.

Examples:

```text
Welcome
Suyash
```

or

```text
Unknown
Person
```

The display automatically clears after the configured timeout to avoid stale information remaining on screen.

---

# Network Requirements

- Raspberry Pi and backend computer must be connected to the same network.
- The backend server must be running before starting the Raspberry Pi client.
- If the network changes, update the backend IP address in `live_client.py`.

---

# Future Improvements

- Automatic backend discovery
- HTTPS communication
- Offline attendance caching
- Camera status monitoring
- OLED display support
- Configuration file for network settings

---

# Related Modules

- `backend/main.py` – Performs face recognition and attendance management.
- `frontend/attendance.html` – Displays attendance records through a web dashboard.

For the complete project overview, see the repository's main `README.md`.
