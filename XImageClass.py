"""
XImageClass
~~~~~~~~~~~
Đây là nơi chứa các widget được custom để giúp bạn nhanh chóng tạo ra một số widget và bố cục phổ biến nhanh chóng."""

from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton, QLabel, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap

class QRadioButtonCustom(QRadioButton):

    def __init__(self, str, value, parent=None):
        super().__init__(str, parent=parent)
        self.value = value

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value


class QHRadioGroupBox(QGroupBox):

    def __init__(self, str, *QRadioButtonCustoms, parent=None):
        '''
        Triển khai một group radio button theo chiều ngang
        :param `*QRadioButtonCustoms`: Truyền vào các QRadioButtonCustom
        '''
        super().__init__(str, parent=parent)
        self.value = ''
        self.radioButtons = QRadioButtonCustoms
        self.hbox_layout = QHBoxLayout(self)
        self.setLayout(self.hbox_layout)
        for i in self.radioButtons:
            i.toggled.connect(self.__setValue)
            self.hbox_layout.addWidget(i)

    def addRadioButtonCustom(self, radioButtonCustom):
        radioButtonCustom.toggled.connect(self.__setValue)
        self.hbox_layout.addWidget(radioButtonCustom)

    def getValue(self):
        return self.value

    def setDefaultValue(self, pos:int):
        """Đặt giá trị mặc định. pos là một int. Nếu `pos` vượt quá, thì mặc định check radio đầu tiên."""
        if pos > len(self.radioButtons) - 1:
            self.radioButtons[0].setChecked(True)
        else:
            self.radioButtons[pos].setChecked(True)

    def __setValue(self):
        rd = self.sender()
        if rd.isChecked():
            self.value = rd.getValue()

class QXImage(QFrame):

    def __init__(self, name, path, info, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.path = path
        self.info = info
        
        self.setupUI()

    def setupUI(self):
        self.hbox_layout = QHBoxLayout()
        self.setLayout(self.hbox_layout)

        self.label_main = QLabel(parent=self)
        self.image = QPixmap(self.path)
        self.label_main.setPixmap(self.image)
        self.hbox_layout.addWidget(self.label_main)

        self.label_name = QLabel(self.name)
        self.hbox_layout.addWidget(self.label_name)
        self.resize(self.image.width(),self.image.height())

    def getInfo(self):
        return self.info

