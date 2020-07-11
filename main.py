from PyQt5.QtWidgets import (QWidget,QMainWindow, QApplication, QPushButton, 
QRadioButton, QLabel, QGridLayout, QCheckBox, QLineEdit, QFileDialog, QFontDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QFileDialog, QButtonGroup)
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize
from XImageClass import QHRadioGroupBox, QRadioButtonCustom

class UnsplashOptionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unsplash Option')
        self.grid_layout = QGridLayout(self)
        self.setupUI()

    def setupUI(self):
        self.label_per_page = QLabel('per page',self)
        self.text_per_page = QLineEdit(self)
        self.label_page = QLabel('page',self)
        self.text_page = QLineEdit(self)
        self.qradioCustomButton_raw = QRadioButtonCustom('raw','raw',self)
        self.qradioCustomButton_full = QRadioButtonCustom('full','full',self)
        self.qradioCustomButton_regular = QRadioButtonCustom('regular','regular',self)
        self.qradioCustomButton_small = QRadioButtonCustom('small','small',self)
        self.qradioCustomButton_thumnail = QRadioButtonCustom('thumnail','thumnail',self)
        self.qhradiogroupbox_quality = QHRadioGroupBox('quality',
                                                        self.qradioCustomButton_raw,
                                                        self.qradioCustomButton_full,
                                                        self.qradioCustomButton_regular,
                                                        self.qradioCustomButton_small,
                                                        self.qradioCustomButton_thumnail)
        self.qhradiogroupbox_quality.setDefaultValue(0)

        self.qradioCustomButton_latest = QRadioButtonCustom('latest','latest',self)
        self.qradioCustomButton_oldest = QRadioButtonCustom('oldest','oldest',self)
        self.qradioCustomButton_popular = QRadioButtonCustom('popular','popular',self)
        self.qhradiogroupbox_orderby = QHRadioGroupBox('order by',
                                                        self.qradioCustomButton_latest,
                                                        self.qradioCustomButton_oldest,
                                                        self.qradioCustomButton_popular)
        self.qhradiogroupbox_orderby.setDefaultValue(0)

        self.button_ok = QPushButton('ok',self)
        self.button_ok.setFixedWidth(130)
        self.button_ok.clicked.connect(lambda: self.close())

        self.grid_layout.addWidget(self.label_per_page,1,0)
        self.grid_layout.addWidget(self.text_per_page,1,1)
        self.grid_layout.addWidget(self.label_page,2,0)
        self.grid_layout.addWidget(self.text_page,2,1)
        self.grid_layout.addWidget(self.qhradiogroupbox_quality,3,0,1,2)
        self.grid_layout.addWidget(self.qhradiogroupbox_orderby,4,0,1,2)
        self.grid_layout.addWidget(self.button_ok,5,0,1,2)


class App(QWidget):

    label_font = QFont('Consolas',10)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Images Download Manager')
        self.setupUI()

    def setupUI(self):

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)

        self.label_find = QLabel('Find:', self)
        self.grid_layout.addWidget(self.label_find,0,0)

        self.line_find = QLineEdit(self)
        self.line_find.setPlaceholderText('What do you want to find?')
        self.grid_layout.addWidget(self.line_find,0,1)

        self.label_save_at = QLabel('Save at:', self)
        self.grid_layout.addWidget(self.label_save_at,1,0)

        self.btt_save_at_browse = QPushButton('Browse...')
        self.btt_save_at_browse.clicked.connect(self.browse)
        self.grid_layout.addWidget(self.btt_save_at_browse,1,2)

        self.line_save_at = QLineEdit(self)
        self.grid_layout.addWidget(self.line_save_at,1,1)


        # Source to get img url
        self.checkbox_group_box_source = QGroupBox('Source',self)
        self.hbox_checkbox_group_box_source = QHBoxLayout()
        self.checkbox_group_box_source.setLayout(self.hbox_checkbox_group_box_source)
        
        self.check_unsplash = QCheckBox('Unsplash',self)
        self.check_unsplash.toggled.connect(self.unsplashOptionWindow)
        self.hbox_checkbox_group_box_source.addWidget(self.check_unsplash)
        self.grid_layout.addWidget(self.checkbox_group_box_source,2,0,1,3)


        # Options
        self.checkbox_group_box_option = QGroupBox('Options',self)
        self.hbox_checkbox_group_box_option = QHBoxLayout()
        self.checkbox_group_box_option.setLayout(self.hbox_checkbox_group_box_option)
        
        self.check_labeled = QCheckBox('Labeled',self)
        self.hbox_checkbox_group_box_option.addWidget(self.check_labeled)
        self.check_threads = QCheckBox('Threads',self)
        self.hbox_checkbox_group_box_option.addWidget(self.check_threads)
        
        self.grid_layout.addWidget(self.checkbox_group_box_option,3,0,1,3)


        # Action buttons
        self.actionButton_group_box = QGroupBox(self)
        self.hbox_buttion_actionButon = QHBoxLayout()
        self.actionButton_group_box.setLayout(self.hbox_buttion_actionButon)
        
        self.button_seeLog = QPushButton('see log',self.actionButton_group_box)
        self.hbox_buttion_actionButon.addWidget(self.button_seeLog)
        self.button_download = QPushButton('download',self.actionButton_group_box)
        self.hbox_buttion_actionButon.addWidget(self.button_download)
        self.button_openInFolder = QPushButton('open in folder',self.actionButton_group_box)
        self.hbox_buttion_actionButon.addWidget(self.button_openInFolder)

        self.grid_layout.addWidget(self.actionButton_group_box,4,0,1,3)
        
        self.show()

    def browse(self):
        file = QFileDialog.getExistingDirectory(self,"Select a folder")
        self.line_save_at.setText(file)

    def unsplashOptionWindow(self):
        self.sub = UnsplashOptionWindow()
        if self.check_unsplash.isChecked():
            self.sub.show()
        else:
            self.sub.close()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    app = App()
    sys.exit(a.exec_())
