import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Taask Week3 - F1D02310144-M. Bayu Aji")
        self.setGeometry(200, 200, 500, 400)
        self.setMouseTracking(True)
        self.setStyleSheet("background-color: #2b2b2b;")
        
        self.label = QLabel(self)
        self.label.setStyleSheet("color: white; font-size: 14px; background-color: rgba(70, 130, 180, 180);")
        self.label.setText("X: 0, Y: 0")
        self.label.move(random.randint(50, 450), random.randint(50, 350))
        self.label.adjustSize()
        self.label.installEventFilter(self)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        self.label.setText(f"X: {event.x()}, Y: {event.y()}")
        self.label.adjustSize()
    
    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == event.Enter:
            self.label.move(random.randint(50, self.width() - 50), random.randint(50, self.height() - 50))
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())