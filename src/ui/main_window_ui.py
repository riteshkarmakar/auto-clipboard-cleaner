# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QTableWidget, QTableWidgetItem, QToolBar,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(600, 0))
        MainWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon()
        icon.addFile(u":/icons/clipboard.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_start = QAction(MainWindow)
        self.action_start.setObjectName(u"action_start")
        icon1 = QIcon()
        icon1.addFile(u":/icons/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_start.setIcon(icon1)
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        self.action_stop.setChecked(False)
        self.action_stop.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_stop.setIcon(icon2)
        self.action_reset = QAction(MainWindow)
        self.action_reset.setObjectName(u"action_reset")
        icon3 = QIcon()
        icon3.addFile(u":/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_reset.setIcon(icon3)
        self.action_export_settings = QAction(MainWindow)
        self.action_export_settings.setObjectName(u"action_export_settings")
        self.action_load_settings = QAction(MainWindow)
        self.action_load_settings.setObjectName(u"action_load_settings")
        self.action_read_documentation = QAction(MainWindow)
        self.action_read_documentation.setObjectName(u"action_read_documentation")
        self.action_check_for_updates = QAction(MainWindow)
        self.action_check_for_updates.setObjectName(u"action_check_for_updates")
        self.action_update_check_at_startup = QAction(MainWindow)
        self.action_update_check_at_startup.setObjectName(u"action_update_check_at_startup")
        self.action_update_check_at_startup.setCheckable(True)
        self.action_update_check_at_startup.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_clean_text = QGroupBox(self.layoutWidget)
        self.groupBox_clean_text.setObjectName(u"groupBox_clean_text")
        self.verticalLayout = QVBoxLayout(self.groupBox_clean_text)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_trim = QCheckBox(self.groupBox_clean_text)
        self.checkBox_trim.setObjectName(u"checkBox_trim")
        self.checkBox_trim.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_trim)

        self.checkBox_remove_blank_lines = QCheckBox(self.groupBox_clean_text)
        self.checkBox_remove_blank_lines.setObjectName(u"checkBox_remove_blank_lines")

        self.verticalLayout.addWidget(self.checkBox_remove_blank_lines)

        self.checkBox_linebreak_to_space = QCheckBox(self.groupBox_clean_text)
        self.checkBox_linebreak_to_space.setObjectName(u"checkBox_linebreak_to_space")

        self.verticalLayout.addWidget(self.checkBox_linebreak_to_space)

        self.checkBox_multiple_spaces_to_single = QCheckBox(self.groupBox_clean_text)
        self.checkBox_multiple_spaces_to_single.setObjectName(u"checkBox_multiple_spaces_to_single")
        self.checkBox_multiple_spaces_to_single.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox_multiple_spaces_to_single)

        self.checkBox_numbered_list_to_plain = QCheckBox(self.groupBox_clean_text)
        self.checkBox_numbered_list_to_plain.setObjectName(u"checkBox_numbered_list_to_plain")

        self.verticalLayout.addWidget(self.checkBox_numbered_list_to_plain)


        self.verticalLayout_4.addWidget(self.groupBox_clean_text)

        self.groupBox_change_case = QGroupBox(self.layoutWidget)
        self.groupBox_change_case.setObjectName(u"groupBox_change_case")
        self.groupBox_change_case.setCheckable(True)
        self.groupBox_change_case.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_change_case)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_upper = QRadioButton(self.groupBox_change_case)
        self.radioButton_upper.setObjectName(u"radioButton_upper")

        self.gridLayout_3.addWidget(self.radioButton_upper, 0, 0, 1, 1)

        self.radioButton_capitalize = QRadioButton(self.groupBox_change_case)
        self.radioButton_capitalize.setObjectName(u"radioButton_capitalize")
        self.radioButton_capitalize.setChecked(False)

        self.gridLayout_3.addWidget(self.radioButton_capitalize, 0, 1, 1, 1)

        self.radioButton_lower = QRadioButton(self.groupBox_change_case)
        self.radioButton_lower.setObjectName(u"radioButton_lower")

        self.gridLayout_3.addWidget(self.radioButton_lower, 1, 0, 1, 1)

        self.radioButton_sentence = QRadioButton(self.groupBox_change_case)
        self.radioButton_sentence.setObjectName(u"radioButton_sentence")
        self.radioButton_sentence.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_sentence, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_change_case)

        self.groupBox_wrap_text = QGroupBox(self.layoutWidget)
        self.groupBox_wrap_text.setObjectName(u"groupBox_wrap_text")
        self.groupBox_wrap_text.setCheckable(True)
        self.groupBox_wrap_text.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_wrap_text)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_single_quotes = QRadioButton(self.groupBox_wrap_text)
        self.radioButton_single_quotes.setObjectName(u"radioButton_single_quotes")

        self.gridLayout_2.addWidget(self.radioButton_single_quotes, 0, 1, 1, 1)

        self.radioButton_parenthesis = QRadioButton(self.groupBox_wrap_text)
        self.radioButton_parenthesis.setObjectName(u"radioButton_parenthesis")
        self.radioButton_parenthesis.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_parenthesis, 0, 0, 1, 1)

        self.radioButton_double_quotes = QRadioButton(self.groupBox_wrap_text)
        self.radioButton_double_quotes.setObjectName(u"radioButton_double_quotes")

        self.gridLayout_2.addWidget(self.radioButton_double_quotes, 1, 1, 1, 1)

        self.radioButton_square_brackets = QRadioButton(self.groupBox_wrap_text)
        self.radioButton_square_brackets.setObjectName(u"radioButton_square_brackets")

        self.gridLayout_2.addWidget(self.radioButton_square_brackets, 2, 0, 1, 1)

        self.radioButton_curly_brackets = QRadioButton(self.groupBox_wrap_text)
        self.radioButton_curly_brackets.setObjectName(u"radioButton_curly_brackets")

        self.gridLayout_2.addWidget(self.radioButton_curly_brackets, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_wrap_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.copyright_label = QLabel(self.layoutWidget)
        self.copyright_label.setObjectName(u"copyright_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyright_label.sizePolicy().hasHeightForWidth())
        self.copyright_label.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.copyright_label)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_find_replace = QGroupBox(self.layoutWidget1)
        self.groupBox_find_replace.setObjectName(u"groupBox_find_replace")
        self.gridLayout = QGridLayout(self.groupBox_find_replace)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.label = QLabel(self.groupBox_find_replace)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_replace = QLineEdit(self.groupBox_find_replace)
        self.lineEdit_replace.setObjectName(u"lineEdit_replace")

        self.gridLayout.addWidget(self.lineEdit_replace, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_find_replace)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_find = QLineEdit(self.groupBox_find_replace)
        self.lineEdit_find.setObjectName(u"lineEdit_find")

        self.gridLayout.addWidget(self.lineEdit_find, 0, 1, 1, 1)

        self.tableWidget = QTableWidget(self.groupBox_find_replace)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(self.groupBox_find_replace)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_remove = QPushButton(self.groupBox_find_replace)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_remove)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.checkBox_process_special_characters = QCheckBox(self.groupBox_find_replace)
        self.checkBox_process_special_characters.setObjectName(u"checkBox_process_special_characters")

        self.gridLayout.addWidget(self.checkBox_process_special_characters, 4, 0, 1, 2, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.groupBox_find_replace)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(50, 50))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_stop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_reset)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_load_settings)
        self.menuFile.addAction(self.action_export_settings)
        self.menuHelp.addAction(self.action_read_documentation)
        self.menuHelp.addAction(self.action_check_for_updates)
        self.menuSettings.addAction(self.action_update_check_at_startup)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.action_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.action_start.setToolTip(QCoreApplication.translate("MainWindow", u"Start", None))
#endif // QT_CONFIG(tooltip)
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
#if QT_CONFIG(tooltip)
        self.action_stop.setToolTip(QCoreApplication.translate("MainWindow", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.action_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.action_export_settings.setText(QCoreApplication.translate("MainWindow", u"Export Settings...", None))
        self.action_load_settings.setText(QCoreApplication.translate("MainWindow", u"Load Settings...", None))
        self.action_read_documentation.setText(QCoreApplication.translate("MainWindow", u"Read Documentation", None))
        self.action_check_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates...", None))
        self.action_update_check_at_startup.setText(QCoreApplication.translate("MainWindow", u"Check for Updates at Startup", None))
        self.groupBox_clean_text.setTitle(QCoreApplication.translate("MainWindow", u"Clean Text", None))
        self.checkBox_trim.setText(QCoreApplication.translate("MainWindow", u"Trim", None))
        self.checkBox_remove_blank_lines.setText(QCoreApplication.translate("MainWindow", u"Remove blank/empty lines", None))
        self.checkBox_linebreak_to_space.setText(QCoreApplication.translate("MainWindow", u"Replace line break with space", None))
        self.checkBox_multiple_spaces_to_single.setText(QCoreApplication.translate("MainWindow", u"Multiple spaces to single", None))
        self.checkBox_numbered_list_to_plain.setText(QCoreApplication.translate("MainWindow", u"Numbered list to plain", None))
        self.groupBox_change_case.setTitle(QCoreApplication.translate("MainWindow", u"Change Case", None))
        self.radioButton_upper.setText(QCoreApplication.translate("MainWindow", u"UPPER CASE", None))
        self.radioButton_capitalize.setText(QCoreApplication.translate("MainWindow", u"Capitalize Case", None))
        self.radioButton_lower.setText(QCoreApplication.translate("MainWindow", u"lower case", None))
        self.radioButton_sentence.setText(QCoreApplication.translate("MainWindow", u"Sentence case", None))
        self.groupBox_wrap_text.setTitle(QCoreApplication.translate("MainWindow", u"Wrap Text", None))
        self.radioButton_single_quotes.setText(QCoreApplication.translate("MainWindow", u"'Single Quotes'", None))
        self.radioButton_parenthesis.setText(QCoreApplication.translate("MainWindow", u"(Parentheses)", None))
        self.radioButton_double_quotes.setText(QCoreApplication.translate("MainWindow", u"\"Double Quotes\"", None))
        self.radioButton_square_brackets.setText(QCoreApplication.translate("MainWindow", u"[Square Brackets]", None))
        self.radioButton_curly_brackets.setText(QCoreApplication.translate("MainWindow", u"{Curly Brackets}", None))
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ritesh karmakar\n"
"riteshkarmakar7407@gmail.com", None))
        self.groupBox_find_replace.setTitle(QCoreApplication.translate("MainWindow", u"Find and Replace", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Find:", None))
        self.lineEdit_replace.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Replace:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Find", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Replace", None));
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.checkBox_process_special_characters.setText(QCoreApplication.translate("MainWindow", u"Process special characters", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

