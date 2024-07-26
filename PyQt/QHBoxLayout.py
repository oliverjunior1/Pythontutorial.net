# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, *kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.addStretch()

#         self.show()

# if __name__ =='__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         layout.addStretch()

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         layout.addStretch()

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.addStretch()

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]

#         layout.addWidget(buttons[0])
#         layout.addWidget(buttons[1])

#         layout.addStretch()

#         layout.addWidget(buttons[2])

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout =QHBoxLayout()
#         self.setLayout(layout)

#         titles= ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.setStretchFactor(buttons[0], 2)
#         layout.setStretchFactor(buttons[1], 2)
#         layout.setStretchFactor(buttons[2], 1)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# class MianWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QHBoxLayout')

#         layout =QHBoxLayout()
#         self.setLayout(layout)

#         titles = ['Yes', 'No', 'Cancel']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.setSpacing(50)

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = MianWindow()
#     sys.exit(app.exec())

#################################################

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        layout = QHBoxLayout()
        self.setLayout(layout)

        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        layout.setContentsMargins(50,50,50,50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())