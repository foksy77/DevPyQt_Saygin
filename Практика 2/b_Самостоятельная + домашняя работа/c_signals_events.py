"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * QtWidgets.QApplication.screens()
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию - готово
    * При изменении размера окна выводить его новый размер - готово
"""
from datetime import datetime

from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signals_events_design import Ui_Form


def tstamp() -> str:
    return "[" + str(datetime.now().strftime("%H:%M:%S")) + "]: "


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUI()
        self.initSignals()

    def changeEvent(self, event):

        # print(f"{tstamp()}changeEvent: {event}")
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            # print(f"{tstamp()}WindowStateChange")
            if self.windowState() == QtCore.Qt.WindowState.WindowMaximized:
                print(f"{tstamp()}WindowMaximized")
            elif self.windowState() == QtCore.Qt.WindowState.WindowMinimized:
                print(f"{tstamp()}WindowMinimized")
        if event.type() == QtCore.QEvent.Type.ActivationChange:
            # print(f"{tstamp()}ActivationChange: {QtCore.Qt.WindowState.WindowActive}")
            if self.windowState() == QtCore.Qt.WindowState.WindowActive:
                print(f"{tstamp()}Window Active")
            if self.windowState() == QtCore.Qt.WindowState.WindowNoState:
                print(f"{tstamp()}Window No State / Window_inActive")
            # if self.windowState() != QtCore.Qt.WindowState. .WindowActive:
            #     print(f"{tstamp()}WindowNoState / Window_inActive")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Изменение размера окна Ш x В: {str(event.size().width())} x "
                                              f"{str(event.size().height())}")
        print(f"{tstamp()}Изменение размера окна Ш x В: {str(event.size().width())} x {str(event.size().height())}")
        self.ui.pushButtonMoveCoords.setDisabled(True)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещение, было: X = {str(event.oldPos().x())} Y = "
                                              f"{str(event.oldPos().y())}")
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещение, стало: X = {str(event.pos().x())} Y = "
                                              f"{str(event.pos().y())}")
        print(f"{tstamp()}Перемещение, было: X = {str(event.oldPos().x())} Y = {str(event.oldPos().y())}")
        print(f"{tstamp()}Перемещение, стало: X = {str(event.pos().x())} Y = {str(event.pos().y())}")
        self.ui.pushButtonMoveCoords.setDisabled(True)

    def initUI(self):
        self.ui.plainTextEdit.appendPlainText(str(self.pos()))
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos())))
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().width()))
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().height()))

        # self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().width()))

        monitors = QtWidgets.QApplication.screens()
        monitorsqty = len(monitors)

        self.ui.plainTextEdit.appendPlainText(f"Мониторы: {monitorsqty} шт:")
        for i in range(len(monitors)):
            self.ui.plainTextEdit.appendPlainText(f"{(i+1)}: {str(monitors[i])}")

        self.ui.pushButtonMoveCoords.setDisabled(True)

    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.moveLeftTop)
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.ui.pushButtonLB.clicked.connect(self.moveLeftBottom)
        self.ui.pushButtonRB.clicked.connect(self.moveRightBottom)
        self.ui.pushButtonCenter.clicked.connect(self.moveCenter)
        self.ui.pushButtonMoveCoords.clicked.connect(self.moveCoords)
        self.ui.pushButtonGetData.clicked.connect(self.getData)

    def moveLeftTop(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в левый верхний угол.")
        self.move(0, 0)

    def moveRightTop(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в правый верхний угол.")
        # self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().height()))

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width = current_screen.size().width()
        # screen_height = current_screen.size().height()

        self.move((screen_width - self.width()), 0)

    def moveLeftBottom(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в левый нижний угол.")
        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        # screen_width = current_screen.size().width()
        screen_height = current_screen.size().height()

        self.move(0, (screen_height - self.height()))

    def moveRightBottom(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в правый нижний угол.")
        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width = current_screen.size().width()
        screen_height = current_screen.size().height()
        self.move((screen_width - self.width()), (screen_height - self.height()))

    def moveCenter(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в центр.")
        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width = current_screen.size().width()
        screen_height = current_screen.size().height()
        self.move((screen_width-self.width())/2, (screen_height-self.height())/2)

    def moveCoords(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Перемещаем в координаты: X = {self.ui.spinBoxX.value()}, Y = "
                                              f"{self.ui.spinBoxY.value()}")
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def getData(self):
        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Получаем данные окна.")
        self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Положение окна: {self.pos().x()}, {self.pos().y()}"))
        # *Текущее основное окно
        self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Текущее основное окно: "
                                                  f"{QtWidgets.QWidget.windowTitle(self)} / "
                                                  f"{QtWidgets.QApplication.activeWindow()} / "
                                                  f"{QtWidgets.QApplication.applicationName()}"))
        # *Минимальные размеры окна
        self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Минимальные размеры окна: "
                                                  f"{QtWidgets.QApplication.activeWindow().minimumSize()}"))
        # print(f"{QtWidgets.QMainWindow.minimumSize()}")
        print(f"{str(QtWidgets.QWidget.isVisible(self))}")
        print(f"{str(QtWidgets.QWidget.isMinimized(self))}")
        print(f"{str(QtWidgets.QWidget.isActiveWindow(self))}")

        # *Координаты центра приложения
        # self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Координаты центра приложения:"
        #                                           f" {QtWidgets.QApplication.activeWindow().}"))
        # *Отслеживание состояния окна(свернуто / развёрнуто / активно / отображено)
        self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Состояние окна: {self.pos().x()}, {self.pos().y()}"))

        self.ui.plainTextEdit.appendPlainText(str(f"{tstamp()}Текущий монитор: "
                                                  f"{QtWidgets.QApplication.screenAt(self.pos()).name()} "
                                                  f"({QtWidgets.QApplication.screenAt(self.pos()).size().width()} x "
                                                  f"{QtWidgets.QApplication.screenAt(self.pos()).size().height()})"))
        # self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().width()))
        # self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().height()))

        # self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size().width()))

        monitors = QtWidgets.QApplication.screens()
        monitorsqty = len(monitors)

        self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Всего мониторов: {monitorsqty} шт:")
        for i in range(len(monitors)):
            self.ui.plainTextEdit.appendPlainText(f"{(i + 1)}: {str(monitors[i])}")

        curr_x = self.pos().x()
        curr_y = self.pos().y()
        # self.ui.plainTextEdit.appendPlainText(f"{tstamp()}Текущее положение окна: X = {curr_x}, Y = {curr_y}")

        self.ui.spinBoxX.setValue(curr_x)
        self.ui.spinBoxX.setMaximum(QtWidgets.QApplication.screenAt(self.pos()).size().width() - self.width())
        self.ui.spinBoxY.setValue(curr_y)
        self.ui.spinBoxY.setMaximum(QtWidgets.QApplication.screenAt(self.pos()).size().height() - self.height())

        self.ui.pushButtonMoveCoords.setDisabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
