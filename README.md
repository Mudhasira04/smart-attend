Face Recognition Based Attendance System
A Python-based Face Recognition Attendance System with an intuitive Graphical User Interface (GUI) that automates attendance marking using real-time facial recognition.
This project eliminates manual attendance processes by accurately identifying individuals through facial features and recording attendance with precise date and time stamps. The system is designed to be simple, secure, and practical for real-world academic or organizational use.
📌 Project Overview
The system captures facial data, trains a recognition model, and uses live camera input to identify registered users. Once recognized, attendance is automatically marked and stored in structured CSV files.
A user-friendly GUI ensures that even non-technical users can operate the system easily.
🚀 Key Features
Interactive and easy-to-use GUI
Face recognition–based attendance using live camera feed
Password-protected registration for adding new users
Automatic creation and updating of student details CSV
Generates a new attendance CSV file every day
Attendance records include ID, Name, Date, and Time
Live attendance display in tabular format
Secure password change option from the menu
🛠️ Technologies Used
Python
Tkinter – GUI development
OpenCV (cv2) – Image processing and face recognition
LBPH Face Recognizer
NumPy – Numerical operations
Pandas – Data handling
CSV – Attendance storage
Datetime – Date and time management
🖥️ System Workflow
User Registration
Admin registers a new user with ID and name
Facial images are captured and stored
Model is trained using captured images
Attendance Marking
Live camera detects and recognizes faces
Recognized users are marked present automatically
Attendance is saved with exact date and time
Attendance Management
Daily attendance stored in separate CSV files
Live attendance shown on the main screen
🔐 Security
Password protection for:
New user registration
Changing system password
Prevents unauthorized access to system controls
📂 Project Structure (Overview)
Copy code

Face_Recognition_Attendance_System/
│
├── Attendance/        # Daily attendance CSV files
├── StudentDetails/    # Registered student information
├── TrainingImage/     # Captured face images
├── TrainingImageLabel/# Trained model files
├── haarcascade_frontalface_default.xml
├── main.py            # Main application file
└── README.md
📸 Screenshots
Main Screen
(GUI home interface showing system options)
Taking Attendance
(Live face detection and recognition in progress)
Attendance Display
(Tabular view of marked attendance with date and time)
Help Menu
(User guidance and system information)
Change Password
(Secure password update interface)
🎯 Use Cases
College and school attendance systems
Office employee attendance
Labs and training centers
Small organizations seeking low-cost automation
📈 Future Enhancements
Database integration (MySQL / PostgreSQL)
Cloud-based attendance storage
Web or mobile app version
Mask detection support
Multi-camera support
