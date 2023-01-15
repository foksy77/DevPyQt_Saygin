"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initTimers()
        self.initUi()

        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.labelDateTime = QtWidgets.QLabel()
        self.labelDateTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.pushButton = QtWidgets.QPushButton("Начать выполнение")
        self.pushButton.setCheckable(True)

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)
        layout.addWidget(self.labelDateTime)

        self.setLayout(layout)

    def initTimers(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timerTime = QtCore.QTimer()
        self.timerTime.setInterval(1000)
        self.timerTime.start()

        self.timerHandle = QtCore.QTimer()
        self.timerHandle.setInterval(2000)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.timerTime.timeout.connect(self.setDateTime)
        self.timerHandle.timeout.connect(self.handleFunc)

        self.pushButton.clicked.connect(self.setTimerHandleStatus)

    def setDateTime(self) -> None:
        """
        Установка времени в labelDateTime

        :return: None
        """

        dateTime = QtCore.QDateTime.currentDateTime()
        dateStr = dateTime.toString("yyyy-MM-dd HH:mm:ss ddd")
        self.labelDateTime.setText(dateStr)

    def handleFunc(self) -> None:
        """
        Функция обработки

        :return: None
        """

        self.plainTextEdit.appendPlainText(time.ctime() + " Вызов функции: " + str(self.handleFunc))

    def setTimerHandleStatus(self, status) -> None:
        """
        Остановка/запуск таймера для функции обработки

        :param status: состояние self.pushButton
        :return: None
        """

        if status:
            self.plainTextEdit.appendPlainText(time.ctime() + " Обработка запущена")
            self.timerHandle.start()
        else:
            self.plainTextEdit.appendPlainText(time.ctime() + " Обработка остановлена")
            self.timerHandle.stop()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.timerHandle.stop()
        self.timerTime.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
