import mysql.connector as mc
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

def view(name_table,tableWidget,user=None,id=None):
    try:
        mydb = mc.connect(host="localhost", user="root", password="", database="library_member")
        mycursor = mydb.cursor()

        if user != None :
            mycursor.execute(f"SELECT * FROM {name_table} WHERE FName = '{user}'")
            data = mycursor.fetchall()
            if len(data) > 0:
                pass
            else:
                mycursor.execute(f"SELECT * FROM {name_table} WHERE LName = '{user}'")
                data = mycursor.fetchall()
                if len(data) > 0:
                    pass
                else:
                    mycursor.execute(f"SELECT * FROM {name_table} WHERE Phone = '{user}'")
                    data = mycursor.fetchall()
                    if len(data) > 0:
                        pass
                    else:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Icon.Information)
                        msg_box.setStyleSheet("QLabel{ color: red; }")
                        msg_box.setText("نام و نام خانوادگی و شماره یا ایدی مد نظر پیدا نشد!!!")
                        msg_box.exec()
            
        elif id != None:
            mycursor.execute(f"SELECT * FROM {name_table} WHERE id = '{id}'")
            data = mycursor.fetchall()
            if len(data) == 0:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStyleSheet("QLabel{ color: red; }")
                msg_box.setText("نام و نام خانوادگی و شماره یا ایدی مد نظر پیدا نشد!!!")
                msg_box.exec()
            
        else:
            mycursor.execute(f"SELECT * FROM {name_table}")    
            data = mycursor.fetchall()        
            
        tableWidget.setRowCount(0)
        for row_index,row_data in enumerate(data):
            tableWidget.insertRow(row_index)
            for col_index,col_data in enumerate(row_data):
                tableWidget.setItem(row_index,col_index,QtWidgets.QTableWidgetItem(str(col_data)))
                
    except mc.Error as err:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStyleSheet("QLabel{ color: red; }")
        msg_box.setText(str(err))
        msg_box.exec()