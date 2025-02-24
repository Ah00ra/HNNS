from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import funcs


def is_float_value(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi('main.ui', self)


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

        if item.parent() is not None:
            parent = item.parent()
            parent_name = parent.text(0)
            ind = parent.indexOfChild(item)
            if parent_name == "Flat Metal Belt":
                if ind == 5:
                    self.pushButton_27.clicked.connect(self.f2metalbelt)
                    self.stackedWidget.setCurrentIndex(18)

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
