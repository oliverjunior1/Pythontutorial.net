# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLineEdit,
#     QPushButton,
#     QVBoxLayout
# )

# class mainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('Qt Signals & Slots')

#         button = QPushButton('Click-me')
#         button.clicked.connect(self.button_clicked)

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         layout.addWidget(button)

#         self.show()

#     def button_clicked(self):
#         print('clicked')

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = mainWindow()
#     sys.exit(app.exec())

#####################################################

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        
