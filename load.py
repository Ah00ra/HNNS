from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QWidget
from PyQt5.uic import loadUi
import funcs


def is_float_value(value):
    try:
        float(value)
        return True
    except ValueError:
        return False




class Wire_Rope_Tables(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('wire_rope_tables.ui', self)
        self.textBrowser.setText("TEST")
        #self.table_widget = QtWidgets.QTableWidget(self)
        #self.table_widget.setRowCount(5)  
        #self.table_widget.setColumnCount(3) 
        #self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])
        ##self.table_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        ##self.table_widget.setFixedSize(self.table_widget.sizeHint())
        #self.table_widget.setColumnWidth(0, 200)
        #self.table_widget.setColumnWidth(1, 150)
        #self.table_widget.setColumnWidth(2, 150)
        #self.table_widget.setColumnWidth(3, 150)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi('main.ui', self)


        # roller chain table
        self.tableWidget_4.setColumnWidth(0, 200)
        self.tableWidget_4.setColumnWidth(1, 150)
        self.tableWidget_4.setColumnWidth(2, 150)
        self.tableWidget_4.setColumnWidth(3, 150)

        self.stackedWidget.setCurrentIndex(0)

        self.tableWidget.setHidden(True) 
        self.pushButton_10.setHidden(True)

        self.tableWidget_3.setHidden(True)
        self.pushButton_21.setHidden(True)
        # set hidden F2 form layout_9
        self.tableWidget_2.setHidden(True)
        self.pushButton_11.setHidden(True)
        self.DoubleSpinBox_11.setHidden(True)
        self.fDoubleSpinBox_13.setHidden(True)
        self.checkBox_14.setHidden(True)
        self.checkBox_15.setHidden(True)
        self.fDoubleSpinBox_14.setHidden(True)
        self.fDoubleSpinBox_15.setHidden(True)
        self.pushButton_16.setHidden(True)

        self.htext_44.setHidden(True)
        self.htext_45.setHidden(True)
        self.htext_46.setHidden(True)
        self.htext_47.setHidden(True)

        self.htext_17.setHidden(True)
        self.htext_18.setHidden(True)
        self.htext_19.setHidden(True)
        self.DdoubleSpinBox_10.setHidden(True)
        self.DdoubleSpinBox_11.setHidden(True)
        self.DdoubleSpinBox_14.setHidden(True)
        self.pushButton_7.setHidden(True)


        self.htext_20.setHidden(True)
        self.htext_21.setHidden(True)
        self.DdoubleSpinBox_15.setHidden(True)
        self.DdoubleSpinBox_16.setHidden(True)
        self.pushButton_8.setHidden(True)




        self.treeWidget.itemClicked['QTreeWidgetItem*','int'].connect(self.item_clicked)




    def item_clicked(self, item, column):
        if item.text(column) == "Chapter17":
    #              self.textBrowser.setText("You Clicked on Chapter17") 
                pass
        if  item.text(column) == "(F1)a-F2":
            self.pushButton_9.clicked.connect(self.f1a_f2)
            self.stackedWidget.setCurrentIndex(1) 

        if item.text(column) == "Belt":
    #              self.textBrowser.setText("You Clicked on Chapter17") 
            pass
        if item.text(column) == "Torque":
            self.stackedWidget.setCurrentIndex(2)
            # self.pushButton_20.clicked.connect(self.Torque_Belt)
            self.pushButton.clicked.connect(self.Torque_Belt)


        if item.text(column) == "Spur Gear":
            self.pushButton_2.clicked.connect(self.super_gear)
            self.stackedWidget.setCurrentIndex(3)

        if item.text(column) == "Open Belt":
            self.pushButton_3.clicked.connect(self.open_belt)
            self.stackedWidget.setCurrentIndex(4)

        if item.text(column) == "Crossed Belt":
            self.pushButton_4.clicked.connect(self.crossed_belt)
            self.stackedWidget.setCurrentIndex(5)

        if item.text(column) == "Belt Speed":
            self.pushButton_5.clicked.connect(self.belt_speed)
            self.stackedWidget.setCurrentIndex(6)

        if item.text(column) == "Fc Belt":
            #self.DdoubleSpinBox_13.setSpecialValueText('3') 
            self.pushButton_6.clicked.connect(self.fc_belt)
            self.pushButton_7.clicked.connect(self.omg)
            self.pushButton_8.clicked.connect(self.fc_belt_speed)
            self.stackedWidget.setCurrentIndex(7)

 #           self.pushButton_2.clicked.connect(self.super_gear)
        if item.text(column) == "exp(fΦ)":
            self.stackedWidget.setCurrentIndex(8)
            self.pushButton_10.clicked.connect(self.get_selected_row_data)
            self.pushButton_19.clicked.connect(self.expphi)
        
        
        if item.text(column) == "Fi":
            self.pushButton_13.clicked.connect(self.fi)
            self.pushButton_17.clicked.connect(self.fi2)
            self.stackedWidget.setCurrentIndex(9)

        
        if item.text(column) == "F2":
            self.pushButton_12.clicked.connect(self.f2)
            self.pushButton_16.clicked.connect(self.f1a_fromf2)
            self.pushButton_11.clicked.connect(self.get_selected_data)
            self.stackedWidget.setCurrentIndex(10)

        
        if item.text(column) == "F1a":
            self.pushButton_14.clicked.connect(self.f1a)
            self.pushButton_21.clicked.connect(self.get_selected_data_f1a)
            self.stackedWidget.setCurrentIndex(11)

        if item.text(column) == "f'":
            self.pushButton_18.clicked.connect(self.fprime)
            self.stackedWidget.setCurrentIndex(12)

        if item.text(column) == "dip":
            self.pushButton_20.clicked.connect(self.dip)
            self.stackedWidget.setCurrentIndex(15)
        
        if item.text(column) == "Sf":
            self.pushButton_23.clicked.connect(self.sfnp)
            self.pushButton_22.clicked.connect(self.sfsy)
            self.stackedWidget.setCurrentIndex(13)

        if item.text(column) == "b(min)":
            self.pushButton_25.clicked.connect(self.minibi)
            self.stackedWidget.setCurrentIndex(14)

        if item.text(column) == "(F1)a":
            self.pushButton_26.clicked.connect(self.f1pa)
            self.stackedWidget.setCurrentIndex(16)

        if item.text(column) == "ΔF":
            self.pushButton_24.clicked.connect(self.delltaf)
            self.stackedWidget.setCurrentIndex(17)

        if item.text(column) == "H(link-plate limited)":
            self.pushButton_30.clicked.connect(self.h_link_plate)
            self.stackedWidget.setCurrentIndex(21)

        if item.text(column) == "C":
            self.pushButton_31.clicked.connect(self.center_distance)
            self.stackedWidget.setCurrentIndex(22)    

        if item.text(column) == "L/p:No. Pitches":
            self.pushButton_32.clicked.connect(self.np_rc)
            self.stackedWidget.setCurrentIndex(23)

        if item.text(column) == "Ha":

            self.pushButton_34.clicked.connect(self.ha_roller_chain)
            self.stackedWidget.setCurrentIndex(24)

        if item.text(column) == "Ft":
            self.stackedWidget.setCurrentIndex(25)
            self.pushButton_35.clicked.connect(self.open_wire_rope_tables)
            self.pushButton_35.clicked.connect(self.wire_rope)



        if item.parent() is not None:
            parent = item.parent()
            parent_name = parent.text(0)
            ind = parent.indexOfChild(item)
            if parent_name == "Flat Metal Belt":
                if ind == 5:
                    self.pushButton_27.clicked.connect(self.f2metalbelt)
                    self.stackedWidget.setCurrentIndex(18)
                if ind == 6:
                    #!TODO: TAB JUMP D
                    print("IM IN")
                    self.pushButton_28.clicked.connect(self.fi_2)
                    self.stackedWidget.setCurrentIndex(19)

                if ind == 7:
                    self.pushButton_29.clicked.connect(self.fprime2)
                    self.stackedWidget.setCurrentIndex(20)


    def open_wire_rope_tables(self):
            # Create an instance of the second window
            self.wire_window = Wire_Rope_Tables()
            # Show the second window
            self.wire_window.textBrowser.append("dynamically text test")


            self.wire_window.show()

    def wire_rope(self):
        wcap = self.DoubleSpinBox_75.value()
        w = self.DoubleSpinBox_77.value()
        lcap = self.DoubleSpinBox_78.value()
        a = self.DoubleSpinBox_79.value()
        psu = self.DoubleSpinBox_80.value()
        dcap = self.DoubleSpinBox_81.value()
        er = self.DoubleSpinBox_83.value()
        dw = self.DoubleSpinBox_84.value()
        am = self.DoubleSpinBox_85.value()

        m = self.comboBox_2.currentText()
        d = self.comboBox_3.currentText()
        ans = wcap, w,lcap, a, psu, dcap, er, dw, am, m, d
        ans = str(ans)
        self.textBrowser.setText(ans)
        

    def ha_roller_chain(self):
        nd = self.DoubleSpinBox_70.value()
        ks = self.DoubleSpinBox_71.value()
        hnom = self.DoubleSpinBox_72.value()
        ncap = self.DoubleSpinBox_73.value()
        v = self.DoubleSpinBox_74.value()

        pre_or_post = self.comboBox.currentText()

        #print(self.tableWidget_4.item(3,4))
        #print(self.tableWidget_4.row())
        ans, chain, types = funcs.ha_roller_chain(nd, ks, hnom, ncap, pre_or_post, v)
        print(types)

        row_count = self.tableWidget_4.rowCount()
        col_count = self.tableWidget_4.columnCount() 
        for i in range(row_count): 
            item = QTableWidgetItem(ans[i])  
            item.setTextAlignment(Qt.AlignCenter)

            item1 = QTableWidgetItem(chain[i]) 
            item1.setTextAlignment(Qt.AlignCenter)

            item2 = QTableWidgetItem(types[i]) 
            item2.setTextAlignment(Qt.AlignCenter)

            ind = i

            self.tableWidget_4.setItem(ind,1, item)
            self.tableWidget_4.setItem(ind,2, item1)
            self.tableWidget_4.setItem(ind,3, item2)


        #self.textBrowser.setText(ans)


    def np_rc(self):
        n1 = self.DoubleSpinBox_62.value()
        n2 = self.DoubleSpinBox_63.value()
        p = self.DoubleSpinBox_64.value()
        c = self.DoubleSpinBox_65.value()
        ans = str(funcs.np_rc(n1, n2, p, c))
        self.textBrowser.setText(ans)

    def center_distance(self):
        n1 = self.DoubleSpinBox_58.value()
        n2 = self.DoubleSpinBox_59.value()
        p = self.DoubleSpinBox_60.value()
        L = self.DoubleSpinBox_61.value()
        ans = str(funcs.center_distance(n1, n2, p, L))
        self.textBrowser.setText(ans)

    def h_link_plate(self):
        N = self.DoubleSpinBox_55.value()
        n = self.DoubleSpinBox_56.value()
        p = self.DoubleSpinBox_57.value()
        ans = str(funcs.h_link_plate(N, n, p,))
        self.textBrowser.setText(ans)



    def fprime2(self):
        sf = self.DoubleSpinBox_47.value()
        et = self.DoubleSpinBox_48.value()
        nu = self.DoubleSpinBox_49.value()
        dcap = self.DoubleSpinBox_50.value()
        tcap = self.DoubleSpinBox_51.value()
        t = self.DoubleSpinBox_52.value()
        b = self.DoubleSpinBox_53.value()
        phi = self.DoubleSpinBox_54.value()
        ans = str(funcs.fprime2(sf, et, nu, dcap, tcap, t, b, phi))
        self.textBrowser.setText(ans)


    def fi_2(self):
        sf = self.DoubleSpinBox_39.value()
        et = self.DoubleSpinBox_40.value()
        nu = self.DoubleSpinBox_41.value()
        dcap = self.DoubleSpinBox_42.value()
        tcap = self.DoubleSpinBox_43.value()
        t = self.DoubleSpinBox_44.value()
        b = self.DoubleSpinBox_46.value()
        ans = str(funcs.fi_2(sf, et, nu, dcap, tcap, t, b))

        self.textBrowser.setText(ans)


    def f2metalbelt(self):
        sf = self.DoubleSpinBox_31.value()
        et = self.DoubleSpinBox_34.value()
        nu = self.DoubleSpinBox_35.value()
        dcap = self.DoubleSpinBox_36.value()
        tcap = self.DoubleSpinBox_37.value()
        t = self.DoubleSpinBox_38.value()
        b = self.DoubleSpinBox_45.value()
        ans = str(funcs.f2metalbelt(sf, et, nu, dcap, tcap, t, b))

        self.textBrowser.setText(ans)



    def delltaf(self):
        capt = self.DoubleSpinBox_4.value()
        capd = self.fDoubleSpinBox_6.value() 
        ans = str(funcs.deltaf(capt, capd))
        self.textBrowser.setText(ans)
        

    def f1pa(self):
        sf = self.DoubleSpinBox_27.value()
        et = self.DoubleSpinBox_28.value()
        nu = self.DoubleSpinBox_29.value()
        dcap = self.DoubleSpinBox_30.value()
        t = self.DoubleSpinBox_32.value()
        b = self.DoubleSpinBox_33.value()

        ans = str(funcs.f1pa(sf, et, nu, dcap, t, b))
        self.textBrowser.setText(ans)


    def minibi(self):
        sf = self.DoubleSpinBox_19.value()
        et = self.DoubleSpinBox_20.value()
        nu = self.DoubleSpinBox_21.value()
        dcap = self.DoubleSpinBox_22.value()
        tcap = self.DoubleSpinBox_24.value()
        t = self.DoubleSpinBox_23.value()
        f = self.DoubleSpinBox_25.value()
        phi = self.DoubleSpinBox_26.value()
        

        ans = str(funcs.minibi(sf, et, nu, dcap, tcap, t,f,phi))
        self.textBrowser.setText(ans)


    def sfnp(self):
        np = self.DoubleSpinBox_17.value()
        ans = str(funcs.sfnp(np))
        self.textBrowser.setText(ans)

         
    def sfsy(self):
        sy = self.DoubleSpinBox_16.value()
        ans = str(funcs.sfsy(sy))
        self.textBrowser.setText(ans)


    def open_belt(self):
        cd = self.htext_6.value()
        c = self.htext_7.value()
        d = self.htext_8.value()

        pass
    def super_gear(self):
        # h = self.HdoubleSpinBox.valDdoubleSpinBox_10ue()

        # ans = funcs.spur_gear(h,n,d)
        # self.textBrowser.setText(ans)
        
        pass

    def open_belt(self):
        cd = self.DdoubleSpinBox_2.value()
        d = self.DdoubleSpinBox_4.value()
        c = self.DdoubleSpinBox_3.value()

        print(cd, d, c)
        ans= funcs.open_belt(cd,d,c)

        self.textBrowser.setText(ans)

    
    def crossed_belt(self):
        cd = self.DdoubleSpinBox_5.value()
        d = self.DdoubleSpinBox_7.value()
        c = self.DdoubleSpinBox_6.value()
        ans= funcs.open_belt(cd,d,c)
        self.textBrowser.setText(ans)




    def belt_speed(self):
        cd = self.DdoubleSpinBox_8.value()
        d = self.DdoubleSpinBox_9.value()
        bs= funcs.belt_speed(cd, d)
        ans = f"V = {bs}"
        self.textBrowser.setText(ans)

    def omg(self):
        y = self.DdoubleSpinBox_10.value()
        b = self.DdoubleSpinBox_11.value()
        t = self.DdoubleSpinBox_14.value()
        ans = funcs.omg(y, b, t)
        self.DdoubleSpinBox_12.setValue(ans)
        pass

    def f1a_fromf2(self):
        b = self.DoubleSpinBox_11.value()
        fa = self.fDoubleSpinBox_13.value()
        cv = self.fDoubleSpinBox_15.value()
        cp = self.fDoubleSpinBox_14.value()
        ans = funcs.f1a(b,fa,cv,cp)
        self.DoubleSpinBox_5.setValue(ans)
        pass

    
    def fc_belt_speed(self):
        d = self.DdoubleSpinBox_16.value()
        n = self.DdoubleSpinBox_15.value()
        ans = funcs.belt_speed(d, n)
        self.DdoubleSpinBox_13.setValue(ans)
        pass
    

    def fc_belt(self):
        # if self.checkBox.isChecked():
        #     print("ok")
        #     y = self.DdoubleSpinBox_10.value()
        #     b = self.DdoubleSpinBox_11.value()
        #     t = self.DdoubleSpinBox_14.value()
        #     ans = funcs.omg(y,b,t)

        #     self.DdoubleSpinBox_12.setValue(ans)

        #     ans = str(ans)
        #     self.textBrowser.setText(ans)
        # else:

        w = self.DdoubleSpinBox_12.value()
        v = self.DdoubleSpinBox_13.value()
        ans = funcs.fc_belt(w,v) 
        ans = str(ans)
        self.textBrowser.setText(ans)
        pass


    def expphi(self):
        phi = self.DoubleSpinBox.value()
        f = self.fDoubleSpinBox.value()
        ans = funcs.expphi(phi, f)
        ans = str(ans)
        self.textBrowser.setText(ans)


    def get_selected_row_data(self):
        selected_items = self.tableWidget.selectedItems()
        row = selected_items[0].row()
        data_org = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
        data = data_org[-1]
        data = float(data)

        self.fDoubleSpinBox.setValue(data)


    def get_selected_data(self):
        # TODO: dont let select Strings
        # TODO; user shouldnt can resize
        selected_items = self.tableWidget_2.selectedItems()
        #row = selected_items[0].row()
        #data_org = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
        #data = data_org[-1]

        selected_data = [item.text() for item in selected_items]
        value = selected_data[0]
        if is_float_value(value):
            self.fDoubleSpinBox_14.setValue(float(value))
        else:
            self.textBrowser.setText("INVALID ITEM YOU SELECT")


    def get_selected_data_f1a(self):
        selected_items = self.tableWidget_3.selectedItems()
        selected_data = [item.text() for item in selected_items]
        value = selected_data[0] 


        if is_float_value(value):
            self.fDoubleSpinBox_10.setValue(float(value))
        else:
            self.textBrowser.setText("INVALID ITEM YOU SELECT")
            
    
    def Torque_Belt(self):
        H_nom = self.DoubleSpinBox_2.value()
        n_d = self.fDoubleSpinBox_3.value()
        K_s = self.fDoubleSpinBox_2.value()
        n = self.fDoubleSpinBox_4.value()
        ans = funcs.TorqueBelt(H_nom,K_s,n_d,n)
        ans = str(ans)  
        self.textBrowser.setText(ans)
       

    def f1a_f2(self):
        T = self.DoubleSpinBox_3.value()
        d = self.fDoubleSpinBox_5.value()   
        ans = funcs.f1a_f2(T,d)
        ans = str(ans)
        self.textBrowser.setText(ans)
    
    def fi(self):
        t = self.DoubleSpinBox_6.value()
        d = self.fDoubleSpinBox_8.value() 
        f = self.DoubleSpinBox_7.value()
        phi = self.DoubleSpinBox_8.value()  
        ans = funcs.fi(t,d,f,phi)
        ans = str(ans)
        self.textBrowser.setText(ans)

    def fi2(self):
        fc =   self.DoubleSpinBox_13.value() 
        f2_p = self.fDoubleSpinBox_16.value()
        f1a_p = self.DoubleSpinBox_12.value()
        ans = funcs.fi2(fc,f2_p,f1a_p)
        ans = str(ans)
        self.textBrowser.setText(ans)

    def f2(self):
        f1a = self.DoubleSpinBox_5.value()
        f1a_f2 = self.fDoubleSpinBox_7.value()
        ans = funcs.f2(f1a,f1a_f2)  
        ans = str(ans)
        self.textBrowser.setText(ans)


    def f1a(self):
        b = self.DoubleSpinBox_9.value()
        fa = self.fDoubleSpinBox_9.value()
        cp = self.fDoubleSpinBox_10.value()
        cv = self.fDoubleSpinBox_11.value()
        ans = funcs.f1a(b,fa,cp,cv)
        ans = str(ans)
        self.textBrowser.setText(ans)


    def fprime(self):   
        phi = self.DoubleSpinBox_14.value()
        f1a_p = self.fDoubleSpinBox_17.value()
        f_2 = self.fDoubleSpinBox_18.value()
        fc = self.fDoubleSpinBox_19.value()
        ans = funcs.f_prime(phi,f1a_p,fc,f_2)
        ans = str(ans)
        self.textBrowser.setText(ans)


    def dip(self):   
        c = self.DoubleSpinBox_15.value()
        w = self.fDoubleSpinBox_20.value()
        fi_p = self.fDoubleSpinBox_21.value()
        ans = funcs.dip(c,w,fi_p)
        ans = str(ans)
        self.textBrowser.setText(ans)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
