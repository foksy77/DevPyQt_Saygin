"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initChilds()
        self.initUi()
        self.initSignals()

    def initUi(self):
        self.label = QtWidgets.QLabel("Пройдите регистрацию")
        self.pushButtonRegistration = QtWidgets.QPushButton("Регистрация")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButtonRegistration)

        self.setLayout(layout)

    def initSignals(self):
        self.pushButtonRegistration.clicked.connect(self.registrationDialog.exec)
        self.registrationDialog.received.connect(
            lambda received: self.label.setText(f"Добро пожаловать {received[0]}, ваш пароль {received[1]}")
        )

    def initChilds(self):
        self.registrationDialog = RegistrationDialog()


class RegistrationDialog(QtWidgets.QDialog):
    received = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self):
        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")

        self.pushButton = QtWidgets.QPushButton("Зарегистрироваться")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditLogin)
        layoutLineEdit.addWidget(self.lineEditPassword)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addWidget(self.pushButton)

        self.setLayout(layoutMain)

    def initSignals(self):
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self):
        login = self.lineEditLogin.text()
        password = self.lineEditPassword.text()

        self.received.emit((login, password))

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
