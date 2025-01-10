import traceback

from Demos.win32gui_menu import MainWindow

from chuong1_ham.BaiTap23.ui.MainWindow23 import Ui_MainWindow


class MainWindow23Ext(Ui_MainWindow):
    def __init__(self):
        self.so_khach_hang=0
        self.soluong_mua_khachhang=0
        self.so_khach_hang_sv=0
        self.soluong_mua_khachhang_sv=0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonBanMoi.clicked.connect(self.xuly_banmoi)
        self.pushButtonTinh.clicked.connect(self.xuly_tinhtien)
        self.pushButtonThongKe.clicked.connect(self.xuly_thongke)
    def xuly_banmoi(self):
        try:
            self.lineEditTenKH.setText("")
            self.lineEditSoluong.setText("")
            self.checkBoxKhachSV.setChecked(False)
            self.lineEditThanhTien.setText("")
            self.lineEditTenKH.setFocus()
        except:
            traceback.print_exc()
    def xuly_tinhtien(self):
        name=self.lineEditTenKH.text()
        quantity=int(self.lineEditSoluong.text())
        if self.checkBoxKhachSV.isChecked()==True:
            self.so_khach_hang_sv=self.so_khach_hang_sv+1
            self.soluong_mua_khachhang_sv=self.soluong_mua_khachhang_sv+quantity
            money=quantity*20000*0.95
            self.lineEditThanhTien.setText(f"{money}")
        else:
            self.so_khach_hang=self.so_khach_hang+1
            self.soluong_mua_khachhang=self.soluong_mua_khachhang+quantity
            money=quantity*20000
            self.lineEditThanhTien.setText(f"{money}")
    def xuly_thongke(self):
        total_money=self.so_khach_hang*self.soluong_mua_khachhang*20000
        total_money_sv=self.so_khach_hang_sv*\
                        self.soluong_mua_khachhang_sv*20000*0.95
        self.lineEditTongKH.setText(f"{self.so_khach_hang}")
        self.lineEditTongKHlaSV.setText(f"{self.so_khach_hang_sv}")
        self.lineEditTongDoanhThu.settext(f"{total_money+total_money_sv}")