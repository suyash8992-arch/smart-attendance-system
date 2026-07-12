# Frontend - Smart Attendance System

The **frontend** provides a lightweight, browser-based dashboard for monitoring attendance in real time. It communicates with the FastAPI backend to display the latest attendance records and provides a simple interface suitable for classroom demonstrations and daily use.

---

# Responsibilities

The frontend is responsible for:

- 🖥️ Displaying today's attendance
- 👥 Showing the names of recognized students
- 📊 Displaying the total attendance count
- 🔄 Automatically refreshing attendance information
- 🌐 Communicating with the FastAPI backend using REST APIs

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| JavaScript | Dynamic updates |
| Fetch API | Backend communication |

---

# Folder Structure

```text
frontend/
│
├── README.md
└── attendance.html
```

---

# How It Works

```text
Browser
    │
    ▼
attendance.html
    │
    ▼
Fetch API Request
    │
    ▼
GET /attendance-today
    │
    ▼
FastAPI Backend
    │
    ▼
JSON Response
    │
    ▼
Dashboard Updates
```

The dashboard periodically requests attendance information from the backend and updates the page without requiring the user to reload the browser.

---

# API Used

## GET /attendance-today

Returns the attendance recorded for the current day.

Example response:

```json
{
  "count": 3,
  "names": [
    "Suyash",
    "Rahul",
    "Aman"
  ]
}
```

The frontend uses this response to display:

- Total students present
- List of recognized students

---

# Running the Frontend

## Option 1 — Python HTTP Server

Navigate to the frontend directory:

```bash
cd frontend
```

Start a local web server:

```bash
python3 -m http.server 5500
```

Open your browser:

```text
http://localhost:5500/attendance.html
```

or

```text
http://<YOUR_COMPUTER_IP>:5500/attendance.html
```

---

# Features

- Live attendance updates
- Lightweight interface
- Browser-based access
- Automatic refresh
- Simple and responsive design
- Easy integration with the FastAPI backend

---

# Future Improvements

Possible enhancements include:

- Student photographs
- Attendance history
- Search and filter
- Export attendance (CSV/PDF)
- Graphs and analytics
- Admin authentication
- Mobile-friendly UI
- Dark mode

---

# Related Modules

The frontend works together with:

- `backend/main.py` – Provides attendance and recognition APIs.
- `raspberry-pi/live_client.py` – Captures webcam frames and communicates with the backend.

For the complete project architecture and setup instructions, refer to the repository's main **README.md**.
