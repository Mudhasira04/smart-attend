# Face Recognition Based Attendance System

A Python-based Face Recognition Attendance System with an intuitive GUI that automates attendance marking using real-time facial recognition. The system captures facial data, trains a recognition model, and uses a live camera feed to identify registered users and mark attendance with date and time stamps.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [System Workflow](#system-workflow)
- [Security](#security)
- [Project Structure](#project-structure-overview)
- [Screenshots](#screenshots)
- [Use Cases](#use-cases)
- [Future Enhancements](#future-enhancements)
- [Installation & Usage](#installation--usage)

---

## Project Overview

This project eliminates manual attendance processes by identifying individuals through facial features and recording attendance automatically. A user-friendly GUI makes it accessible for non-technical users.

---

## Key Features

- Interactive, easy-to-use GUI
- Face recognition–based attendance using the live camera feed
- Password-protected registration for adding new users
- Automatic creation and updating of student details CSV
- Generates a new attendance CSV file every day
- Attendance records include ID, Name, Date, and Time
- Live attendance display in a tabular format
- Secure password change option available from the menu

---

## Technologies Used

- Python
- Tkinter (GUI)
- OpenCV (cv2) — image processing and face recognition
- LBPH Face Recognizer
- NumPy
- Pandas
- CSV
- datetime

---

## System Workflow

1. User Registration
   - Admin registers a new user with ID and name.
   - Facial images are captured and stored.
   - The recognition model is trained using the captured images.

2. Attendance Marking
   - Live camera detects and recognizes faces.
   - Recognized users are marked present automatically.
   - Attendance is saved with exact date and time.

3. Attendance Management
   - Daily attendance is stored in separate CSV files.
   - Live attendance is shown on the main screen.

---

## Security

- Password protection for:
  - New user registration
  - Changing the system password
- Prevents unauthorized access to admin controls

---

## Project Structure (Overview)

```text
Face_Recognition_Attendance_System/
│
├── Attendance/            # Daily attendance CSV files
├── StudentDetails/        # Registered student information CSVs
├── TrainingImage/         # Captured face images
├── TrainingImageLabel/    # Trained model files
├── haarcascade_frontalface_default.xml
├── main.py                # Main application file
└── README.md
```

---

## Use Cases

- College and school attendance systems  
- Office employee attendance  
- Labs and training centers  
- Small organizations seeking a low-cost automation solution

---

## Future Enhancements

- Database integration (MySQL / PostgreSQL)
- Cloud-based attendance storage
- Web or mobile app version
- Mask detection support
- Multi-camera support

---

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Mudhasira04/smart-attend.git
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install opencv-python numpy pandas
   ```
   (Also ensure Tkinter is available on your system; it is usually bundled with Python on Windows and macOS.)
4. Run the application:
   ```bash
   python main.py
   ```
5. Use the GUI to register users, train the model, and take attendance.

---
