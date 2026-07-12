from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import os
from insightface.app import FaceAnalysis
from datetime import date, datetime
from fastapi.responses import FileResponse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "attendance.csv")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def serve_ui():
    return FileResponse("static/attendance.html")
# =========================
# MODEL LOAD
# =========================
model = FaceAnalysis(name="buffalo_l")
model.prepare(ctx_id=0)

# =========================
# STORAGE
# =========================
known_embeddings = []
known_names = []

latest_result = {
    "name": "None",
    "confidence": 0.0,
    "status": "Idle"
}

# =========================
# LOAD KNOWN FACES
# =========================
def load_known_faces():
    folder = "known_faces"

    for file in os.listdir(folder):
        if file.startswith("."):
            continue

        path = os.path.join(folder, file)
        img = cv2.imread(path)

        if img is None:
            continue

        faces = model.get(img)

        if len(faces) > 0:
            embedding = faces[0].embedding
            known_embeddings.append(embedding)

            name = os.path.splitext(os.path.basename(file))[0]
            name = name.split(":")[-1]
            known_names.append(name)

            print(f"✅ Loaded: {name}")

load_known_faces()

# =========================
# MATCH FUNCTION
# =========================
def find_match(embedding):
    if len(known_embeddings) == 0:
        return "Unknown", 0.0

    similarities = []

    for known_embedding in known_embeddings:
        sim = np.dot(embedding, known_embedding) / (
            np.linalg.norm(embedding) * np.linalg.norm(known_embedding)
        )
        similarities.append(sim)

    max_index = np.argmax(similarities)
    max_similarity = similarities[max_index]

    if max_similarity > 0.5:
        return known_names[max_index], float(max_similarity)
    else:
        return "Unknown", float(max_similarity)

# =========================
# 🔥 HELPER: Ensure CSV exists
# =========================
def ensure_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w") as f:
            f.write("name,date,time\n")   # header

# =========================
# API ENDPOINT
# =========================
@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    global latest_result

    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if img is None:
        latest_result["status"] = "Invalid Image"
        return {"error": "Invalid image"}

    faces = model.get(img)
    results = []

    if len(faces) == 0:
        latest_result["status"] = "No Face"
    else:
        for face in faces:
            embedding = face.embedding
            name, confidence = find_match(embedding)

            results.append({
                "name": name,
                "confidence": confidence
            })

            latest_result["name"] = name
            latest_result["confidence"] = confidence
            latest_result["status"] = "Recognized"

            # =========================
            # 🔥 ADD THIS BLOCK (WRITE CSV)
            # =========================
            if name != "Unknown":
                ensure_csv()

                today = datetime.now().strftime("%Y-%m-%d")
                current_time = datetime.now().strftime("%H:%M:%S")

                # prevent duplicates for today
                already_marked = set()

                with open(CSV_PATH, "r") as f:
                    next(f)  # skip header
                    for line in f:
                        n, d, _ = [x.strip() for x in line.strip().split(",")]
                        if d == today:
                            already_marked.add(n)

                if name not in already_marked:
                    with open(CSV_PATH, "a") as f:
                        f.write(f"{name},{today},{current_time}\n")

                    print(f"✅ Attendance stored: {name}")
            # =========================

    return {
        "faces_detected": len(faces),
        "results": results
    }

# =========================
# UI STATUS
# =========================
@app.get("/status")
def get_status():
    return latest_result

# =========================
# ATTENDANCE API
# =========================
@app.get("/attendance-today")
def get_today_attendance():

    if not os.path.exists(CSV_PATH):
        return {"count": 0, "names": []}

    today = datetime.now().strftime("%Y-%m-%d")
    names = set()

    with open(CSV_PATH, "r") as f:
        next(f)  # skip header
        for line in f:
            name, d, _ = [x.strip() for x in line.strip().split(",")]
            if d == today:
                names.add(name)

    return {
        "count": len(names),
        "names": list(names)
    }