# import sys
# from PyQt6.QtWidgets import (
#     QApplication, 
#     QWidget, 
#     QFileDialog, 
#     QGridLayout,
#     QPushButton, 
#     QLabel,
#     QListWidget
# )
# from pathlib import Path


# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt File Dialog')
#         self.setGeometry(100, 100, 300, 150)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         # file selection
#         file_browser_btn = QPushButton('Browse')
#         file_browser_btn.clicked.connect(self.open_file_dialog)

#         self.file_list = QListWidget(self)

#         layout.addWidget(QLabel('Files:'), 0, 0)
#         layout.addWidget(self.file_list, 1, 0)
#         layout.addWidget(file_browser_btn, 2 ,0)

#         self.show()

#     def open_file_dialog(self):
#         dialog = QFileDialog(self)
#         dialog.setDirectory(r'C:\images')
#         dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
#         dialog.setNameFilter("Images (*.png *.jpg)")
#         dialog.setViewMode(QFileDialog.ViewMode.List)
#         if dialog.exec():
#             filenames = dialog.selectedFiles()
#             if filenames:
#                 self.file_list.addItems([str(Path(filename)) for filename in filenames])


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#########################################################################################

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout,QLineEdit,QPushButton, QLabel
# from pathlib import Path

# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt File Dialog')
#         self.setGeometry(100, 100, 400, 100)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         # file selection
#         file_browse = QPushButton('Browse')
#         file_browse.clicked.connect(self.open_file_dialog)
#         self.filename_edit = QLineEdit()

#         layout.addWidget(QLabel('File:'), 0, 0)
#         layout.addWidget(self.filename_edit, 0, 1)
#         layout.addWidget(file_browse, 0 ,2)

      
#         self.show()


#     def open_file_dialog(self):
#         filename, ok = QFileDialog.getOpenFileName(
#             self,
#             "Select a File", 
#             "D:\\icons\\avatar\\", 
#             "Images (*.png *.jpg)"
#         )
#         if filename:
#             path = Path(filename)
#             self.filename_edit.setText(str(path))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#########################################################################################

# import sys
# from PyQt6.QtWidgets import QApplication,  QFileDialog, QWidget, QGridLayout, QListWidget, QPushButton, QLabel
# from pathlib import Path


# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('PyQt File Dialog')
#         self.setGeometry(100, 100, 400, 100)

#         layout = QGridLayout()
#         self.setLayout(layout)

#         # file selection
#         file_browse = QPushButton('Browse')
#         file_browse.clicked.connect(self.open_file_dialog)

#         self.file_list = QListWidget(self)

#         layout.addWidget(QLabel('Selected Files:'), 0, 0)
#         layout.addWidget(self.file_list, 1, 0)
#         layout.addWidget(file_browse, 2, 0)

#         self.show()

#     def open_file_dialog(self):
#         filenames, _ = QFileDialog.getOpenFileNames(
#             self,
#             "Select Files",
#             r"C:\\images\\",
#             "Images (*.png *.jpg)"
#         )
#         if filenames:
#             self.file_list.addItems([str(Path(filename))
#                                      for filename in filenames])


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

#########################################################################################
import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from pathlib import Path

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100,100,400,100)

        layout = QGridLayout()
        self.setLayout(layout)

        dir_btn = QPushButton('Browse')
        dir_btn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit = QLineEdit()

        layout.addWidget(QLabel('Directory:'),1,0)
        layout.addWidget(self.dir_name_edit, 1,1)
        layout.addWidget(dir_btn,1,2)

        self.show()

    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select a Directory')
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())