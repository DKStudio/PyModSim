# coding = utf-8
import sys
from QT import MainFrom

if __name__ == "__main__":
    #所有應用必須創建一個應用（Application)對象
    print("sys.path={}".format(sys.path))
    app = MainFrom.QtWidgets.QApplication(sys.argv)
    test = MainFrom.Window()
    sys.exit(app.exec_())