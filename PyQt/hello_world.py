# from PyQt6.QtWidgets import QApplication, QWidget

# app= QApplication([])

# window = QWidget(windowTitle = 'Hello World')
# window.show()

# app.exec()

#####################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget


# # create the QApplication
# app = QApplication(sys.argv)

# # create the main window
# window = QWidget(windowTitle='Hello World')
# window.show()

# # start the event loop
# sys.exit(app.exec())

#####################################################

import sys
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # set the window title
        self.setWindowTitle('Hello World')
        
        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())