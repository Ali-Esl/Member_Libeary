

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from helper.api_helper import view
import mysql.connector as mc



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Admin Menu")
        Dialog.resize(456, 493)
        Dialog.setMinimumSize(QtCore.QSize(456, 493))
        Dialog.setMaximumSize(QtCore.QSize(456, 493))
        Dialog.setMouseTracking(False)
        self.Address_Input = QtWidgets.QLineEdit(parent=Dialog)
        self.Address_Input.setGeometry(QtCore.QRect(10, 160, 441, 111))
        self.Address_Input.setObjectName("Address_Input")
        self.ContactID_input = QtWidgets.QLineEdit(parent=Dialog)
        self.ContactID_input.setGeometry(QtCore.QRect(10, 10, 231, 22))
        self.ContactID_input.setObjectName("ContactID_input")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 441, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EditContact = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.EditContact.setStyleSheet("QPushButton{\n"
"    background: #dada39;\n"
"    color: white;\n"
"}")
        self.EditContact.setObjectName("EditContact")
        self.horizontalLayout.addWidget(self.EditContact)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.AddContact = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.AddContact.setStyleSheet("QPushButton{\n"
"    background: #4caf50;\n"
"    color: white;\n"
"}")
        self.AddContact.setObjectName("AddContact")
        self.horizontalLayout.addWidget(self.AddContact)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.RemoveContact = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.RemoveContact.setStyleSheet("QPushButton{\n"
"    background: #af4c5b;\n"
"    color: white;\n"
"}")
        self.RemoveContact.setObjectName("RemoveContact")
        self.horizontalLayout.addWidget(self.RemoveContact)
        self.layoutWidget1 = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 441, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FName_input = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.FName_input.setObjectName("FName_input")
        self.verticalLayout.addWidget(self.FName_input)
        self.Lname_input = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.Lname_input.setObjectName("Lname_input")
        self.verticalLayout.addWidget(self.Lname_input)
        self.PNumber_input = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.PNumber_input.setObjectName("PNumber_input")
        self.verticalLayout.addWidget(self.PNumber_input)
        self.ZIPcode_input = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.ZIPcode_input.setObjectName("ZIPcode_input")
        self.verticalLayout.addWidget(self.ZIPcode_input)
        self.StatusTable_ToolTip = QtWidgets.QTableWidget(parent=Dialog)
        self.StatusTable_ToolTip.setGeometry(QtCore.QRect(10, 280, 441, 161))
        self.StatusTable_ToolTip.setObjectName("StatusTable_ToolTip")
        self.StatusTable_ToolTip.setColumnCount(6)
        self.StatusTable_ToolTip.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.StatusTable_ToolTip.setHorizontalHeaderItem(5, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Admin Menu", "Admin Menu"))
        self.Address_Input.setPlaceholderText(_translate("Dialog", "Address Here"))
        self.ContactID_input.setPlaceholderText(_translate("Dialog", "Contact ID Here For Edit Or Delete"))
        self.EditContact.setText(_translate("Dialog", "Edit Contact"))
        self.AddContact.setText(_translate("Dialog", "Add Contact"))
        self.RemoveContact.setText(_translate("Dialog", "Remove Contact"))
        self.FName_input.setPlaceholderText(_translate("Dialog", "First Name Here"))
        self.Lname_input.setPlaceholderText(_translate("Dialog", "Last Name Here"))
        self.PNumber_input.setPlaceholderText(_translate("Dialog", "Phone Number Here"))
        self.ZIPcode_input.setPlaceholderText(_translate("Dialog", "ZIP Code Here"))
        self.View_Member()
        item = self.StatusTable_ToolTip.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.StatusTable_ToolTip.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First Name"))
        item = self.StatusTable_ToolTip.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Last Name"))
        item = self.StatusTable_ToolTip.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Phone Number"))
        item = self.StatusTable_ToolTip.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "ZIP Code"))
        item = self.StatusTable_ToolTip.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Address"))
        self.AddContact.clicked.connect(self.Add_Member)
        self.AddContact.clicked.connect(self.View_Member)
        self.EditContact.clicked.connect(self.Edit_Member)
        self.EditContact.clicked.connect(self.View_Member)
        self.RemoveContact.clicked.connect(self.Delete_Member)
        self.RemoveContact.clicked.connect(self.View_Member)
        
    def View_Member(self):
        view(name_table="info",tableWidget=self.StatusTable_ToolTip)
        
    def Add_Member(self):
        try:
            msg_box = QMessageBox()
            mydb = mc.connect(host="localhost", user="root", password="", database="library_member")
            mycursor = mydb.cursor()

            Member_name = self.FName_input.text()
            Member_Lname = self.Lname_input.text()
            Member_Phone = self.PNumber_input.text()
            Member_ZipCode = self.ZIPcode_input.text()
            Member_Address = self.Address_Input.text()
                                  
            if  Member_name == "" or Member_Lname == "" or Member_Phone == "" or Member_ZipCode == "" or Member_Address == "":
                msg_box.setIcon(QMessageBox.Icon.Warning)    
                msg_box.setStyleSheet("QLabel{ color: red; }")
                msg_box.setText("لطفا تمام فیلد ها رو پر کنید")
                msg_box.exec()
                return
            mycursor.execute("SELECT id FROM info")
            Id_count = mycursor.fetchall()
            query = "INSERT INTO info (ID,FName,LName,Phone,ZipCode,Address) VALUES (%s, %s, %s, %s, %s, %s)"        
            Values = (len(Id_count)+1,Member_name,Member_Lname,Member_Phone,Member_ZipCode,Member_Address)
            
            mycursor.execute(query,Values)
            mydb.commit()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet("QLabel{ color: green; }")
            msg_box.setText(f"شخص با موفقیت اضافه شد")
            msg_box.exec()
        except mc.Error as err:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet("QLabel{ color: red; }")
            msg_box.setText("Failed to connect to db\n"+err.msg)
            msg_box.exec()

    def Edit_Member(self):
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="library_member")
            Member_Id = self.ContactID_input.text()
            Member_name = self.FName_input.text()
            Member_Lname = self.Lname_input.text()
            Member_Phone = self.PNumber_input.text()
            Member_ZipCode = self.ZIPcode_input.text()
            Member_Address = self.Address_Input.text()
            
            if Member_Id == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStyleSheet("QLabel{ color: red; }")
                msg_box.setText("لطفا ایدی رو وارد کنید")
                msg_box.exec()
            else:
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM info WHERE id = %s", ((Member_Id,)))
                myresult = mycursor.fetchall()
                
                if len(myresult) != 0 and Member_name == "" and Member_Lname == "" and Member_Phone== "" and Member_ZipCode == "" and Member_Address == "":
                    self.FName_input.setText(str(myresult[0][1]))
                    self.Lname_input.setText(str(myresult[0][2]))
                    self.PNumber_input.setText(str(myresult[0][3]))
                    self.ZIPcode_input.setText(str(myresult[0][4]))
                    self.Address_Input.setText(str(myresult[0][5]))
                elif len(myresult) != 0 and Member_name != "" and Member_Lname != "" and Member_Phone != "" and Member_ZipCode != "" and Member_Address != "":
                    mycursor.execute("UPDATE info SET FName = %s WHERE id = %s",(Member_name,Member_Id,))
                    mycursor.execute("UPDATE info SET LName = %s WHERE id = %s",(Member_Lname,Member_Id,))
                    mycursor.execute("UPDATE info SET Phone = %s WHERE id = %s",(Member_Phone,Member_Id,))
                    mycursor.execute("UPDATE info SET ZipCode = %s WHERE id = %s",(Member_ZipCode,Member_Id,))
                    mycursor.execute("UPDATE info SET Address = %s WHERE id = %s",(Member_Address,Member_Id,))
                    mydb.commit()
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setStyleSheet("QLabel{ color: green; }")
                    msg_box.setText("ادیت شد")
                    msg_box.exec()
                else:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setStyleSheet("QLabel{ color: red; }")
                    msg_box.setText("لطفا ایدی درست رو وارد کنید")
                    msg_box.exec()
                
                
        except mc.Error as err:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet("QLabel{ color: red; }")
            msg_box.setText("Failed to connect to db\n"+err.msg)
            msg_box.exec()
    
    def Delete_Member(self):
        try:
            msg_box = QMessageBox()
                
            mydb = mc.connect(host="localhost", user="root", password="", database="library_member")
            mycursor = mydb.cursor()
            Member_Id = self.ContactID_input.text()
            if  Member_Id == "":
                msg_box.setIcon(QMessageBox.Icon.Warning)    
                msg_box.setStyleSheet("QLabel{ color: red; }")
                msg_box.setText("لطفا فیلد ایدی رو پر کنید")
                msg_box.exec()
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM info WHERE id=%s", (Member_Id,))
            mydb.commit()       
            cursor.close()
            msg_box.setIcon(QMessageBox.Icon.Information)    
            msg_box.setStyleSheet("QLabel{ color: red; }")
            msg_box.setText("ممبر با موفقیت حذف شد")
            msg_box.exec()
                
        except mc.Error as err:
            msg_box = QMessageBox()
                
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet("QLabel{ color: red; }")
            msg_box.setText("Failed to connect to db\n"+err.msg)
            msg_box.exec()