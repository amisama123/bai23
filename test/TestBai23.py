from PyQt6.QtWidgets import QApplication, QMainWindow

from chuong1_ham.BaiTap23.ui.MainWindow23Ext import MainWindow23Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow23Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
