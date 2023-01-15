from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.cb = QtWidgets.QComboBox()
        self.cb.addItems(['1', '2', '3'])

        self.tw = QtWidgets.QTabWidget()
        self.tw.addTab(QtWidgets.QWidget(), "1")
        self.tw.addTab(QtWidgets.QWidget(), "2")
        self.tw.addTab(QtWidgets.QWidget(), "3")

        self.tw.setTabBarAutoHide(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.cb)
        layout.addWidget(self.tw)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
