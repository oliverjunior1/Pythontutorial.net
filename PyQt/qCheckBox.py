# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
# from PyQt6.QtCore import Qt

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QCheckBox')
#         self.setGeometry(100,100,320,210)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         checkbox = QCheckBox('I Agree', self)

#         layout.addWidget(checkbox, 0,0, Qt.AlignmentFlag.AlignCenter)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
# from PyQt6.QtCore import Qt

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QCheckBox')
#         self.setGeometry(100, 100, 320, 210)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         checkbox = QCheckBox('I agree', self)
#         checkbox.stateChanged.connect(self.on_checkbox_changed)

#         layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

#         self.show()

#     def on_checkbox_changed(self, value):
#         state = Qt.CheckState(value)
#         if state == Qt.CheckState.Checked:
#             print('Checked')
#         elif state == Qt.CheckState.Unchecked:
#             print('Unchecked')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout
# from PyQt6.QtCore import Qt

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QCheckBox')
#         self.setGeometry(100,100,320,210)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         self.checkbox = QCheckBox('I agree', self)

#         check_button = QPushButton('Check', self)
#         check_button.clicked.connect(self.check)

#         uncheck_button = QPushButton('Uncheck', self)
#         uncheck_button.clicked.connect(self.check)

#         layout.addWidget(self.checkbox, 0,0,0,2, Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(check_button, 1, 0)
#         layout.addWidget(uncheck_button, 1,1)

#         self.show()

#     def check(self):
#         self.checkbox.setChecked(True)

#     def uncheck(self):
#         self.checkbox.setChecked(False)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100,100,320,210)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox =QCheckBox('A Tristate Checkbox', self)
        self.checkbox.setTristate(True)

        layout.addWidget(self.checkbox, 0,0, Qt.AlignmentFlag.AlignCenter)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

