import sys # Allows handle the exit status of app

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv) # Create an instance of application

# Create window and add elements to it
window = QWidget()
window.setWindowTitle("PyQt5 App")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

window.show() # Show application
sys.exit(app.exec_()) # Start application (+ exit it successfuly)