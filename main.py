import sys
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox, QTabWidget, QVBoxLayout, QMainWindow, )
from PyQt5.QtGui import QIcon, QPixmap


# from typing import Self

# labs imports
from task1 import Iterator1_img, create_csv
from task2 import copy_dataset
from task3 import create_dir_copy_randNames, create_dir_copy_randNames_both


class Example(QWidget):

    def __init__(self) -> None:
        '''Constructor'''
        super().__init__()
        self.mainBtn = QPushButton("Choose dataset dir", self)
        self.mainBtn.clicked.connect(self.__inputPath)
        self.iterator = Iterator1_img("test", "dataset")
        # self.pixmap = QPixmap('blueLobster.jpg')
        self.pixmap = QPixmap('.jpg')
        self.lable = QLabel(self)
        self.name = "test"
        self.path = "dataset"
        self.initUI()

    # def __iter__(self) -> Self:
    #     '''something'''
    #     return self

    def initUI(self) -> None:
        '''support constructor function'''

        self.setWindowTitle('Lab3')

        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.generalTab(), "general")
        tabs.addTab(self.showImageTab(), "show image")
        # tabs.addTab(self.task1Tab(), "task1")
        # tabs.addTab(self.task2Tab(), "task2")
        # tabs.addTab(self.task3Tab(), "task3")
        tabs.addTab(self.tasksTab(), "tasksTab")
        self.iterator.setPath(self.path)
        layout.addWidget(tabs)

        self.setGeometry(300, 300, 350, 300)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.setWindowIcon(QIcon('6112_Logo_git_prefinal.jpg'))
        self.show()

    # Main window with hello-words and descripition what's going on
    def generalTab(self) -> QWidget:
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

        # layoutRadioButton = QHBoxLayout()
        # radiobutton = QRadioButton("zebra")
        # radiobutton.name = "zebra"
        # radiobutton.toggled.connect(self.onClicked)
        # layoutRadioButton.addWidget(radiobutton)

        # radiobutton = QRadioButton("bay horse")
        # radiobutton.name = "bay horse"
        # radiobutton.toggled.connect(self.onClicked)
        # layoutRadioButton.addWidget(radiobutton)
        # radiobutton = QRadioButton("test")

        # radiobutton.name = "test"
        # radiobutton.setChecked(True)
        # radiobutton.toggled.connect(self.onClicked)

        # layoutRadioButton.addWidget(radiobutton)
        # layout.addLayout(layoutRadioButton)
        generalTab.setLayout(layout)
        return generalTab

    # image tab where user choose directory and see the img via _next_
    def showImageTab(self) -> QWidget:
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

        self.lable.setPixmap(self.pixmap)
        layout.addWidget(self.lable)
        self.resize(self.pixmap.width(), self.pixmap.height())

        # layout.addLayout(layoutRadioButton)
        layout.addLayout(layoutButton)
        generalTab.setLayout(layout)
        return generalTab

    def tasksTab(self) -> QWidget:
        '''function generates tab with all buttons of prev lab'''
        generalTab = QWidget()
        layout = QVBoxLayout()

        layout = QVBoxLayout()
        task1 = QPushButton('task1')
        task1.clicked.connect(self.task1)
        layout.addWidget(task1)

        task2 = QPushButton('task2')
        task2.clicked.connect(self.task2)
        layout.addWidget(task2)

        task3Single = QPushButton('task3Single')
        task3Single.clicked.connect(self.task3Single)
        task3Both = QPushButton('task3Both')
        task3Both.clicked.connect(self.task3Both)
        layout.addWidget(task3Single)
        layout.addWidget(task3Both)

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

    # def task1Tab(self) -> QWidget:    # task1 tab
    #     '''task1 tab'''

    #     generalTab = QWidget()
    #     layout = QVBoxLayout()
    #     task1 = QPushButton('task1')
    #     task1.clicked.connect(self.task1)
    #     layout.addWidget(task1)
    #     generalTab.setLayout(layout)
    #     return generalTab

    # def task2Tab(self) -> QWidget:   # task2 tab
    #     '''task2 tab'''
    #     generalTab = QWidget()
    #     layout = QVBoxLayout()
    #     task2 = QPushButton('task2')
    #     task2.clicked.connect(self.task2)
    #     layout.addWidget(task2)
    #     generalTab.setLayout(layout)
    #     return generalTab

    # # Main window with hello-words and descripition what's going on
    # def task3Tab(self) -> QWidget:
    #     '''task3 tab'''
    #     generalTab = QWidget()
    #     layout = QVBoxLayout()
    #     task3Single = QPushButton('task3Single')
    #     task3Single.clicked.connect(self.task3Single)
    #     task3Both = QPushButton('task3Both')
    #     task3Both.clicked.connect(self.task3Both)
    #     layout.addWidget(task3Single)
    #     layout.addWidget(task3Both)

    #     generalTab.setLayout(layout)

    #     return generalTab

    def onClicked(self) -> None:
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Class is %s" % (radioButton.name))
            self.iterator.setName(radioButton.name)
            self.name = radioButton.name

    def __inputPath(self) -> None:
        '''service function'''
        print("innnnpppuuut")
        tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        while not "dataset" in tmp:
            print("error")
            QMessageBox.critical(
                self, "Wrong dir", "please choose dir with dataset", QMessageBox.Ok)
            tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        tmp = self.path

    def clearButton(self) -> None:
        print("clear")
        self.pixmap = QPixmap(".jpg")
        self.lable.setPixmap(self.pixmap)
        self.iterator.clear()
        self.resize(300, 300)

    def nextButton(self) -> None:
        try:
            tmp = os.path.join(os.path.join(self.iterator.path,
                                            self.iterator.name), self.iterator.__next__())
            self.pixmap = QPixmap(
                f"{tmp}")
            self.lable.setPixmap(self.pixmap)
            print(tmp)
        except:
            self.pixmap = QPixmap('blueLobster.jpg')
            self.lable.setPixmap(self.pixmap)
            reply = QMessageBox.question(self, 'End of img_class',
                                         "empry, clear?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.iterator.clear()
            print("Error")

    def task1(self) -> None:
        print("done task1!")
        create_csv(self.name, self.path)

    def task2(self) -> None:
        print("done task2!")
        copy_dataset(self.name, self.path, QFileDialog.getExistingDirectory(
            self, 'Select Folder'))

    def task3Single(self) -> None:
        print("done task3 single!")
        create_dir_copy_randNames(
            self.name, self.path, QFileDialog.getExistingDirectory(self, 'Select Folder'))

    def task3Both(self) -> None:
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
