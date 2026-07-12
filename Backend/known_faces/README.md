# Known Faces Directory

This directory stores the reference face images used by the Smart Attendance System for face recognition.

During backend startup, each image in this folder is processed using the **InsightFace** model to generate a face embedding. These embeddings are stored in memory and used to recognize individuals during attendance.

---

# Purpose

This folder acts as the local face database for the system.

Each image should represent **one registered person**.

---

# Supported Formats

The following image formats are recommended:

- `.jpg`
- `.jpeg`
- `.png`

---

# Naming Convention

Use the person's name as the filename.

### Examples

```text
Alice.jpg
Rahul.png
John_Doe.jpeg
```

The filename (without the extension) will be used as the person's name in the attendance records.

---

# Image Guidelines

For the best recognition accuracy:

- Use a clear, high-resolution image.
- Ensure only one face is visible.
- Face should be looking toward the camera.
- Avoid sunglasses, masks, or heavy obstructions.
- Use good lighting.
- Avoid blurry or low-quality images.

---

# Privacy Notice

This public repository does **not** include real user face images.

If you are using this project, add your own reference images to this folder before running the backend.

---

# Loading Process

When the backend starts:

1. The backend scans this folder.
2. Each image is loaded using OpenCV.
3. InsightFace detects the face.
4. A face embedding is generated.
5. The embedding is stored in memory for future comparison.

---

# Example Folder Structure

```text
known_faces/
│
├── README.md
├── .gitkeep
├── Alice.jpg
├── Rahul.jpg
└── John_Doe.png
```

> In the public GitHub repository, only `README.md` and `.gitkeep` are included. Add your own images locally when using the project.

---

# Troubleshooting

If a face is not recognized:

- Verify the image contains exactly one clear face.
- Ensure the filename follows the naming convention.
- Restart the backend after adding new images so they are loaded into memory.

---

Thank you for using the Smart Attendance System!
