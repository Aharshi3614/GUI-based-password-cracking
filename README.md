🔐 Password Audit Tool
A lightweight desktop application built with Python & Tkinter that analyzes password strength in real time and provides actionable feedback to help users create stronger passwords.

📸 Features

⚡ Real-time analysis — strength updates as you type
📊 Visual progress bar — color-coded from red (weak) to green (strong)
✅ 5-point scoring system based on security best practices
🚫 Common password detection — flags passwords like 123456, qwerty
💡 Instant feedback — tells you exactly what to improve


🧠 How Scoring Works
CriteriaPointsAt least 8 characters+1Contains uppercase letter (A-Z)+1Contains lowercase letter (a-z)+1Contains a number (0-9)+1Contains special character (!@#$%^&*)+1Common password detectedScore → 0
ScoreStrength LabelBar Color0Very Weak🔴 Red1Weak🟠 Orange2Moderate🟡 Yellow3Strong🟢 Light Green4-5Very Strong💚 Green

🛠️ Requirements

Python 3.x
tkinter (included with standard Python installation)

No external packages needed.

🚀 Installation & Run
bash# Clone the repository
git clone https://github.com/your-username/password-audit-tool.git
cd password-audit-tool

# Run the app
python password_audit.py

📁 Project Structure
password-audit-tool/
├── password_audit.py   # Main application file
└── README.md           # Project documentation

📌 Usage

Launch the app
Type a password in the input field
Watch the strength bar and feedback update instantly
Follow the suggestions to improve your password


