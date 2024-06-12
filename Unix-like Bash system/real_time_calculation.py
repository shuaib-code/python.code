import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
import webbrowser

def calculate():
    try:
        x = int(x_value.text())
        results = {
            "Stamp": abs(x * 15 - 100),
            "Ragi": x * 10 + 388,
            "Sub Ragi": x * 30,
            "SR": x * 20,
            "Sub total": x * 75 + 520
        }
        result_content = "\n".join([f"{k}: {v}" for k, v in results.items()])
    except ValueError:
        result_content = "Please enter a valid integer value for X."
    result_label.setText(result_content)

def open_facebook():
    webbrowser.open("https://www.facebook.com/shuaib.code")

# Hexadecimal to character conversion
hC = ['4d', '6f', '68', '61', '6d', '6d', '61', '64', '20', '53', '68', '75', '61', '69', '62']
nA = [chr(int(h, 16)) for h in hC]
name = "".join(nA)

# Initialize the application
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Real-time Calculation")
window.setGeometry(100, 100, 400, 450)
window.setStyleSheet("background-color: #ffffff; color: #1f2937;")

# Create the layout
layout = QVBoxLayout()

# Header
header = QLabel("Real-time Calculation")
header.setFont(QFont("Arial", 24, QFont.Bold))
header.setStyleSheet("color: #6366f1;")
header.setAlignment(Qt.AlignCenter)
layout.addWidget(header)

# Input label and entry
input_label = QLabel("Enter the value of X:")
input_label.setFont(QFont("Arial", 18))
input_label.setStyleSheet("color: #374151;")
layout.addWidget(input_label)

x_value = QLineEdit()
x_value.setFont(QFont("Arial", 14))
x_value.setStyleSheet("color: #374151; background-color: #f9fafb; border: 1px solid #d1d5db;")
x_value.textChanged.connect(calculate)  # Connect the textChanged signal to the calculate function
layout.addWidget(x_value)

# Result box
result_label = QTextEdit()
result_label.setFont(QFont("Courier", 14))
result_label.setStyleSheet("color: #1f2937; background-color: #f3f4f6; border: 1px solid #6366f1;")
result_label.setReadOnly(True)
layout.addWidget(result_label)

# Note
note_label = QLabel("This request was made by Sayed Al Walid.")
note_label.setFont(QFont("Arial", 12))
note_label.setStyleSheet("color: #6b7280; opacity: 0.6;")
layout.addWidget(note_label)

# Footer
footer_layout = QHBoxLayout()

footer_text = QLabel(f"© 2024 {name}")
footer_text.setFont(QFont("Arial", 14))
footer_text.setStyleSheet("color: #6b7280;")
footer_layout.addWidget(footer_text)

# Facebook icon button
fb_button = QPushButton()
fb_button.setIcon(QIcon("facebook_icon.png"))
fb_button.setIconSize(QSize(24, 24))
fb_button.setStyleSheet("background-color: #ffffff; border: none;")
fb_button.clicked.connect(open_facebook)
footer_layout.addWidget(fb_button)

layout.addLayout(footer_layout)

# Set the layout and show the window
window.setLayout(layout)
window.show()

# Run the application
sys.exit(app.exec_())
