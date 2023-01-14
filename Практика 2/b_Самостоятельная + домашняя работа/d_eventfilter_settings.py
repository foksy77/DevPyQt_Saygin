"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLCDNumber

from ui.d_eventfilter_settings import Ui_Form



class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSignals()
        self.initUI()

    def initUI(self):
        self.ui.comboBox.addItems(['Hex', 'Dec', 'Oct', 'Bin'])
        self.ui.comboBox.setCurrentIndex(1)
        self.ui.lcdNumber.setMode(QLCDNumber.Dec)
        print(self.ui.lcdNumber.mode())

    def initSignals(self):
        self.ui.dial.valueChanged.connect(self.dial_touch)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_touch)
        self.ui.comboBox.currentIndexChanged.connect(self.cb_touch)

    def cb_touch(self):
        curr_index = self.ui.comboBox.currentIndex()
        if curr_index == 0:
            self.ui.lcdNumber.setMode(QLCDNumber.Hex)
            print(self.ui.lcdNumber.mode())
        if curr_index == 1:
            self.ui.lcdNumber.setMode(QLCDNumber.Dec)
            print(self.ui.lcdNumber.mode())
        if curr_index == 2:
            self.ui.lcdNumber.setMode(QLCDNumber.Oct)
            print(self.ui.lcdNumber.mode())
        if curr_index == 3:
            self.ui.lcdNumber.setMode(QLCDNumber.Bin)
            print(self.ui.lcdNumber.mode())


    def dial_touch(self):
        print(str(self.ui.dial.value()))
        self.ui.lcdNumber.display(self.ui.dial.value())
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def slider_touch(self):
        print(str(self.ui.horizontalSlider.value()))
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        self.ui.dial.setValue(self.ui.horizontalSlider.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
