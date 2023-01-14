"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditInput.setPlaceholderText("Введите текст")

        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setReadOnly(True)
        self.lineEditMirror.setPlaceholderText("Текст задом наперёд")

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("Очистить")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addWidget(self.pushButton)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(lambda: self.lineEditMirror.setText(""))

        # self.lineEditInput.textChanged.connect(
        #     lambda input_text: self.lineEditMirror.setText(input_text[::-1])
        # )

        self.lineEditInput.textChanged.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self) -> None:
        """
        Отображение текста задом наперед

        :return: None
        """

        input_text = self.lineEditInput.text()
        if not input_text:
            self.lineEditMirror.setText("")
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Нечего отображать")
            return

        self.lineEditMirror.setText(input_text[::-1])







if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
