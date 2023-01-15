"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url + время обновления(таймаута)),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui
import requests
from requests.exceptions import ConnectTimeout


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThread()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.layoutUrls = QtWidgets.QVBoxLayout()

        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Введите URL")

        self.pushButton = QtWidgets.QPushButton("Начать выполнение")
        self.pushButton.setCheckable(True)

        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(2)
        self.spinBox.setMinimum(2)

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditUrl)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initThread(self):
        """

        :return:
        """

        self.urlCheckerThread = URLCheckerThread()

    def initSignals(self):
        """

        :return:
        """

        self.pushButton.clicked.connect(self.startUrlCheck)
        self.urlCheckerThread.started.connect(lambda: self.plainTextEdit.appendPlainText("Поток запущен"))
        self.urlCheckerThread.responsed.connect(lambda status_code: self.plainTextEdit.appendPlainText(f"{time.ctime()} Статус сайта: {status_code}"))
        self.urlCheckerThread.finished.connect(self.threadFinished)
        self.spinBox.valueChanged.connect(self.setTimeout)

    def startUrlCheck(self, status: bool) -> None:
        """

        :param status: состояние кнопки
        :return:
        """

        if status:
            url = self.lineEditUrl.text()

            if not url:
                QtWidgets.QMessageBox.about(self, "Ошибка", "URL не заполнен")
                self.pushButton.setChecked(False)
                return None

            self.urlCheckerThread.url = url
            self.urlCheckerThread.timeout = self.spinBox.value()
            self.urlCheckerThread.start()
            self.pushButton.setText("Остановить проверку")
        else:
            self.urlCheckerThread.status = False
            self.pushButton.setText("Запустить проверку")
            self.pushButton.setEnabled(False)

    def threadFinished(self):
        self.plainTextEdit.appendPlainText("Поток остановлен")
        self.pushButton.setEnabled(True)

    def setTimeout(self, value):
        self.urlCheckerThread.timeout = value

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.urlCheckerThread.terminate()


class URLCheckerThread(QtCore.QThread):
    responsed = QtCore.Signal(int)

    def __init__(self, url=None, timeout=2, parent=None):
        super().__init__(parent)

        self.url = url
        self.timeout = timeout
        self.status = True

    def run(self):
        self.status = True

        while self.status:
            try:
                response = requests.get(self.url)
                self.responsed.emit(response.status_code)
            except ConnectTimeout:
                self.responsed.emit(-1)
            time.sleep(self.timeout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
