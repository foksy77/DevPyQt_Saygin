"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.label = QtWidgets.QLabel("Красивая кнопка")
        self.label.setStyleSheet("border: 3px solid red")
        self.label.setText("<font color ='#2a9d8f'>Красивая</font>  <font color ='#e76f51'>кнопка</font>")

        self.label2 = QtWidgets.QLabel("Красивая кнопка")
        self.label2.setStyleSheet("border: 3px solid blue")

        self.label.installEventFilter(self)
        self.label2.installEventFilter(self)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)

        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print(event)
            print("Тут можно выполнить любой бэк при нажатии на кнопку")

        if watched == self.label2 and event.type() == QtCore.QEvent.Type.Wheel:
            print(event)
            print("Тут можно выполнить любой бэк при прокрутке колесика мыши")
            print(self.label2.setText(f"Красивая кнопка: {event.angleDelta()}"))

        return super(Window, self).eventFilter(watched, event)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
