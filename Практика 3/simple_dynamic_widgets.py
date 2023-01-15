from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.initSignals()

    def initUi(self):
        self.verticalLayoutDynamicWidgets = QtWidgets.QVBoxLayout()

        self.pushButtonAddWidget = QtWidgets.QPushButton("Добавить элемент")
        self.pushButtonGetData = QtWidgets.QPushButton("Получить данные")
        self.pushButtonDelWidget = QtWidgets.QPushButton("Удалить элемент")

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(self.verticalLayoutDynamicWidgets)
        layout.addSpacerItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding))
        layout.addWidget(self.pushButtonAddWidget)
        layout.addWidget(self.pushButtonGetData)
        layout.addWidget(self.pushButtonDelWidget)

        self.setLayout(layout)

    def initSignals(self):
        self.pushButtonAddWidget.clicked.connect(self.onPBClicked)
        self.pushButtonGetData.clicked.connect(self.onPBGetData)
        self.pushButtonDelWidget.clicked.connect(self.onPBDelWidget)

    def onPBClicked(self):
        new_widget = QtWidgets.QLineEdit()
        new_widget.setObjectName(f"lineEdit_{self.verticalLayoutDynamicWidgets.count()}")

        self.verticalLayoutDynamicWidgets.addWidget(new_widget)

    def onPBGetData(self):

        result = []
        for i in range(self.verticalLayoutDynamicWidgets.count()):
            widget_link = self.verticalLayoutDynamicWidgets.itemAt(i).widget()
            result.append(widget_link.text())

        print(result)

    def onPBDelWidget(self):
        last_widget = self.verticalLayoutDynamicWidgets.count() - 1

        widget_link = self.verticalLayoutDynamicWidgets.itemAt(last_widget)
        if not widget_link:
            return 

        widget_link = widget_link.widget()

        print(widget_link)
        widget_link.deleteLater()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
