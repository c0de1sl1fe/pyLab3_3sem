import sys
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox)

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,

)

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


# labs imports
from task1 import Iterator1_img, create_csv
from task2 import copy_dataset
from task3 import create_dir_copy_randNames, create_dir_copy_randNames_both


class Example(QWidget):

    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.mainBtn = QPushButton("Main", self)
        self.task1Btn = QPushButton("Do task1")
        self.task2Btn = QPushButton("Do task 2")
        self.task3Btn = QPushButton("Do task 3")
        self.clearBtn = QPushButton("clear")
        self.nextBtn = QPushButton("next")
        self.iterator = Iterator1_img("test", "dataset")
        self.mainBtn.clicked.connect(self.__inputPath)

        # self.pixmap = QPixmap('blueLobster.jpg')
        self.pixmap = QPixmap('.jpg')

        self.lable = QLabel(self)
        self.name = "test"
        self.path = "dataset"
        self.initUI()

    def initUI(self):
        '''support constructor function'''

        self.setWindowTitle('Lab3')

        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.generalTab(), "general")
        tabs.addTab(self.showImageTab(), "show image")
        tabs.addTab(self.task1Tab(), "task1")
        tabs.addTab(self.task2Tab(), "task2")
        tabs.addTab(self.task3Tab(), "task3")

        self.iterator.setPath(self.path)
        layout.addWidget(tabs)

        self.setGeometry(300, 300, 350, 300)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.show()

    def generalTab(self):  # Main window with hello-words and descripition what's going on
        '''main window with hello-words and descripition what's going on'''

        generalTab = QWidget()
        layout = QVBoxLayout()
        # layout.addWidget(QPushButton("test1"))
        text = QVBoxLayout()
        line1 = QLabel("hello there")
        line2 = QLabel("at showImageTab you can view dataset's imgs")
        line3 = QLabel("at task1Tab create CSV file for dataset's classes")
        line4 = QLabel("at task2Tab you can copy dataset to new directory")
        line5 = QLabel("at task3Tab you can copy dataset with new names")
        text.addWidget(line1)
        text.addWidget(line2)
        text.addWidget(line3)
        text.addWidget(line4)
        text.addWidget(line5)
        layout.addLayout(text)
        layout.addWidget(self.mainBtn)

        layoutRadioButton = QHBoxLayout()
        radiobutton = QRadioButton("zebra")
        radiobutton.name = "zebra"
        radiobutton.toggled.connect(self.onClicked)
        layoutRadioButton.addWidget(radiobutton)

        radiobutton = QRadioButton("bay horse")
        radiobutton.name = "bay horse"
        radiobutton.toggled.connect(self.onClicked)
        layoutRadioButton.addWidget(radiobutton)
        radiobutton = QRadioButton("test")

        radiobutton.name = "test"
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.onClicked)

        layoutRadioButton.addWidget(radiobutton)
        layout.addLayout(layoutRadioButton)
        generalTab.setLayout(layout)
        return generalTab

    def showImageTab(self):  # image tab where user choose directory and see the img via _next_
        '''image tab where user choose directory and see the img via _next_'''
        generalTab = QWidget()
        layout = QVBoxLayout()

        layoutButton = QHBoxLayout()
        clearBtn = QPushButton("clear")
        clearBtn.clicked.connect(self.clearButton)
        nextBtn = QPushButton("next")
        nextBtn.clicked.connect(self.nextButton)
        layoutButton.addWidget(clearBtn)
        layoutButton.addWidget(nextBtn)

        # pixmap = QPixmap('blueLobster.jpg')
        self.lable.setPixmap(self.pixmap)
        layout.addWidget(self.lable)
        self.resize(self.pixmap.width(), self.pixmap.height())

        # layout.addLayout(layoutRadioButton)
        layout.addLayout(layoutButton)
        generalTab.setLayout(layout)
        return generalTab

    def tasksTab(self):
        generalTab = QWidget()
        layout = QVBoxLayout()

        generalTab.setLayout(layout)

        layoutRadioButton = QHBoxLayout()
        radiobutton = QRadioButton("zebra")
        radiobutton.name = "zebra"
        radiobutton.toggled.connect(self.onClicked)
        layoutRadioButton.addWidget(radiobutton)

        radiobutton = QRadioButton("bay horse")
        radiobutton.name = "bay horse"
        radiobutton.toggled.connect(self.onClicked)
        layoutRadioButton.addWidget(radiobutton)
        radiobutton = QRadioButton("test")

        radiobutton.name = "test"
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.onClicked)
        layoutRadioButton.addWidget(radiobutton)

        layoutButton = QHBoxLayout()
        task1 = QPushButton('task1')
        task2 = QPushButton('task2')
        task3 = QPushButton('task3')

        return generalTab

    def task1Tab(self):  # task1 tab
        '''task1 tab'''

        generalTab = QWidget()
        layout = QVBoxLayout()
        task1 = QPushButton('task1')
        task1.clicked.connect(self.task1)
        layout.addWidget(task1)
        generalTab.setLayout(layout)
        return generalTab

    def task2Tab(self):  # task2 tab
        '''task2 tab'''
        generalTab = QWidget()
        layout = QVBoxLayout()
        task2 = QPushButton('task2')
        task2.clicked.connect(self.task2)
        layout.addWidget(task2)
        generalTab.setLayout(layout)
        return generalTab

    def task3Tab(self):  # Main window with hello-words and descripition what's going on
        '''task3 tab'''
        generalTab = QWidget()
        layout = QVBoxLayout()
        task3Single = QPushButton('task3Single')
        task3Single.clicked.connect(self.task3Single)
        task3Both = QPushButton('task3Both')
        task3Both.clicked.connect(self.task3Both)
        layout.addWidget(task3Single)
        layout.addWidget(task3Both)

        generalTab.setLayout(layout)

        return generalTab

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Class is %s" % (radioButton.name))
            self.iterator.setName(radioButton.name)
            self.name = radioButton.name

    def click(self):
        '''function for testing qt events '''
        print("Click!")

    def __inputPath(self) -> None:
        '''service function'''
        tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        while not "dataset" in self.path:
            tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        tmp = self.path

    def clearButton(self):
        print("clear")
        self.pixmap = QPixmap(".jpg")
        self.lable.setPixmap(self.pixmap)
        self.iterator.clear()
        self.resize(300, 300)

    def nextButton(self):
        try:
            tmp = os.path.join(os.path.join(self.iterator.path,
                                            self.iterator.name), self.iterator.__next__())
            self.pixmap = QPixmap(
                f"{tmp}")
            self.lable.setPixmap(self.pixmap)
            # self.resize(self.pixmap.width(), self.pixmap.height())
            print(tmp)
        except:
            self.pixmap = QPixmap('blueLobster.jpg')
            self.lable.setPixmap(self.pixmap)
            reply = QMessageBox.question(self, 'Message',
                                         "empry, clear?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.iterator.clear()
            print("Error")

    def task1(self):
        print("done task1!")
        create_csv(self.name, self.path)

    def task2(self):
        print("done task2!")
        copy_dataset(self.name, self.path, QFileDialog.getExistingDirectory(
            self, 'Select Folder'))

    def task3Single(self):
        print("done task3 single!")
        create_dir_copy_randNames(
            self.name, self.path, QFileDialog.getExistingDirectory(self, 'Select Folder'))

    def task3Both(self):
        print("done task3 both!")
        create_dir_copy_randNames_both(
            'zebra', 'bay horse', self.path, QFileDialog.getExistingDirectory(self, 'Select Folder'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTabWidget Example")
#         self.resize(270, 110)
#         # Create a top-level layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         # Create the tab widget with two tabs
#         tabs = QTabWidget()
#         tabs.addTab(self.generalTabUI(), "General")
#         tabs.addTab(self.networkTabUI(), "Network")
#         layout.addWidget(tabs)

#     def generalTabUI(self):
#         """Create the General page UI."""
#         generalTab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QCheckBox("General Option 1"))
#         layout.addWidget(QCheckBox("General Option 2"))
#         generalTab.setLayout(layout)
#         return generalTab

#     def networkTabUI(self):
#         """Create the Network page UI."""
#         networkTab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QCheckBox("Network Option 1"))
#         layout.addWidget(QCheckBox("Network Option 2"))
#         networkTab.setLayout(layout)
#         return networkTab

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
