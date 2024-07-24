# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt6.QtGui import QFont

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt Label Widget')
#         self.setGeometry(100,100,320,210)

#         label = QLabel('This is a QLabel widget')

#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

#         self.show()

# if __name__== '__main__':
#     app = QApplication(sys.argv)

#     window = MainWindow()

#     sys.exit(app.exec())

#####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt6.QtGui import QPixmap

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt Label Widget')
#         self.setGeometry(100,100,320,210)

#         label = QLabel()
#         pixmap = QPixmap('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\Pythontutorial.net\\PyQt\\python-logo.png')
#         label.setPixmap(pixmap)

#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     window = MainWindow()

#     sys.exit(app.exec())

#####################################################
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLabel Widget')
        self.setGeometry(100,100,320,210)

        label = QLabel()
        movie = QMovie('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\Pythontutorial.net\\PyQt\\Python.gif')
        label.setMovie(movie)
        movie.start()

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())

