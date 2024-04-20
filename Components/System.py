from PyQt6.QtCore import Qt 
from UI.MainForm import Ui_MainWindow
from UI.ToolTip import Ui_Dialog
from PyQt6.QtWidgets import QMainWindow, QWidget,QDialog,QMessageBox,QTableWidgetItem
from mysql import connector as mc

class Library(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()
        self.ToolButton.clicked.connect(self.Add_Edit_Delete)

    def Add_Edit_Delete(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        dialog.exec()
    