# Contributing to Smart Attendance System

First of all, thank you for your interest in contributing to the **Smart Attendance System**.

This project was developed as part of a Diploma Minor Project with the goal of automating classroom attendance using **Raspberry Pi**, **FastAPI**, **OpenCV**, and **InsightFace**. We welcome contributions that improve the project, fix bugs, enhance documentation, or add new features.

---

# Ways to Contribute

You can contribute in many ways, including:

- 🐞 Reporting bugs
- ✨ Suggesting new features
- 🛠 Improving the backend
- 🍓 Enhancing the Raspberry Pi client
- 🖥 Improving the web dashboard
- 📚 Improving documentation
- ⚡ Optimizing performance
- 🧪 Testing and validation

---

# Development Setup

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/smart-attendance-system.git
cd smart-attendance-system
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Start the backend

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

## 4. Run the Raspberry Pi client

```bash
python3 raspberry-pi/live_client.py
```

---

# Coding Guidelines

Please follow these guidelines when contributing:

- Follow **PEP 8** coding conventions for Python.
- Use meaningful variable and function names.
- Keep functions modular and reusable.
- Add comments where the logic is not immediately obvious.
- Test your changes before submitting.
- Update documentation if your changes affect functionality.

---

# Commit Message Guidelines

Use clear and descriptive commit messages.

Examples:

```text
feat: add LCD timeout feature
fix: prevent duplicate attendance entries
docs: update README installation guide
refactor: improve face matching logic
```

Avoid messages like:

```text
update
final
test
working
```

---

# Pull Request Guidelines

Before submitting a pull request, please ensure:

- The project builds and runs successfully.
- Existing functionality has not been broken.
- New functionality has been tested.
- Documentation is updated where necessary.
- Commit history is clean and meaningful.

---

# Reporting Bugs

When opening a bug report, please include:

- Operating System
- Python Version
- Raspberry Pi Model
- Error message (if any)
- Steps to reproduce the issue
- Expected behavior
- Actual behavior

Providing this information helps us reproduce and resolve issues more efficiently.

---

# Feature Requests

If you would like to propose a new feature:

- Check whether it has already been suggested.
- Clearly explain the idea.
- Describe the expected benefit.
- Explain how it integrates with the existing system.

---

# Areas for Future Contributions

Some ideas for future improvements include:

- Database integration (MySQL/PostgreSQL)
- Docker support
- Cloud deployment
- Face registration portal
- Admin authentication
- Multi-camera support
- Attendance analytics
- Mobile application

---

# Code of Conduct

By contributing to this repository, you agree to follow our Code of Conduct and maintain a respectful, collaborative, and inclusive environment.

---

# Thank You

Every contribution—whether it is code, documentation, testing, or feedback—is appreciated.

Thank you for helping improve the **Smart Attendance System**!
