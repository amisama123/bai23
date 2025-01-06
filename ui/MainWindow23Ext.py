from Demos.win32gui_menu import MainWindow

from LearnCheckBoxDirectly.MainWindow import Ui_MainWindow


class MainWindow23Ext (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()