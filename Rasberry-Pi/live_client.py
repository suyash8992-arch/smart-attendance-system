import datetime
import os
import cv2
import requests
import time
from RPLCD.i2c import CharLCD

# LCD init (change 0x27 if needed)
lcd = CharLCD('PCF8574', 0x27)

def display_message(line1="", line2=""):
    last_displayed_name = ""
    lcd.clear()
    lcd.write_string(f"{line1}\n{line2}")

ATTENDANCE_FILE = "attendance.csv"
url = "http://127.0.0.1:8000/recognize"


# =========================
# ATTENDANCE FUNCTION (FIXED)
# =========================
def mark_attendance(name):
    print("\n--- MARK ATTENDANCE CALLED ---")
    print("Name:", name)

    if name == "Unknown":
        print("Skipping unknown")
        return

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # Create file if not exists
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w") as f:
            f.write("Name,Date,Time\n")

    # Read existing entries
    with open(ATTENDANCE_FILE, "r") as f:
        lines = f.readlines()

    # 🔥 FIXED duplicate logic (exact match)
    for line in lines:
        if line.startswith("Name"):
            continue

        existing_name, existing_date, _ = [x.strip() for x in line.strip().split(",")]

        print("Checking:", existing_name, existing_date)

        if existing_name == name and existing_date == date:
            print("Already marked → skipping")
            return

    # Write new entry
    print("Writing to CSV:", name)

    with open(ATTENDANCE_FILE, "a") as f:
        f.write(f"{name},{date},{time_now}\n")

    print(f"✅ Attendance marked: {name}")


# =========================
# CAMERA + CLIENT LOOP
# =========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

print("✅ Camera started. Press ESC to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    frame = cv2.resize(frame, (640, 480))

    _, img_encoded = cv2.imencode('.jpg', frame)

    try:
        response = requests.post(
            url,
            files={"file": ("frame.jpg", img_encoded.tobytes(), "image/jpeg")}
        )

        data = response.json()
        print("Response:", data)

        # =========================
        # HANDLE RESPONSE
        # =========================
        if data["faces_detected"] > 0:
            name = data["results"][0]["name"]
        if name != last_displayed_name:
    print("LCD:", name)

    if name != "Unknown":
        display_message("Welcome", name)
    else:
        display_message("Unknown", "Person")

    last_displayed_name = name
            confidence = data["results"][0]["confidence"]

            print("Detected:", name, "| Confidence:", confidence)

            # 🔥 IMPORTANT CONDITION
            if confidence > 0.5:
                mark_attendance(name)

    except Exception as e:
        print("❌ Request failed:", e)

    time.sleep(1)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()