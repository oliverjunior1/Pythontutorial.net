# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         titles = ['Find Next', 'Find All', 'Close']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         self.show()

# if __name__== '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         titles = ['Find Next', 'Find All', 'Close']
#         buttons =[QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.addStretch()

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec()) 

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         layout.addStretch()

#         titles = ['Find Next', 'Find all', 'Close']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)

#         layout.addStretch()

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBOxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         find_next_btn = QPushButton('Find Next')
#         find_all_btn = QPushButton('Find All')
#         close_btn = QPushButton('Find All')

#         layout.addWidget(find_next_btn)
#         layout.addWidget(find_all_btn)

#         layout.addStretch()

#         layout.addWidget(close_btn)

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBOxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         label_1 = QLabel()
#         label_1.setStyleSheet('QLabel{background-color:red}')
#         label_2 = QLabel()
#         label_2.setStyleSheet('QLabel{background-color:green}')
#         label_3 = QLabel()
#         label_3.setStyleSheet('QLabel{background-color:blue}')

#         layout.addWidget(label_1)
#         layout.addWidget(label_2)
#         layout.addWidget(label_3)

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         label_1 = QLabel('')
#         label_1.setStyleSheet('QLabel{background-color:red}')

#         label_2 = QLabel('')
#         label_2.setStyleSheet('QLabel{background-color:green}')
        
#         label_3 = QLabel('')
#         label_3.setStyleSheet('QLabel{background-color:blue}')

#         layout.addWidget(label_1)
#         layout.addWidget(label_2)
#         layout.addWidget(label_3)

#         layout.setStretchFactor(label_1, 1)
#         layout.setStretchFactor(label_2, 2)
#         layout.setStretchFactor(label_3, 3)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())
        

####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt QVBoxLayout')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         label_1 = QLabel('')
#         label_1.setStyleSheet('QLabel{background-color:red}')

#         label_2 = QLabel('')
#         label_2.setStyleSheet('QLabel{background-color:green}')

#         label_3 = QLabel('')
#         label_3.setStyleSheet('QLabel{background-color:blue}')

#         layout.addWidget(label_1)
#         layout.addWidget(label_2)
#         layout.addWidget(label_3)

#         layout.setSpacing(0)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

####################################################

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QVBoxLayout')

        layout = QVBoxLayout()
        self.setLayout(layout)

        label_1 = QLabel()
        label_1.setStyleSheet('QLabel{background-color:red}')

        label_2 = QLabel()
        label_2.setStyleSheet('QLabel{background-color:green}')

        label_3 = QLabel()
        label_3.setStyleSheet('QLabel{background-color:blue}')

        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)

        layout.setContentsMargins(0,0,0,0)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


