import subprocess
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QGridLayout, QPushButton, QLineEdit, QTextEdit, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


#Global Dictionary
widget = {"logo": [],
          "button": [],
          "ip_input": [],
          "result_frame": []}

# Block creates window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("NMAP Recon Tool")
window.setFixedWidth(1000)
window.setStyleSheet("background: black;")
window.setFixedHeight(1000)

grid = QGridLayout()

# set up a text box to display results
result_text = QTextEdit()
result_text.setReadOnly(True)# Make it read-only
result_text.setStyleSheet(
    "color: white;" +
    "font-size: 15px;"
)


widget["result_frame"].append(result_text)
grid.addWidget(widget["result_frame"][-1], 3, 0, 1, 2)

def append_results(scan_result):
    widget["result_frame"][-1].setPlainText(scan_result)  # Display the result in the QTextEdit widget


def Start():
    start_scan()
    recon()
    append_results()

# The Main Function Start Scan
def start_scan():
    ip = widget["ip_input"][-1].text()
    if ip:
        scan_result = recon(ip)
        widget["result_frame"][-1].setPlainText(scan_result)#Display the result in the QTextEdit widget
        # append the result frame to the result texts
    else:
        print("Please enter an IP address.")

# Function to perform the Nmap scan
#def recon(ip):
    #os.system(f"nmap -p80 -Pn {ip} -v")
    #print(f"It works", ip)
# Function to perform the Nmap scan and return results
def recon(ip):
    try:
        result = subprocess.run(["nmap", "-p80", "-Pn", ip, "-v"], capture_output=True, text=True, check=True)
        captured_output = result.stdout
        print(captured_output)  # Print the captured output for debugging
        return captured_output
    except subprocess.CalledProcessError as e:
        return f"Error: {e}\nNmap command failed."



# First Frame last line appends the global widget logo to the variable logo which is the image we are using in function
def frame1():
    image = QPixmap("nmap.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("Margin-top: 75px; Margin-bottom: 100px")
    widget["logo"].append(logo)

    # Create and set up IP Input field widget
    ip_input = QLineEdit()
    ip_input.setPlaceholderText("Enter IP Address to Scan")
    ip_input.setAlignment(QtCore.Qt.AlignCenter)
    ip_input.setStyleSheet(
        "*{border: 2px solid '#8B0082';" +
        "border-radius: 45px;" +
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 15px 20px;" +
        "margin: 10px 200px}" +
        "*:focus{border: 2px solid purple;}"
    )
    widget["ip_input"].append(ip_input)




    #Button Widget
    button = QPushButton("Start Scan")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#8B0082';" +
        "border-radius: 45px;" +
        "font-size: 45px;" +
        "color: 'white';" +
        "padding: 15px 0;" +
        "margin: 100px 200px}" +
        "*:hover{background: '#8B0082';}"
    )
    widget["button"].append(button)

    button.clicked.connect(start_scan)

    grid.addWidget(widget["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widget["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widget["ip_input"][-1], 1, 0, 1, 2)







frame1()

# Apply grid to the window
window.setLayout(grid)


#Shows and exits out of window
window.show()
sys.exit(app.exec())

