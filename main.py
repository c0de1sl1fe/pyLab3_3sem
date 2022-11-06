import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                                QTextEdit, QGridLayout, QApplication, QHBoxLayout, )

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # task1 = QLabel('task1')
        # task2 = QLabel('task2')
        # task3 = QLabel('task3')

        # task1Btn = QPushButton("Do task1")
        # task2Btn = QPushButton("Do task 2")
        # task3Btn = QPushButton("Do task 3")
        # clearBtn = QPushButton("clear")
        # nextBtn = QPushButton("next")
        # grid = QGridLayout()
        # grid.setSpacing(1)
        # grid.setAlignment(1)
        # grid.addWidget(task1, 1, 0)
        # grid.addWidget(task1Btn, 1, 1)

        # grid.addWidget(task2, 2, 0)
        # grid.addWidget(task2Btn, 2, 1)

        # grid.addWidget(task3, 3, 0)
        # grid.addWidget(task3Btn, 3, 1)

        

        # grid.addWidget(clearBtn)
        # grid.addWidget(nextBtn)
        # self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Lab3')

        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.generalTab(), "general")
        tabs.addTab(self.generalTab(), "general")

        layout.addWidget(tabs)






        self.show()




    def generalTab(self):
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("test1"))
        generalTab.setLayout(layout)
        return generalTab


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
import sys


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