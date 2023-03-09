#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QMessageBox, QProgressBar, QComboBox, QInputDialog, QLineEdit, QTextEdit, QGridLayout, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel,
                             QMenu, QDesktopWidget, QAction, QFileDialog, QApplication, QPushButton, QMessageBox)
from PyQt5 import QtWidgets
import sys
import mt
import re


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.sheetName = ''
        self.excelName = ''
        self.initUI()

    # 初始化控件
    def initUI(self):
        # button按钮创建;初始化默认大小;button按钮的位置
        btnExe = QPushButton('执行', self)
        btnExe.resize(btnExe.sizeHint())
        btnSelect = QPushButton('选择', self)
        btnSelect.resize(btnSelect.sizeHint())
        # btnExe.move(280, 0)

        # label标签;abel标签的位置
        lblInput = QLabel('请选择需要分析的Excel文件:')
        lblSheetNames = QLabel('请选择需要分析的Sheet工作簿:')

        # lblInput.move(50, 50)

        # 下拉选择
        self.comboText = QComboBox()

        # Text编辑标签
        # self.txtEdit = QTextEdit()
        self.qLine = QLineEdit(self)
        self.qLine.setReadOnly(True)

        # # 鼠标显示label
        # x = 0
        # y = 0
        # self.text = "x: {0},  y: {1}".format(x, y)
        # self.label = QLabel(self.text, self)

        # 状态栏statusBar
        # self.statusBar().showMessage('状态:就绪')
        # QAction是菜单栏、工具栏或者快捷键的动作的组合
        # 创建了一个图标、一个exit的标签
        # openFile = QAction(QIcon('open.png'), 'Open', self)
        # 快捷键组合
        # openFile.setShortcut('Ctrl+O')
        # openFile.setStatusTip('Open new File')
        # openFile.triggered.connect(self.showDialog)

        # 进度条菜单;时间进度
        # barProgress = QProgressBar()
        # self.timer = QBasicTimer()
        # self.step = 0

        # 框架布局;在使用QMainWindow中要注意初始化QWidget
        widget = QWidget()
        self.setCentralWidget(widget)
        # 栅格布局初始化;设置布局格式为栅格布局;添加控件在0行1列;添加控件在3行1列占用1行3列
        grid = QGridLayout()
        widget.setLayout(grid)
        grid.addWidget(lblInput, 0, 0)
        grid.addWidget(self.qLine, 1, 0)
        grid.addWidget(btnSelect, 1, 1)
        grid.addWidget(lblSheetNames, 2, 0)
        grid.addWidget(self.comboText, 3, 0)
        grid.addWidget(btnExe, 3, 1)
        # grid.addWidget(barProgress, 4, 0, 1, 2)
        # grid.addWidget(self.txtEdit, 3, 0, 3, 3)
        # grid.addWidget(self.label, 3, 1, 1, 3)

        # # 盒布局-水平布局;增加弹性空间比例1;在布局内加入控件
        # hBox = QHBoxLayout()
        # hBox.addStretch(1)
        # hBox.addWidget(lblInput)
        # hBox.addWidget(btnExe)
        # # hBox.addWidget(btnA)
        # # 盒布局-垂直布局;增加弹性空间;在布局内加入控件水平布局
        # vBox = QVBoxLayout()
        # vBox.addStretch(1)
        # vBox.addLayout(hBox)
        # self.setLayout(vBox)

        # 设置事件
        # 设置鼠标事件
        widget.setMouseTracking(True)
        # button按钮触发事件
        btnSelect.clicked.connect(self.showDialog)
        # btnExe.clicked.connect(self.doAction)
        btnExe.clicked.connect(self.createExcel)

        # 框架整体
        # self.setGeometry(300, 300, 350, 300)
        self.resize(350, 300)
        self.center()
        self.setWindowTitle('码头停车场excel分析')
        self.show()

    # 时间函数
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    # 开始执行进度条
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    # 获取鼠标事件
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)

    # 框架居中显示

    def center(self):
        # 获得所在框架
        qr = self.frameGeometry()
        # 获取显示器分辨率,得到中间点像素
        cp = QDesktopWidget().availableGeometry().center()
        # 将框架放置在中间点位置
        qr.moveCenter(cp)
        # 将主窗口左上角移动到框架左上角
        self.move(qr.topLeft())

    # 打开文件对话框;fname获取文件路径;
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, '选择文件', '/home')
        if fname[0]:
            # f = open(fname[0], 'r')
            # with f:
            #     data = f.read()
            #     self.txtEdit.setText(data)
            # self.txtEdit.setText(fname[0])
            # self.comboText.clear()
            pattern = re.compile(r'[^<>/\\\|:""\*\?]+\.\w+$')
            self.fileName = pattern.search(fname[0])
            self.qLine.setText(self.fileName.group())
            sheetNames = mt.loadExcel(self.fileName.group())
            self.comboText.addItem('请选择')
            for i in sheetNames:
                self.comboText.addItem(i)
            # print(self.comboText.currentText())

        # text, ok = QInputDialog.getText(self, '', '请输入要转换的工作簿:')
        # if ok:
        #     self.qLine.setText(str(text))

    # # 关闭程事件
    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Message',
    #                                  "确定要关闭程序吗?", QMessageBox.Yes
    #                                  | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
    def createExcel(self):
        # self.statusBar().clearMessage()
        # self.statusBar().showMessage('状态:执行中,请等待...')
        excelPath = mt.createExcel(
            self.fileName.group(), self.comboText.currentText())
        QtWidgets.QMessageBox.information(
            self, '提示', 'excel分析文件已生成! \n \n保存在:' + excelPath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Parking = Example()
    sys.exit(app.exec_())
