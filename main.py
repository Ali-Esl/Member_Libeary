import sys,os
try:
    from PyQt6.QtWidgets import QApplication
    from Components.System import Library
except:
    os.system("pip install PyQt6 && pip install pyqt6-tools && pip install mysql-connector-python")
    from PyQt6.QtWidgets import QApplication
    from Components.System import Library

libraryApp = QApplication(sys.argv)
window = Library()
sys.exit(libraryApp.exec())