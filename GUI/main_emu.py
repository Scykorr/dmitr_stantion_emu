# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_emu.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 962)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_arrow_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_left.setGeometry(QtCore.QRect(790, 40, 75, 23))
        self.pushButton_arrow_left.setObjectName("pushButton_arrow_left")
        self.pushButton_arrow_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_right.setGeometry(QtCore.QRect(900, 40, 75, 23))
        self.pushButton_arrow_right.setObjectName("pushButton_arrow_right")
        self.pushButton_arrow_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_up.setGeometry(QtCore.QRect(900, 110, 75, 23))
        self.pushButton_arrow_up.setObjectName("pushButton_arrow_up")
        self.pushButton_arrow_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_down.setGeometry(QtCore.QRect(790, 110, 75, 23))
        self.pushButton_arrow_down.setObjectName("pushButton_arrow_down")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 310, 501, 611))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 481, 171))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(160, 50, 161, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_message = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_message.setGeometry(QtCore.QRect(10, 220, 381, 20))
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.pushButton_message = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_message.setGeometry(QtCore.QRect(400, 220, 81, 23))
        self.pushButton_message.setObjectName("pushButton_message")
        self.label_49 = QtWidgets.QLabel(self.groupBox)
        self.label_49.setGeometry(QtCore.QRect(10, 200, 121, 16))
        self.label_49.setObjectName("label_49")
        self.textEdit_message = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_message.setGeometry(QtCore.QRect(10, 250, 471, 271))
        self.textEdit_message.setObjectName("textEdit_message")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 520, 161, 21))
        self.label.setObjectName("label")
        self.plainTextEdit_commands_list = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_commands_list.setGeometry(QtCore.QRect(10, 540, 461, 61))
        self.plainTextEdit_commands_list.setReadOnly(True)
        self.plainTextEdit_commands_list.setObjectName("plainTextEdit_commands_list")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 290, 651, 631))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 631, 591))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_diagram = QtWidgets.QLabel(self.groupBox_4)
        self.label_diagram.setGeometry(QtCore.QRect(10, 30, 611, 491))
        self.label_diagram.setText("")
        self.label_diagram.setObjectName("label_diagram")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(330, 550, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.pushButton_get_result = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_get_result.setGeometry(QtCore.QRect(10, 550, 75, 23))
        self.pushButton_get_result.setObjectName("pushButton_get_result")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(90, 550, 111, 16))
        self.label_35.setObjectName("label_35")
        self.lineEdit_result = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_result.setGeometry(QtCore.QRect(210, 550, 113, 20))
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 10, 171, 531))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_am_korr = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_am_korr.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.lineEdit_am_korr.setObjectName("lineEdit_am_korr")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(130, 80, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_26.setObjectName("label_26")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(130, 130, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_39 = QtWidgets.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(10, 120, 47, 13))
        self.label_39.setObjectName("label_39")
        self.lineEdit_b = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_b.setGeometry(QtCore.QRect(10, 140, 113, 20))
        self.lineEdit_b.setText("")
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(130, 180, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.label_7.setObjectName("label_7")
        self.spinBox_b_korr = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_b_korr.setGeometry(QtCore.QRect(10, 190, 111, 22))
        self.spinBox_b_korr.setMinimum(0)
        self.spinBox_b_korr.setMaximum(355)
        self.spinBox_b_korr.setSingleStep(5)
        self.spinBox_b_korr.setProperty("value", 215)
        self.spinBox_b_korr.setObjectName("spinBox_b_korr")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(130, 280, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.label_28.setObjectName("label_28")
        self.lineEdit_a = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_a.setGeometry(QtCore.QRect(10, 290, 113, 20))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(130, 240, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_g_prd = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_g_prd.setGeometry(QtCore.QRect(10, 240, 113, 20))
        self.lineEdit_g_prd.setObjectName("lineEdit_g_prd")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(130, 340, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(10, 320, 47, 13))
        self.label_38.setObjectName("label_38")
        self.lineEdit_g_prm = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_g_prm.setGeometry(QtCore.QRect(10, 340, 113, 20))
        self.lineEdit_g_prm.setObjectName("lineEdit_g_prm")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setGeometry(QtCore.QRect(10, 370, 47, 13))
        self.label_43.setObjectName("label_43")
        self.lineEdit_a_prm = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_a_prm.setGeometry(QtCore.QRect(10, 390, 113, 20))
        self.lineEdit_a_prm.setText("")
        self.lineEdit_a_prm.setObjectName("lineEdit_a_prm")
        self.label_44 = QtWidgets.QLabel(self.groupBox_3)
        self.label_44.setGeometry(QtCore.QRect(130, 380, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(310, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.lineEdit_g_prm_p = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_g_prm_p.setGeometry(QtCore.QRect(190, 40, 113, 20))
        self.lineEdit_g_prm_p.setObjectName("lineEdit_g_prm_p")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(190, 20, 47, 13))
        self.label_41.setObjectName("label_41")
        self.label_45 = QtWidgets.QLabel(self.groupBox_3)
        self.label_45.setGeometry(QtCore.QRect(310, 80, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_3)
        self.label_46.setGeometry(QtCore.QRect(190, 70, 47, 13))
        self.label_46.setObjectName("label_46")
        self.lineEdit_a_prm_p = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_a_prm_p.setGeometry(QtCore.QRect(190, 90, 113, 20))
        self.lineEdit_a_prm_p.setText("")
        self.lineEdit_a_prm_p.setObjectName("lineEdit_a_prm_p")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(310, 130, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.spinBox_a_m_p = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_a_m_p.setGeometry(QtCore.QRect(190, 140, 111, 22))
        self.spinBox_a_m_p.setMinimum(0)
        self.spinBox_a_m_p.setMaximum(355)
        self.spinBox_a_m_p.setSingleStep(5)
        self.spinBox_a_m_p.setProperty("value", 70)
        self.spinBox_a_m_p.setObjectName("spinBox_a_m_p")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(190, 120, 47, 13))
        self.label_32.setObjectName("label_32")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(310, 190, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(190, 170, 47, 13))
        self.label_30.setObjectName("label_30")
        self.lineEdit_h_korr = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_h_korr.setGeometry(QtCore.QRect(190, 190, 113, 20))
        self.lineEdit_h_korr.setObjectName("lineEdit_h_korr")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(310, 240, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(190, 220, 47, 13))
        self.label_12.setObjectName("label_12")
        self.lineEdit_w_c = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_w_c.setGeometry(QtCore.QRect(190, 240, 113, 20))
        self.lineEdit_w_c.setObjectName("lineEdit_w_c")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(310, 290, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_w_p = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_w_p.setGeometry(QtCore.QRect(190, 290, 113, 20))
        self.lineEdit_w_p.setObjectName("lineEdit_w_p")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(190, 270, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(310, 390, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(190, 370, 47, 13))
        self.label_17.setObjectName("label_17")
        self.spinBox_k = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_k.setGeometry(QtCore.QRect(190, 390, 111, 22))
        self.spinBox_k.setMinimum(20)
        self.spinBox_k.setMaximum(30)
        self.spinBox_k.setProperty("value", 25)
        self.spinBox_k.setObjectName("spinBox_k")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(310, 440, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(190, 420, 47, 13))
        self.label_13.setObjectName("label_13")
        self.spinBox_p_prd = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_p_prd.setGeometry(QtCore.QRect(190, 440, 111, 22))
        self.spinBox_p_prd.setMinimum(-23)
        self.spinBox_p_prd.setMaximum(-3)
        self.spinBox_p_prd.setProperty("value", -9)
        self.spinBox_p_prd.setObjectName("spinBox_p_prd")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 410, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(10, 460, 47, 13))
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(130, 430, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.spinBox_z1 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_z1.setGeometry(QtCore.QRect(10, 430, 111, 22))
        self.spinBox_z1.setMinimum(10)
        self.spinBox_z1.setMaximum(12)
        self.spinBox_z1.setProperty("value", 10)
        self.spinBox_z1.setObjectName("spinBox_z1")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(130, 480, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.spinBox_z2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_z2.setGeometry(QtCore.QRect(10, 480, 111, 22))
        self.spinBox_z2.setMinimum(15)
        self.spinBox_z2.setMaximum(20)
        self.spinBox_z2.setProperty("value", 17)
        self.spinBox_z2.setObjectName("spinBox_z2")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(310, 490, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(190, 470, 47, 13))
        self.label_23.setObjectName("label_23")
        self.lineEdit_z_tr = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_z_tr.setGeometry(QtCore.QRect(190, 490, 113, 20))
        self.lineEdit_z_tr.setObjectName("lineEdit_z_tr")
        self.lineEdit_a_m = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a_m.setGeometry(QtCore.QRect(990, 40, 91, 20))
        self.lineEdit_a_m.setObjectName("lineEdit_a_m")
        self.lineEdit_h_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_h_a.setGeometry(QtCore.QRect(990, 110, 91, 20))
        self.lineEdit_h_a.setObjectName("lineEdit_h_a")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 10, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(860, 70, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1090, 30, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1090, 110, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.checkBox_polaris = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_polaris.setGeometry(QtCore.QRect(660, 40, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_polaris.setFont(font)
        self.checkBox_polaris.setObjectName("checkBox_polaris")
        self.label_antenna_img = QtWidgets.QLabel(self.centralwidget)
        self.label_antenna_img.setGeometry(QtCore.QRect(380, 50, 111, 111))
        self.label_antenna_img.setText("")
        self.label_antenna_img.setObjectName("label_antenna_img")
        self.pushButton_arrow_down_per = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_down_per.setGeometry(QtCore.QRect(790, 180, 75, 23))
        self.pushButton_arrow_down_per.setObjectName("pushButton_arrow_down_per")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(760, 140, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.pushButton_arrow_up_per = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_up_per.setGeometry(QtCore.QRect(900, 180, 75, 23))
        self.pushButton_arrow_up_per.setObjectName("pushButton_arrow_up_per")
        self.lineEdit_p_per = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_p_per.setGeometry(QtCore.QRect(990, 180, 91, 20))
        self.lineEdit_p_per.setObjectName("lineEdit_p_per")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(1090, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1090, 250, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(960, 220, 161, 16))
        self.label_34.setObjectName("label_34")
        self.lineEdit_p_p_vh_prm = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_p_p_vh_prm.setGeometry(QtCore.QRect(992, 250, 91, 20))
        self.lineEdit_p_p_vh_prm.setObjectName("lineEdit_p_p_vh_prm")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(790, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.pushButton_arrow_up_pom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_up_pom.setGeometry(QtCore.QRect(900, 250, 75, 23))
        self.pushButton_arrow_up_pom.setObjectName("pushButton_arrow_up_pom")
        self.pushButton_arrow_down_pom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arrow_down_pom.setGeometry(QtCore.QRect(790, 250, 75, 23))
        self.pushButton_arrow_down_pom.setObjectName("pushButton_arrow_down_pom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_arrow_left.setText(_translate("MainWindow", "˂"))
        self.pushButton_arrow_right.setText(_translate("MainWindow", "˃"))
        self.pushButton_arrow_up.setText(_translate("MainWindow", "˄"))
        self.pushButton_arrow_down.setText(_translate("MainWindow", "˅"))
        self.groupBox.setTitle(_translate("MainWindow", "ПУ"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#00aa00;\">Некоторый</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#00aa00;\">Тестовый</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#00aa00;\">Текст</span></p></body></html>"))
        self.pushButton_message.setText(_translate("MainWindow", "Отправить"))
        self.label_49.setText(_translate("MainWindow", "Поле ввода сообщения"))
        self.label.setText(_translate("MainWindow", "Спсиок доступных комманд"))
        self.plainTextEdit_commands_list.setPlainText(_translate("MainWindow", "Перейти на высоту: _(число от 7 до 20)\n"
"Перейти на высоту 4 метра и сменить поляризацию\n"
"Направить антенну на азимут магнитный: _(число от 0 до 355)\n"
"Перейти в режим работы: _(А6/Е1)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Основное окно"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Графики и диаграммы"))
        self.label_36.setText(_translate("MainWindow", "дБ"))
        self.pushButton_get_result.setText(_translate("MainWindow", "Расчет"))
        self.label_35.setText(_translate("MainWindow", "Итоговый результат:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Основные компоненты"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Е1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "А6"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ц68"))
        self.label_6.setText(_translate("MainWindow", "Режим работы РРС"))
        self.lineEdit_am_korr.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "o"))
        self.label_26.setText(_translate("MainWindow", "Ам корр"))
        self.label_40.setText(_translate("MainWindow", "o"))
        self.label_39.setText(_translate("MainWindow", "β"))
        self.label_8.setText(_translate("MainWindow", "o"))
        self.label_7.setText(_translate("MainWindow", "βкорр"))
        self.label_27.setText(_translate("MainWindow", "o"))
        self.label_28.setText(_translate("MainWindow", "a(прд)"))
        self.lineEdit_a.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "дБ"))
        self.lineEdit_g_prd.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "Gпрд(а)"))
        self.label_37.setText(_translate("MainWindow", "дБ"))
        self.label_38.setText(_translate("MainWindow", "Gпрм(а)"))
        self.lineEdit_g_prm.setText(_translate("MainWindow", "3"))
        self.label_43.setText(_translate("MainWindow", "a(прм)"))
        self.label_44.setText(_translate("MainWindow", "o"))
        self.label_42.setText(_translate("MainWindow", "дБ"))
        self.lineEdit_g_prm_p.setText(_translate("MainWindow", "3"))
        self.label_41.setText(_translate("MainWindow", "Gпрм(а)п"))
        self.label_45.setText(_translate("MainWindow", "o"))
        self.label_46.setText(_translate("MainWindow", "a(прм)п"))
        self.label_31.setText(_translate("MainWindow", "o"))
        self.label_32.setText(_translate("MainWindow", "Am(п)"))
        self.label_29.setText(_translate("MainWindow", "м"))
        self.label_30.setText(_translate("MainWindow", "H korr"))
        self.lineEdit_h_korr.setText(_translate("MainWindow", "16"))
        self.label_14.setText(_translate("MainWindow", "дБ"))
        self.label_12.setText(_translate("MainWindow", "Wc(h)"))
        self.lineEdit_w_c.setText(_translate("MainWindow", "15"))
        self.label_16.setText(_translate("MainWindow", "дБ"))
        self.lineEdit_w_p.setText(_translate("MainWindow", "15"))
        self.label_15.setText(_translate("MainWindow", "Wп(h)"))
        self.label_18.setText(_translate("MainWindow", "дБ"))
        self.label_17.setText(_translate("MainWindow", "К"))
        self.label_11.setText(_translate("MainWindow", "дБ"))
        self.label_13.setText(_translate("MainWindow", "p(прд)"))
        self.label_19.setText(_translate("MainWindow", "z1"))
        self.label_22.setText(_translate("MainWindow", "z2"))
        self.label_20.setText(_translate("MainWindow", "дБ"))
        self.label_21.setText(_translate("MainWindow", "дБ"))
        self.label_24.setText(_translate("MainWindow", "дБ"))
        self.label_23.setText(_translate("MainWindow", "z тр"))
        self.lineEdit_z_tr.setText(_translate("MainWindow", "0"))
        self.lineEdit_a_m.setText(_translate("MainWindow", "210"))
        self.lineEdit_h_a.setText(_translate("MainWindow", "16"))
        self.label_2.setText(_translate("MainWindow", "Aм"))
        self.label_3.setText(_translate("MainWindow", "На"))
        self.label_4.setText(_translate("MainWindow", "o"))
        self.label_5.setText(_translate("MainWindow", "м"))
        self.checkBox_polaris.setText(_translate("MainWindow", "Поляризация"))
        self.pushButton_arrow_down_per.setText(_translate("MainWindow", "˅"))
        self.label_47.setText(_translate("MainWindow", "Мощность передатчика корреспондента"))
        self.pushButton_arrow_up_per.setText(_translate("MainWindow", "˄"))
        self.lineEdit_p_per.setText(_translate("MainWindow", "-9"))
        self.label_48.setText(_translate("MainWindow", "Дб"))
        self.label_33.setText(_translate("MainWindow", "дБ"))
        self.label_34.setText(_translate("MainWindow", "p(п)(вх.прм)"))
        self.lineEdit_p_p_vh_prm.setText(_translate("MainWindow", "-7"))
        self.label_50.setText(_translate("MainWindow", "Мощность помехи"))
        self.pushButton_arrow_up_pom.setText(_translate("MainWindow", "˄"))
        self.pushButton_arrow_down_pom.setText(_translate("MainWindow", "˅"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
