#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QPixmap
from PyQt5.QtCore import Qt, QPoint
from GUI.main_emu import Ui_MainWindow


class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = None
        # self.change_size(341, 300)
        self.setupUi(self)
        self.setWindowTitle('Основное окно эмулятора')
        self.img_width = 1150
        self.img_height = 280
        self.img_num = 0
        self.img_num_h = 0
        self.antenna_height = 80
        self.diag_num = 210
        self.img_address = f'img/landscape/horizon_main_step_{self.img_num}{self.img_num_h}.jpg'
        self.diag_address = f'img/diagram/{self.diag_num}grad.jpg'
        self.image = QPixmap(self.img_address).scaled(
            self.img_width, self.img_height)
        self.diagram = QPixmap(self.diag_address)
        self.img_label = self.label
        self.antenna_w = 90
        self.antenna_h = 60
        # self.label.setText("<h2 style='color: blue'>img/horizon_main.jpg</h2>")
        # w = self.image.size().width()
        # h = self.image.size().height()
        # self.background_image = self.img_label
        # self.background_image.move(w - 240, h - 100)
        self.pushButton_arrow_up.clicked.connect(self.change_horizont_up)
        self.pushButton_arrow_down.clicked.connect(self.change_horizont_down)
        self.pushButton_arrow_right.clicked.connect(self.change_horizont_right)
        self.pushButton_arrow_left.clicked.connect(self.change_horizont_left)
        self.checkBox_polaris.stateChanged.connect(self.change_horizont_check)
        self.pushButton_get_result.clicked.connect(self.get_main_result)
        self.antenna_x = self.label_antenna_img.x()
        self.antenna_y = self.label_antenna_img.y()
        self.left_line_antenna = 330
        self.right_line_antenna = 530
        self.groupBox_3.setVisible(False)
        self.groupBox_5.setStyleSheet("background-color: black;")
        self.groupBox_login.setStyleSheet("background-color: white;")
        self.groupBox_additional_func.setStyleSheet("background-color: white;")
        self.textBrowser.setStyleSheet(
            "background-color: black; color: green; text-align: center; content-align: center; border: none; font-size: 14px")
        self.textBrowser.setText("")
        self.checkBox_polaris.setEnabled(False)
        self.pushButton_arrow_up_per.clicked.connect(self.change_per_up)
        self.pushButton_arrow_down_per.clicked.connect(self.change_per_down)
        self.pushButton_arrow_up_pom.clicked.connect(self.change_pom_up)
        self.pushButton_arrow_down_pom.clicked.connect(self.change_pom_down)
        self.pushButton_message.clicked.connect(self.get_chat)
        self.listView.clicked.connect(self.get_val_list_view)
        self.checkBox_polaris.stateChanged.connect(self.result_check)
        self.checkBox_polaris_2.stateChanged.connect(self.result_check)
        self.checkBox_polaris_3.stateChanged.connect(self.result_check)
        self.add_val_list_view()
        self.result_check()
        self.user = 'Гость'
        self.login_val = 'admin'
        self.password_val = '1'
        self.groupBox_login.setVisible(False)
        self.groupBox_additional_func.setVisible(False)
        self.pushButton_entry_config.clicked.connect(self.login)
        self.pushButton_login_next.clicked.connect(self.open_config)
        self.pushButton_login_back.clicked.connect(self.close_login)
        self.pushButton_close_admin_pannel.clicked.connect(self.close_config)
        self.pushButton_logout.clicked.connect(self.logout_user)
        self.pushButton_change_pass.clicked.connect(self.change_pass)
        self.select_pass()

    def select_pass(self):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        select_query = 'SELECT * FROM pass'
        cursor.execute(select_query)
        rows = cursor.fetchall()
        self.password_val = rows[0][1]

        conn.commit()
        conn.close()



    def login(self):
        if self.label_52.text() == 'Админ':
            self.groupBox_additional_func.setVisible(True)
        else:
            self.groupBox_login.setVisible(True)

    def open_config(self):
        if self.lineEdit_username.text() == self.login_val and self.lineEdit_password.text() == self.password_val:
            self.groupBox_login.setVisible(False)
            self.lineEdit_username.setText('')
            self.lineEdit_password.setText('')
            self.groupBox_additional_func.setVisible(True)
            self.label_52.setText('Админ')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Неверно введен логин или пароль!")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()

    def close_login(self):
        self.groupBox_login.setVisible(False)
        self.lineEdit_username.setText('')
        self.lineEdit_password.setText('')

    def close_config(self):
        self.lineEdit_new_pass.setText('')
        self.lineEdit_new_pass_repeat.setText('')
        self.groupBox_additional_func.setVisible(False)

    def logout_user(self):
        self.label_52.setText('Гость')

    def change_pass(self):
        if self.lineEdit_new_pass_repeat.text() == self.lineEdit_new_pass.text() != '':
            conn = sqlite3.connect('main.db')
            cursor = conn.cursor()

            update_query = 'UPDATE pass SET pass = ? WHERE id = ?'
            data = (f'{self.lineEdit_new_pass_repeat.text()}', 1)  # Укажите новые данныеВыполняем запрос на обновление
            cursor.execute(update_query, data)

            conn.commit()
            conn.close()
            self.select_pass()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("пароль успешно изменен!")
            msg.setWindowTitle("Успешно!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Пароли не совпадают или пароль пустой!")
            msg.setWindowTitle("Ошибка!")
            msg.exec_()

    def add_val_list_view(self):
        entries = ['Перейти на высоту: _(число от 7 до 20)', 'Перейти на высоту 4 метра и сменить поляризацию',
                   'Направить антенну на азимут магнитный: _(число от 0 до 355)', 'Перейти в режим работы: _(А6/Е1)']
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            self.model.appendRow(item)

    def get_val_list_view(self):
        index = self.listView.currentIndex()
        if index.isValid():
            # Использование модели чтобы получить данные
            item_data = self.model.data(index)
            res_str = ''
            if item_data == 'Перейти на высоту: _(число от 7 до 20)':
                res_str = 'Перейти на высоту: '
            elif item_data == 'Перейти на высоту 4 метра и сменить поляризацию':
                res_str = 'Перейти на высоту 4 метра и сменить поляризацию'
            elif item_data == 'Направить антенну на азимут магнитный: _(число от 0 до 355)':
                res_str = 'Направить антенну на азимут магнитный: '
            elif item_data == 'Перейти в режим работы: _(А6/Е1)':
                res_str = 'Перейти в режим работы: '
            self.lineEdit_message.setText(res_str)

    def change_size(self, width, height):
        self.setFixedWidth(width)
        self.setFixedHeight(height)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.img_address = f'img/landscape/horizon_main_step_{self.img_num}{self.img_num_h}.jpg'
        self.diag_address = f'img/diagram/{self.diag_num}grad.png'
        self.image = QPixmap(self.img_address).scaled(
            self.img_width, self.img_height)
        qp.drawPixmap(QPoint(), self.image.scaled(self.img_width, self.img_height))  # +++
        qp.setPen(QPen(Qt.black, 2))
        qp.drawLine(self.antenna_x + 49, self.antenna_y + 100, 430, 278)
        qp.drawLine(self.antenna_x + 49, self.antenna_y + 90, self.right_line_antenna, 278)
        qp.drawLine(self.antenna_x + 49, self.antenna_y + 90, self.left_line_antenna, 278)
        # self.drawLines(qp)
        # self.drawAntenna(qp)
        self.label_antenna_img.move(self.antenna_x, self.antenna_y)
        self.drawAntennaImg(qp)
        self.drawDiagrammImg(qp)

        # self.drawBrushes(qp)
        qp.end()

    def change_horizont_up(self):
        if int(self.lineEdit_h_a.text()) < 20 and self.antenna_height > 70:
            self.lineEdit_h_a.setText(str(int(self.lineEdit_h_a.text()) + 1))
            self.antenna_height -= 1
            self.antenna_y -= 10
            self.label_antenna_img.move(self.antenna_x, self.antenna_y)
            self.right_line_antenna += 7
            self.left_line_antenna -= 7
            self.img_num_h += 1
        if int(self.lineEdit_h_a.text()) == 4:
            self.checkBox_polaris.setEnabled(True)
        else:
            self.checkBox_polaris.setEnabled(False)
        self.update()
        self.result_check()

    def change_horizont_down(self):
        if int(self.lineEdit_h_a.text()) > 4:
            self.lineEdit_h_a.setText(str(int(self.lineEdit_h_a.text()) - 1))
            self.antenna_height += 1
            self.antenna_y += 10
            self.right_line_antenna -= 7
            self.left_line_antenna += 7
            self.img_num_h -= 1
        if int(self.lineEdit_h_a.text()) == 4:
            self.checkBox_polaris.setEnabled(True)
        else:
            self.checkBox_polaris.setEnabled(False)
        self.update()
        self.result_check()

    def change_horizont_left(self):
        if int(self.lineEdit_am_korr.text()) - 5 <= 0:
            self.lineEdit_am_korr.setText(str((int(self.lineEdit_am_korr.text()) - 5 + 360) % 360))
        else:
            self.lineEdit_am_korr.setText(str(int(self.lineEdit_am_korr.text()) - 5))
        self.diag_num = self.diag_num - 5
        if self.diag_num < 0:
            self.diag_num += 360
        if self.img_num - 1 < 0:
            self.img_num = self.img_num + 9
        else:
            self.img_num -= 1
        self.update()
        self.result_check()

    def change_horizont_right(self):
        if int(self.lineEdit_am_korr.text()) + 5 > 359:
            self.lineEdit_am_korr.setText(str((int(self.lineEdit_am_korr.text()) + 5) % 360))
        else:
            self.lineEdit_am_korr.setText(str(int(self.lineEdit_am_korr.text()) + 5))
        self.img_num = (self.img_num + 1) % 10
        self.diag_num = (self.diag_num + 5) % 360
        self.update()
        self.result_check()

    def change_horizont_check(self):
        if self.checkBox_polaris.isChecked():
            self.antenna_w = 60
            self.antenna_h = 90
        else:
            self.antenna_h = 60
            self.antenna_w = 90

        self.update()

    def drawAntenna(self, qp):
        brush = QBrush(Qt.SolidPattern)

        brush.setStyle(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(400, self.antenna_height, self.antenna_w, self.antenna_h)

        # qp.setPen(QPen(Qt.red, 5))
        # qp.drawLine(10, 10, 500, 500)

    def drawDiagrammImg(self, qp):
        pixmap = QPixmap(self.diag_address).scaled(600, 500)
        self.label_diagram.setPixmap(pixmap)

    def drawAntennaImg(self, qp):
        if self.checkBox_polaris.isChecked():
            pixmap = QPixmap('img/antenna_v_100px.png')

        else:
            pixmap = QPixmap('img/antenna_h_100px.png')
        self.label_antenna_img.setPixmap(pixmap)

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)

    def drawBrushes(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)

    def result_check(self):
        if self.lineEdit_a_m.text() == '':
            self.lineEdit_a_m.setText('30')
        if self.lineEdit_h_a.text() == '':
            self.lineEdit_h_a.setText('16')
        if self.lineEdit_am_korr.text() == '':
            self.lineEdit_am_korr.setText('210')
        if self.lineEdit_b_korr.text() == '':
            self.lineEdit_b_korr.setText('215')
        if self.lineEdit_a.text() == '':
            self.lineEdit_a.setText('0')
        if self.lineEdit_g_prd.text() == '':
            self.lineEdit_g_prd.setText('3')
        if self.spinBox_p_prd.text() == '':
            self.spinBox_p_prd.setText('-9')
        if self.lineEdit_w_c.text() == '':
            self.lineEdit_w_c.setText('15')
        if self.lineEdit_w_p.text() == '':
            self.lineEdit_w_p.setText('15')
        if self.lineEdit_k.text() == '':
            self.lineEdit_k.setText('0')
        if self.spinBox_z1.text() == '':
            self.spinBox_z1.setText('10')
        if self.spinBox_z2.text() == '':
            self.spinBox_z2.setText('17')
        if self.lineEdit_z_tr.text() == '':
            self.lineEdit_z_tr.setText('0')
        if self.lineEdit_h_korr.text() == '':
            self.lineEdit_h_korr.setText('16')
        if self.spinBox_a_m_p.text() == '':
            self.spinBox_a_m_p.setText('70')
        if self.lineEdit_p_p_vh_prm.text() == '':
            self.lineEdit_p_p_vh_prm.setText('-7')
        if self.lineEdit_b.text() == '':
            self.lineEdit_b.setText('30')
        # self.lineEdit_am_korr.setText(str((int(self.lineEdit_b.text()) + 180) % 360))
        self.lineEdit_b_korr.setText(str((int(self.lineEdit_a_m.text()) + 185) % 360))
        self.lineEdit_a.setText(str(abs(int(self.lineEdit_b_korr.text()) - int(self.lineEdit_am_korr.text()))))
        self.lineEdit_b.setText(self.lineEdit_a_m.text())
        self.lineEdit_a_prm.setText(str(abs(int(self.lineEdit_b.text()) - int(self.lineEdit_a_m.text()))))
        self.lineEdit_a_prm_p.setText(str(abs(int(self.lineEdit_b.text()) - int(self.spinBox_a_m_p.text()))))

        if int(self.lineEdit_a.text()) == 0:
            self.lineEdit_g_prd.setText('13')
        elif int(self.lineEdit_a.text()) == 5 or int(self.lineEdit_a.text()) == 355:
            self.lineEdit_g_prd.setText('12.7')
        elif int(self.lineEdit_a.text()) == 10 or int(self.lineEdit_a.text()) == 350:
            self.lineEdit_g_prd.setText('12')
        elif int(self.lineEdit_a.text()) == 15 or int(self.lineEdit_a.text()) == 345:
            self.lineEdit_g_prd.setText('10')
        elif 20 <= int(self.lineEdit_a.text()) <= 55 or 305 <= int(self.lineEdit_a.text()) <= 340:
            self.lineEdit_g_prd.setText('3')
        elif int(self.lineEdit_a.text()) == 60 or int(self.lineEdit_a.text()) == 300:
            self.lineEdit_g_prd.setText('0')
        elif int(self.lineEdit_a.text()) == 75 or int(self.lineEdit_a.text()) == 285:
            self.lineEdit_g_prd.setText('5')
        elif 80 <= int(self.lineEdit_a.text()) <= 130 or 230 <= int(self.lineEdit_a.text()) <= 280:
            self.lineEdit_g_prd.setText('0')
        elif int(self.lineEdit_a.text()) == 135 or int(self.lineEdit_a.text()) == 225:
            self.lineEdit_g_prd.setText('3')
        elif 140 <= int(self.lineEdit_a.text()) <= 175 or 185 <= int(self.lineEdit_a.text()) <= 220:
            self.lineEdit_g_prd.setText('0')
        elif int(self.lineEdit_a.text()) == 180:
            self.lineEdit_g_prd.setText('3')

        if int(self.lineEdit_a_prm.text()) == 0:
            self.lineEdit_g_prm.setText('13')
        elif int(self.lineEdit_a_prm.text()) == 5 or int(self.lineEdit_a_prm.text()) == 355:
            self.lineEdit_g_prm.setText('12.7')
        elif int(self.lineEdit_a_prm.text()) == 10 or int(self.lineEdit_a_prm.text()) == 350:
            self.lineEdit_g_prm.setText('12')
        elif int(self.lineEdit_a_prm.text()) == 15 or int(self.lineEdit_a_prm.text()) == 345:
            self.lineEdit_g_prm.setText('10')
        elif 20 <= int(self.lineEdit_a_prm.text()) <= 55 or 305 <= int(self.lineEdit_a_prm.text()) <= 340:
            self.lineEdit_g_prm.setText('3')
        elif int(self.lineEdit_a_prm.text()) == 60 or int(self.lineEdit_a_prm.text()) == 300:
            self.lineEdit_g_prm.setText('0')
        elif int(self.lineEdit_a_prm.text()) == 75 or int(self.lineEdit_a_prm.text()) == 285:
            self.lineEdit_g_prm.setText('5')
        elif 80 <= int(self.lineEdit_a_prm.text()) <= 130 or 230 <= int(self.lineEdit_a_prm.text()) <= 280:
            self.lineEdit_g_prm.setText('0')
        elif int(self.lineEdit_a_prm.text()) == 135 or int(self.lineEdit_a_prm.text()) == 225:
            self.lineEdit_g_prm.setText('3')
        elif 140 <= int(self.lineEdit_a_prm.text()) <= 175 or 185 <= int(self.lineEdit_a_prm.text()) <= 220:
            self.lineEdit_g_prm.setText('0')
        elif int(self.lineEdit_a_prm.text()) == 180:
            self.lineEdit_g_prm.setText('3')

        if int(self.lineEdit_a_prm_p.text()) == 0:
            self.lineEdit_g_prm_p.setText('13')
        elif int(self.lineEdit_a_prm_p.text()) == 5 or int(self.lineEdit_a_prm_p.text()) == 355:
            self.lineEdit_g_prm_p.setText('12.7')
        elif int(self.lineEdit_a_prm_p.text()) == 10 or int(self.lineEdit_a_prm_p.text()) == 350:
            self.lineEdit_g_prm_p.setText('12')
        elif int(self.lineEdit_a_prm_p.text()) == 15 or int(self.lineEdit_a_prm_p.text()) == 345:
            self.lineEdit_g_prm_p.setText('10')
        elif 20 <= int(self.lineEdit_a_prm_p.text()) <= 55 or 305 <= int(self.lineEdit_a_prm_p.text()) <= 340:
            self.lineEdit_g_prm_p.setText('3')
        elif int(self.lineEdit_a_prm_p.text()) == 60 or int(self.lineEdit_a_prm_p.text()) == 300:
            self.lineEdit_g_prm_p.setText('0')
        elif int(self.lineEdit_a_prm_p.text()) == 75 or int(self.lineEdit_a_prm_p.text()) == 285:
            self.lineEdit_g_prm_p.setText('5')
        elif 80 <= int(self.lineEdit_a_prm_p.text()) <= 130 or 230 <= int(self.lineEdit_a_prm_p.text()) <= 280:
            self.lineEdit_g_prm_p.setText('0')
        elif int(self.lineEdit_a_prm_p.text()) == 135 or int(self.lineEdit_a_prm_p.text()) == 225:
            self.lineEdit_g_prm_p.setText('3')
        elif 140 <= int(self.lineEdit_a_prm_p.text()) <= 175 or 185 <= int(self.lineEdit_a_prm_p.text()) <= 220:
            self.lineEdit_g_prm_p.setText('0')
        elif int(self.lineEdit_a_prm_p.text()) == 180:
            self.lineEdit_g_prm_p.setText('3')

        if self.lineEdit_h_korr.text() == '20' and self.lineEdit_h_a.text() == '20':
            self.lineEdit_w_c.setText('8')
        elif self.lineEdit_h_korr.text() == '16' and self.lineEdit_h_a.text() == '16':
            self.lineEdit_w_c.setText('9')
        elif self.lineEdit_h_korr.text() == '12' and self.lineEdit_h_a.text() == '12':
            self.lineEdit_w_c.setText('10')
        elif self.lineEdit_h_korr.text() == '20' and self.lineEdit_h_a.text() == '16' or self.lineEdit_h_korr.text() == '16' and self.lineEdit_h_a.text() == '20':
            self.lineEdit_w_c.setText('8.5')
        elif self.lineEdit_h_korr.text() == '20' and self.lineEdit_h_a.text() == '12' or self.lineEdit_h_korr.text() == '12' and self.lineEdit_h_a.text() == '20':
            self.lineEdit_w_c.setText('9')
        elif self.lineEdit_h_korr.text() == '16' and self.lineEdit_h_a.text() == '12' or self.lineEdit_h_korr.text() == '12' and self.lineEdit_h_a.text() == '16':
            self.lineEdit_w_c.setText('9')
        elif self.lineEdit_h_korr.text() == '20' and self.lineEdit_h_a.text() == '8' or self.lineEdit_h_korr.text() == '8' and self.lineEdit_h_a.text() == '20':
            self.lineEdit_w_c.setText('9')
        elif self.lineEdit_h_korr.text() == '20' and self.lineEdit_h_a.text() == '4' or self.lineEdit_h_korr.text() == '4' and self.lineEdit_h_a.text() == '20':
            self.lineEdit_w_c.setText('10')
        elif self.lineEdit_h_korr.text() == '16' and self.lineEdit_h_a.text() == '8' or self.lineEdit_h_korr.text() == '8' and self.lineEdit_h_a.text() == '16':
            self.lineEdit_w_c.setText('10')
        else:
            self.lineEdit_w_c.setText('15')

        if int(self.lineEdit_h_a.text()) == 20:
            self.lineEdit_w_p.setText('10.8')
        elif 16 < int(self.lineEdit_h_a.text()) <= 20:
            self.lineEdit_w_p.setText('11')
        elif 12 < int(self.lineEdit_h_a.text()) <= 16:
            self.lineEdit_w_p.setText('11.2')
        elif 4 < int(self.lineEdit_h_a.text()) <= 12:
            self.lineEdit_w_p.setText('15')

        self.lineEdit_z_tr.setText(str(int(self.spinBox_z1.text()) + int(self.spinBox_z2.text())))
        if self.checkBox_polaris.isChecked() or self.checkBox_polaris_2.isChecked() or self.checkBox_polaris_3.isChecked():
            self.lineEdit_k.setText('25')
        else:
            self.lineEdit_k.setText('0')

        # условный уровень помехи без учета коэффициента усиления антенны "нашего" приемника и затухания сигнала помехи в сторону "нашего" приемника
        # self.lineEdit_p_p_vh_prm.setText(
        #     str(float(self.spinBox_p_prd.text()) + float(self.lineEdit_g_prd.text()) - float(
        #         self.lineEdit_w_p.text()) - float(self.lineEdit_w_c.text())))

        self.result_calc()

    def result_calc(self):
        if int(self.lineEdit_h_a.text()) >= 7:
            result = (float(self.lineEdit_p_per.text()) + float(self.lineEdit_g_prd.text()) + float(
                self.lineEdit_a_prm.text()) - float(self.lineEdit_w_c.text())) - (
                             float(self.lineEdit_p_p_vh_prm.text()) + float(self.lineEdit_g_prm_p.text()) - float(
                         self.lineEdit_w_p.text())) + float(self.lineEdit_k.text())
            self.lineEdit_result.setText(str(round(result, 2)))
            if result < 10.5:
                self.textBrowser.setText('Коэффициент ошибки: 10^-3\nСвязи нет')
            elif result >= 10.5:
                self.textBrowser.setText('Коэффициент ошибки: 10^-6\nСвязь есть')
        else:
            self.lineEdit_result.setText('Связи нет')
            self.textBrowser.setText('Коэффициент ошибки: 10^-3\nСвязи нет')

    def change_per_up(self):
        if int(self.lineEdit_p_per.text()) < -3:
            self.lineEdit_p_per.setText(str(int(self.lineEdit_p_per.text()) + 1))
        self.update()
        self.result_check()

    def change_per_down(self):
        if int(self.lineEdit_p_per.text()) > -23:
            self.lineEdit_p_per.setText(str(int(self.lineEdit_p_per.text()) - 1))
        self.update()
        self.result_check()

    def change_pom_up(self):
        if int(self.lineEdit_p_p_vh_prm.text()) < -3:
            self.lineEdit_p_p_vh_prm.setText(str(int(self.lineEdit_p_p_vh_prm.text()) + 1))
        self.update()
        self.result_check()

    def change_pom_down(self):
        if int(self.lineEdit_p_p_vh_prm.text()) > -23:
            self.lineEdit_p_p_vh_prm.setText(str(int(self.lineEdit_p_p_vh_prm.text()) - 1))
        self.update()
        self.result_check()

    def get_main_result(self):
        self.result_check()
        self.result_calc()

    def get_chat(self):

        answer_dict = {'Перейти на высоту:': 'Перешел на высоту',
                       'Перейти на высоту 4 метра и сменить поляризацию': 'Перешел на высоту 4 метра и сменил поляризацию',
                       'Направить антенну на азимут магнитный:': 'Направил антенну на азимут магнитный',
                       'Перейти в режим работы:': 'Перешел в режим работы'}
        self.textEdit_message.append('- ' + self.lineEdit_message.text())
        result_answer = ''
        for num, el in enumerate(answer_dict.items()):
            if el[0] == 'Перейти на высоту:' and ('Перейти на высоту:' in self.lineEdit_message.text()):
                result_answer = el[1] + ' ' + self.lineEdit_message.text().split()[-1]
                self.lineEdit_h_korr.setText(self.lineEdit_message.text().split()[-1])
                self.textEdit_message.append(result_answer)
            elif el[0] == 'Перейти на высоту 4 метра и сменить поляризацию' and (
                    'Перейти на высоту 4 метра и сменить поляризацию' in self.lineEdit_message.text()):
                result_answer = el[1]
                self.lineEdit_h_korr.setText('4')
                if self.checkBox_polaris_2.isChecked():
                    self.checkBox_polaris_2.setChecked(False)
                else:
                    self.checkBox_polaris_2.setChecked(True)
                self.textEdit_message.append(result_answer)
            elif el[0] == 'Направить антенну на азимут магнитный:' and (
                    'Направить антенну на азимут магнитный:' in self.lineEdit_message.text()):
                result_answer = el[1] + ' ' + self.lineEdit_message.text().split()[-1]
                self.lineEdit_a_m.setText(self.lineEdit_message.text().split()[-1])
                self.textEdit_message.append(result_answer)
            elif el[0] == 'Перейти в режим работы:' and ('Перейти в режим работы:' in self.lineEdit_message.text()):
                result_answer = el[1] + ' ' + self.lineEdit_message.text().split()[-1]
                self.textEdit_message.append(result_answer)
        if result_answer == '':
            self.textEdit_message.append('Уточните команду!')
        self.get_main_result()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Example()
    w = MainClass()
    w.show()
    sys.exit(app.exec_())
