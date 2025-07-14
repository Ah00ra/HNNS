import re
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QDoubleSpinBox, QComboBox,QHeaderView
from PyQt5.QtGui import QDoubleValidator
from PyQt5.uic import loadUi
import funcs
from PyQt5.QtWidgets import QApplication, QStyleFactory
import reoureces_rc

#from qt_material import apply_stylesheet

history = []
print(QStyleFactory.keys())

def is_float_value(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_standard_speed(v):
    v = float(v)
    standard_speed_vbelt = [1000,2000,3000,4000,5000]
    if v in standard_speed_vbelt:
        return True
    return False

def is_htab_error_message(htab):
    htab = str(htab)
    if re.search(r"\bError\b", htab):
        return True
        
def is_numeric_string(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_standard_sheave_d(selected_type, sheave_d):
    sheave_d = float(sheave_d)
    standard_sheave_d_vbelt_A = [2.6, 3, 3.4, 3.8, 4.2, 4.6, 5]
    standard_sheave_d_vbelt_B = [4.2, 4.6, 5, 5.4, 5.8, 6.2, 6.6, 7]
    standard_sheave_d_vbelt_C = [6, 7, 8, 9, 10, 11, 12]
    standard_sheave_d_vbelt_D = [10, 11, 12, 13, 14, 15, 16, 17]
    standard_sheave_d_vbelt_E = [16, 18 ,20, 22, 24, 26, 28]

    if selected_type == "A":
        if sheave_d in standard_sheave_d_vbelt_A:
            return True
        return False
    elif selected_type == "B":
        if sheave_d in standard_sheave_d_vbelt_B:
            return True
        return False
    elif selected_type == "C":
        if sheave_d in standard_sheave_d_vbelt_C:
            return True
        return False
    elif selected_type == "D":
        if sheave_d in standard_sheave_d_vbelt_D:
            return True
        return False
    elif selected_type == "E":
        if sheave_d in standard_sheave_d_vbelt_E:
            return True
        return False



class CustomDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self, value):
        if value == 0:
            return "0"
        else:
            return f"{value:.3f}".rstrip('0').rstrip('.')

class FloatOnlyComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)  # Prevent adding invalid entries

        self.validator = QDoubleValidator()
        self.validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit().setValidator(self.validator)

        # Regular expression to match valid float inputs (including partial)
        self.float_regex = re.compile(r'^-?(\d+)?(\.\d*)?$')

        self.lineEdit().textEdited.connect(self.on_text_edited)

    def on_text_edited(self, text):
        # Allow empty string (user clearing input)
        if text == '':
            return

        # Check if text matches float regex (allows partial input)
        if self.float_regex.match(text):
            # Further check with validator for stricter validation
            state, _, _ = self.validator.validate(text, 0)
            if state == self.validator.Invalid:
                # Invalid float input, revert to previous valid text
                self.lineEdit().undo()
        else:
            # Not matching float pattern, revert
            self.lineEdit().undo()

class Wire_Rope_Tables(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('wire_rope_tables.ui', self)
        self.tabWidget.setTabText(0, "ft")
        self.tabWidget.setTabText(1, "nf")
        self.tabWidget.setTabText(2, "fb")
        self.tabWidget.setTabText(3, "ff")
       
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

class Ha_Table(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ha_table.ui', self)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi('main.ui', self)
        self.txtbrowser = self.textBrowser
        
        # roller chain table
        self.tableWidget_4.setColumnWidth(0, 200)
        self.tableWidget_4.setColumnWidth(1, 200)
        self.tableWidget_4.setColumnWidth(2, 150)
        self.tableWidget_4.setColumnWidth(3, 150)

        self.stackedWidget.setCurrentIndex(0)

        # self.tableWidget.setHidden(True) 
        # self.pushButton_10.setHidden(True)

        # self.tableWidget_3.setHidden(True)
        # self.pushButton_21.setHidden(True)
        # set hidden F2 form layout_9
        # self.tableWidget_2.setHidden(True)
        # self.pushButton_11.setHidden(True)
        # self.DoubleSpinBox_11.setHidden(True)
        # self.fDoubleSpinBox_13.setHidden(True)
        # self.checkBox_14.setHidden(True)
        # self.checkBox_15.setHidden(True)
        # self.fDoubleSpinBox_14.setHidden(True)
        # self.fDoubleSpinBox_15.setHidden(True)
        # self.pushButton_16.setHidden(True)

        # self.htext_44.setHidden(True)
        # self.htext_45.setHidden(True)
        # self.htext_46.setHidden(True)
        # self.htext_47.setHidden(True)
        
        # fc belt
        self.DoubleSpinBox_87.setHidden(True)
        self.fDoubleSpinBox_29.setHidden(True)
        self.fDoubleSpinBox_30.setHidden(True)
        self.DoubleSpinBox_88.setHidden(True)
        self.DoubleSpinBox_89.setHidden(True)
        self.pushButton_7.setHidden(True)
        self.pushButton_8.setHidden(True)
        self.htext_132.setHidden(True)
        self.htext_133.setHidden(True)
        self.htext_134.setHidden(True)
        self.htext_135.setHidden(True)
        self.htext_136.setHidden(True)

        # wire_rope Ft
        #self.widget.setHidden(True)
        #self.htext_152.setHidden(True)
        self.htext_153.setHidden(True)
        self.htext_154.setHidden(True)
        self.htext_154.setHidden(True)
        self.htext_155.setHidden(True)
        self.htext_156.setHidden(True)
        self.htext_157.setHidden(True)
        self.htext_158.setHidden(True)
        self.htext_159.setHidden(True)
        self.htext_160.setHidden(True)
        self.htext_161.setHidden(True)


        #self.DoubleSpinBox_152.setHidden(True)

        self.DoubleSpinBox_153.setHidden(True)
        self.DoubleSpinBox_154.setHidden(True)
        self.DoubleSpinBox_155.setHidden(True)
        self.DoubleSpinBox_156.setHidden(True)
        self.DoubleSpinBox_157.setHidden(True)
        self.DoubleSpinBox_158.setHidden(True)
        self.DoubleSpinBox_159.setHidden(True)
        self.DoubleSpinBox_160.setHidden(True)
        self.DoubleSpinBox_161.setHidden(True)
        # nfs_...

        self.tableWidget_10.setHidden(True)
        self.pushButton_53.setHidden(True)

        self.comboBox_5.setHidden(True)
        self.comboBox_6.setHidden(True)
        self.comboBox_7.setHidden(True)
        self.comboBox_8.setHidden(True)

        self.comboBox_11.setHidden(True)
        self.comboBox_12.setHidden(True)
        self.comboBox_13.setHidden(True)
        self.comboBox_14.setHidden(True)


        self.comboBox_10.setEditable(True)
        self.comboBox_10.lineEdit().setPlaceholderText("Select or Insert Sheave Pitch Diameter(in)")
        self.comboBox_10.setCurrentIndex(-1)

        self.comboBox_11.setEditable(True)
        self.comboBox_11.lineEdit().setPlaceholderText("Select or Insert Sheave Pitch Diameter(in)")
        self.comboBox_11.setCurrentIndex(-1)

        self.comboBox_12.setEditable(True)
        self.comboBox_12.lineEdit().setPlaceholderText("Select or Insert Sheave Pitch Diameter(in)")
        self.comboBox_12.setCurrentIndex(-1)

        self.comboBox_13.setEditable(True)
        self.comboBox_13.lineEdit().setPlaceholderText("Select or Insert Sheave Pitch Diameter(in)")
        self.comboBox_13.setCurrentIndex(-1)

        self.comboBox_14.setEditable(True)
        self.comboBox_14.lineEdit().setPlaceholderText("Select or Insert Sheave Pitch Diameter(in)")
        self.comboBox_14.setCurrentIndex(-1)


        self.comboBox_16.setEditable(True)
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.comboBox_16.lineEdit().setPlaceholderText("Select or Insert Speed")
        self.comboBox_16.setCurrentIndex(-1)
        self.comboBox_16.lineEdit().setValidator(validator)


        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.treeWidget.itemClicked['QTreeWidgetItem*','int'].connect(self.item_clicked)

        self.textBrowser.textChanged.connect(self.append_text_to_history)
        self.textBrowser.textChanged.connect(self.write_history_to_table)
        # for btn in self.findChildren(QPushButton):
        #     btn.clicked.connect(self.write_history_to_table)



        # wire rope
        self.comboBox_3.currentIndexChanged.connect(self.number_of_d)
        self.pushButton_2.clicked.connect(self.clear_table_and_history)

        # dynamic combo for LP vbelt
        self.comboBox_2.currentIndexChanged.connect(self.dynamic_combo_lp)
        # dynamic combo for HA vbelt
        self.comboBox_9.currentIndexChanged.connect(self.dynamic_combo_ha_vbelt)
    

    def clear_table_and_history(self):
        history.clear()
        self.tableWidget_6.clearContents()
        pass
        
    def write_history_to_table(self):
        # rows = self.tableWidget_6.rowCount()
        # columns = self.tableWidget_6.columnCount()
        # sender = self.sender(o)
        for row, item in enumerate(history):
            self.tableWidget_6.setItem(row, 0, QTableWidgetItem(item[0]))

            self.tableWidget_6.setItem(row, 1, QTableWidgetItem(item[1]))


    def append_text_to_history(self):
        def split_text(text):
            name_expl, value = text.split("=")
    
            name = name_expl.split(";")[0]
            return name, value
            

        text = self.textBrowser.toPlainText()
        print("LOG: ",text) 
        if not re.search(r"\bError\b", text):
            name, value= split_text(text)

            # formula_name_unit = split_text[0]
            # value = str(split_text[1])
           
            if is_numeric_string(value):
                value = str(round(float(value), 3))  

            item_to_add = [name, value]

            if len(history) == 0:
                history.append(item_to_add)
            elif history[-1][1] != value:
                print(history[-1])
                if len(history) == 20:
                    history.pop(0)
                history.append(item_to_add)
                            

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
            # self.pushButton_16.clicked.connect(self.f1a_fromf2)
            # self.pushButton_11.clicked.connect(self.get_selected_data)
            self.stackedWidget.setCurrentIndex(10)

        
        if item.text(column) == "F1a":
            self.pushButton_14.clicked.connect(self.f1a)
            self.pushButton_21.clicked.connect(self.get_selected_data_f1a)
            self.stackedWidget.setCurrentIndex(11)

        if item.text(column) == "f'":
            self.pushButton_18.clicked.connect(self.fprime)
            self.stackedWidget.setCurrentIndex(12)

        if item.text(column) == "dip":
            self.pushButton_20.clicked.connect(self.cal_dip)
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

        if item.text(column) == "Hp(link-plate limited)":
            self.pushButton_30.clicked.connect(self.hp_link_plate)
            self.stackedWidget.setCurrentIndex(21)

        if item.text(column) == "Hp(Roller Limited)":
            self.pushButton_58.clicked.connect(self.hp_roller_limited)
            self.stackedWidget.setCurrentIndex(41)

        if item.text(column) == "C":
            self.pushButton_31.clicked.connect(self.center_distance)
            self.stackedWidget.setCurrentIndex(22)    

        if item.text(column) == "L/p:No. Pitches":
            self.pushButton_32.clicked.connect(self.np_rc)
            self.stackedWidget.setCurrentIndex(23)

        if item.text(column) == "Ha":

            self.pushButton_34.clicked.connect(self.ha_roller_chain)
            self.pushButton_34.clicked.connect(self.open_ha_table)
            self.stackedWidget.setCurrentIndex(24)

        if item.text(column) == "Max Rotational Speed":
            self.pushButton_158.clicked.connect(self.max_rotational_speed)
            self.stackedWidget.setCurrentIndex(42)

        if item.text(column) == "Ft":
            self.stackedWidget.setCurrentIndex(25)
            self.pushButton_35.clicked.connect(self.open_wire_rope_tables)
            self.pushButton_35.clicked.connect(self.wire_rope)
        
        if item.text(column) == "Length of Pitch":
            self.stackedWidget.setCurrentIndex(26)
            self.pushButton_36.clicked.connect(self.lengh_pitch_vbelt)
            self.pushButton_37.clicked.connect(self.combo_lengh_pitch_vbelt)

        if item.text(column) == "Center Distance":
            self.stackedWidget.setCurrentIndex(27)
            self.pushButton_38.clicked.connect(self.cente_distance_vbelt)

        if item.text(column) == "Hp allowable":
            self.pushButton_40.clicked.connect(self.cal_ha_vbelt)
            self.pushButton_39.clicked.connect(self.get_selected_data_ha_vbelt)
            self.stackedWidget.setCurrentIndex(28)

        if item.text(column) == "Hp design":
            self.pushButton_41.clicked.connect(self.hd_vbelt_load)
            self.stackedWidget.setCurrentIndex(29)

        if item.text(column) == "MIN Number of Belt":
            self.pushButton_43.clicked.connect(self.nb_vbelt_load)
            self.stackedWidget.setCurrentIndex(30)

        if item.text(column) == "'Fc' Centrifugal Tension":
            self.pushButton_45.clicked.connect(self.get_selected_data_fc_tension)
            self.pushButton_44.clicked.connect(self.fc_vbelt_load)
            self.stackedWidget.setCurrentIndex(31)

        if item.text(column) == "ΔF":
            self.pushButton_46.clicked.connect(self.deltaf_vebelt_load)
            self.stackedWidget.setCurrentIndex(32)

        if item.text(column) == "Exp(fΦ)":
            self.pushButton_214.clicked.connect(self.expphi_vbelt)
            self.stackedWidget.setCurrentIndex(43)

        if item.text(column) == "'F1' Largest Tension ":
            self.pushButton_47.clicked.connect(self.f1_vebelt_load)
            self.stackedWidget.setCurrentIndex(33)

        if item.text(column) == "'F2' Least Tension ":
            self.pushButton_48.clicked.connect(self.f2_vbelt_load)
            self.stackedWidget.setCurrentIndex(34)

        if item.text(column) == "'Fi' initial Tension":
            self.pushButton_49.clicked.connect(self.fi_vbelt_load)
            self.stackedWidget.setCurrentIndex(35)

        if item.text(column) == "η_fs":
            self.pushButton_51.clicked.connect(self.nfs_vbelt_load)
            self.stackedWidget.setCurrentIndex(36)

        if item.text(column) == "Fb1, Fb2":
            self.pushButton_52.clicked.connect(self.fb12_vbelt_load)
            self.pushButton_53.clicked.connect(self.get_selected_data_fb1fb2)
            self.stackedWidget.setCurrentIndex(37)

        if item.text(column) == "T1, T2":
            self.pushButton_54.clicked.connect(self.t12_vbelt_load)
            self.stackedWidget.setCurrentIndex(38)

        if item.text(column) == "'Np' Number of Passes":
            self.pushButton_55.clicked.connect(self.np_vbelt_load)
            self.pushButton_57.clicked.connect(self.get_selected_data_np_vbelt)
            self.stackedWidget.setCurrentIndex(39)    

        if item.text(column) == "'t' Lifetime ":
            self.pushButton_56.clicked.connect(self.t_vbelt_load)
            self.stackedWidget.setCurrentIndex(40)

        if item.parent() is not None:
            parent = item.parent()
            parent_name = parent.text(0)
            ind = parent.indexOfChild(item)
            if parent_name == "Flat Metal Belt":
                if ind == 5:
                    self.pushButton_27.clicked.connect(self.cal_f2metalbelt)
                    self.stackedWidget.setCurrentIndex(18)
                if ind == 6:
                    self.pushButton_28.clicked.connect(self.fi_2)
                    self.stackedWidget.setCurrentIndex(19)

                if ind == 7:
                    self.pushButton_29.clicked.connect(self.fprime2)
                    self.stackedWidget.setCurrentIndex(20)


    def open_ha_table(self):
        self.ha_win = Ha_Table()
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

        row_count = self.ha_win.tableWidget_4.rowCount()
        col_count = self.ha_win.tableWidget_4.columnCount() 

        for i in range(row_count): 
            item = QTableWidgetItem(ans[i])  
            item.setTextAlignment(Qt.AlignCenter)

            item1 = QTableWidgetItem(chain[i]) 
            item1.setTextAlignment(Qt.AlignCenter)

            item2 = QTableWidgetItem(types[i]) 
            item2.setTextAlignment(Qt.AlignCenter)

            ind = i

            self.ha_win.tableWidget_4.setItem(ind,1, item)
            self.ha_win.tableWidget_4.setItem(ind,2, item1)
            self.ha_win.tableWidget_4.setItem(ind,3, item2)

        self.ha_win.show()


    def open_wire_rope_tables(self):
            self.wire_window = Wire_Rope_Tables()
            # Show the second window

            #row_position = self.wire_window.tableWidget.rowCount()
            row_position = 1
            col_position = 1
            no_d = int(self.comboBox_3.currentText())
            col_c = 10# int(self.comboBox_2.currentText())

            d_values = [] 
            for i in range(no_d):
                ind = 152+i
                d_values.append(getattr(self, f'DoubleSpinBox_{ind}').value())
            
            #just create 
            for i in range(no_d-1):
                self.wire_window.tableWidget.insertRow(row_position)
                self.wire_window.tableWidget_2.insertRow(row_position)
                self.wire_window.tableWidget_3.insertRow(row_position)
                self.wire_window.tableWidget_4.insertRow(row_position)
                row_position += 1


            # ff and fb
            self.wire_window.tableWidget_3.insertColumn(1)
            self.wire_window.tableWidget_4.insertColumn(1)
###########
            self.wire_window.tableWidget_3.setHorizontalHeaderItem(1, QTableWidgetItem(f"RESULT"))
            self.wire_window.tableWidget_4.setHorizontalHeaderItem(1, QTableWidgetItem(f"RESULT"))

            if col_c != 1:
                for i in range(col_c):
                    self.wire_window.tableWidget.insertColumn(col_position)
                    self.wire_window.tableWidget.setHorizontalHeaderItem(col_position, QTableWidgetItem(f"m = {i+1}"))

                    self.wire_window.tableWidget_2.insertColumn(col_position)
                    self.wire_window.tableWidget_2.setHorizontalHeaderItem(col_position, QTableWidgetItem(f"m = {i+1}"))
                    col_position += 1



            wcap = self.DoubleSpinBox_75.value()
            w = self.DoubleSpinBox_77.value()
            lcap = self.DoubleSpinBox_78.value()
            a = self.DoubleSpinBox_79.value()
            psu = self.DoubleSpinBox_80.value()
            su = self.DoubleSpinBox_82.value()
            dcap = self.DoubleSpinBox_81.value()
            er = self.DoubleSpinBox_83.value()
            dw = self.DoubleSpinBox_84.value()
            am = self.DoubleSpinBox_85.value()
            no_d = self.comboBox_3.currentText()
            #m = self.comboBox_2.currentText()
            
            table_of_ans_ft = funcs.f_t_wire_rope(cap_w=wcap, w=w, l=lcap, a=a, d=d_values)

            table_of_ans_nf = funcs.nf_wire_rope(cap_w=wcap, w=w, l=lcap,
                                                a=a, ps=psu, d=d_values, 
                                                cap_d=dcap, 
                                                er=er, dw=dw, am=am, su=su)
            table_of_ans_fb = funcs.f_b_wire_rope(er=er, dw=dw, am=am, cap_d=dcap, d=d_values)
            table_of_ans_ff = funcs.f_f_wire_rope(ps=psu, s=su,cap_d=dcap, d=d_values)

            # write
            for i in range(int(no_d)):
                self.wire_window.tableWidget.setItem(i, 0, QTableWidgetItem(f"{d_values[i]}"))
                self.wire_window.tableWidget_2.setItem(i, 0, QTableWidgetItem(f"{d_values[i]}"))
                self.wire_window.tableWidget_3.setItem(i, 0, QTableWidgetItem(f"{d_values[i]}"))
                self.wire_window.tableWidget_4.setItem(i, 0, QTableWidgetItem(f"{d_values[i]}"))
                # col for ff fb
                self.wire_window.tableWidget_3.setItem(i, 1, QTableWidgetItem(f"{table_of_ans_fb[i]}"))
                self.wire_window.tableWidget_4.setItem(i, 1, QTableWidgetItem(f"{table_of_ans_ff[i]}"))

                for j in range(0, 10):
                    self.wire_window.tableWidget.setItem(i, j+1, QTableWidgetItem(f"{table_of_ans_ft[i][j]}"))
                    self.wire_window.tableWidget_2.setItem(i, j+1, QTableWidgetItem(f"{table_of_ans_nf[i][j]}"))
                    #print(table_of_ans[i][j])


            ##self.textBrowser.setText(str(table_of_ans_ft))



            #:self.wire_window.textBrowser.append(f"{r},{c}")

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
        no_d = self.comboBox_3.currentText()
        #m = self.comboBox_2.currentText()

        d_values = []
        for i in range(int(no_d)):
                ind = 152+i
                d_values.append(getattr(self, f'DoubleSpinBox_{ind}').value())

        #ans = wcap, w,lcap, a, psu, dcap, er, dw, am, m, no_d, d_values
        ans = funcs.f_t_wire_rope(cap_w=wcap, w=w, l=lcap, a=a, d=d_values)
        ###ans = str(ans)
        ###self.textBrowser.setText(ans)


    def number_of_d(self):
        d = int(self.comboBox_3.currentText())
        for i in range(10):
            ind = 152+i
            getattr(self, f'htext_{ind}').hide()
            getattr(self, f'DoubleSpinBox_{ind}').hide()

        for i in range(d):
            ind = 152+i
            getattr(self, f'htext_{ind}').show()
            getattr(self, f'DoubleSpinBox_{ind}').show()



        
        
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

    def max_rotational_speed(self):
        p = self.DoubleSpinBox_436.value()
        n = self.DoubleSpinBox_437.value()
        f = self.DoubleSpinBox_438.value()
        ans = str(funcs.max_rotational_speed(p , n, f))
        fans = f"L RollerChain;Length of the chain = {ans}"
        self.textBrowser.setText(fans)
        
    def np_rc(self):
        n1 = self.DoubleSpinBox_62.value()
        n2 = self.DoubleSpinBox_63.value()
        p = self.DoubleSpinBox_64.value()
        c = self.DoubleSpinBox_65.value()
        ans = str(funcs.np_rc(n1, n2, p, c))
        fans = f"L RollerChain;Length of the chain = {ans}"
        self.textBrowser.setText(fans)

    def center_distance(self):
        n1 = self.DoubleSpinBox_58.value()
        n2 = self.DoubleSpinBox_59.value()
        p = self.DoubleSpinBox_60.value()
        L = self.DoubleSpinBox_61.value()
        ans = str(funcs.center_distance(n1, n2, p, L))
        fans = f"C RollerChain(in); center-to-center distance Sprocket RollerChain = {ans}"
        self.textBrowser.setText(fans)

    def hp_link_plate(self):
        N = self.DoubleSpinBox_55.value()
        n = self.DoubleSpinBox_56.value()
        p = self.DoubleSpinBox_57.value()
        ans = str(funcs.hp_link_plate(N, n, p),)
        fans = f"Hp1; Maximum Power transmission capacity of  chain,\
        limited by the strength of the link plates = {ans}"
        self.textBrowser.setText(fans)

    def hp_roller_limited(self):
        chain_number = self.comboBox_17.currentText()
        cn = self.DoubleSpinBox_138.value()
        n = self.DoubleSpinBox_139.value()
        p = self.DoubleSpinBox_140.value()
        ans = str(funcs.hp_roller_limited(chain_number ,cn, n, p))
        fans = f"Hp1 RollerChain(Hp); Maximum Power transmission capacity of chain,\
        limited by the strength of the Rollers = {ans}"
        self.textBrowser.setText(fans)

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
        fans = f"f' Metalbelt; Effective coefficient of friction between the belt and the pulley = {ans}"
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
        fans = f"Fi Metalbelt(Ibf); Tension in the slack side of the MetalBelt = {ans}"
        self.textBrowser.setText(fans)


    def cal_f2metalbelt(self):
        sf = self.DoubleSpinBox_31.value()
        et = self.DoubleSpinBox_34.value()
        nu = self.DoubleSpinBox_35.value()
        dcap = self.DoubleSpinBox_36.value()
        tcap = self.DoubleSpinBox_37.value()
        t = self.DoubleSpinBox_38.value()
        b = self.DoubleSpinBox_45.value()
        ans = funcs.f2metalbelt(sf, et, nu, dcap, tcap, t, b)
        fans = f"F2 Metalbelt(Ibf); Tension in the slack side of the MetalBelt = {ans}"
        self.textBrowser.setText(fans)



    def delltaf(self):
        capt = self.DoubleSpinBox_4.value()
        capd = self.fDoubleSpinBox_6.value() 
        ans = str(funcs.deltaf(capt, capd))
        fans = f"ΔF Belt (Ibf)= {ans}"
        self.textBrowser.setText(fans)
        

    def f1pa(self):
        sf = self.DoubleSpinBox_27.value()
        e = self.DoubleSpinBox_28.value()
        nu = self.DoubleSpinBox_29.value()
        dcap = self.DoubleSpinBox_30.value()
        t = self.DoubleSpinBox_32.value()
        b = self.DoubleSpinBox_33.value()
        ans = str(funcs.f1pa(sf, e, nu, dcap, t, b))
        fans = f"(f1)a MetalBelt(Ibf); Allowable tension  = {ans} "
        self.textBrowser.setText(fans)


    def minibi(self):
        sf = self.DoubleSpinBox_19.value()
        e = self.DoubleSpinBox_20.value()
        nu = self.DoubleSpinBox_21.value()
        dcap = self.DoubleSpinBox_22.value()
        tcap = self.DoubleSpinBox_24.value()
        t = self.DoubleSpinBox_23.value()
        f = self.DoubleSpinBox_25.value()
        phi = self.DoubleSpinBox_26.value()
        ans = funcs.minibi(sf, e, nu, dcap, tcap, t,f,phi)
        fans = f"Min b MetalBelt(in); Minimum  Belt Thicknes = {ans} "
        self.textBrowser.setText(ans)


    def sfnp(self):
        np = self.DoubleSpinBox_17.value()
        ans = str(funcs.sfnp(np))
        fans = f"Sf MetalBelt(psi); Endurance Strength = {ans}"
        self.textBrowser.setText(fans)

         
    def sfsy(self):
        sy = self.DoubleSpinBox_16.value()
        ans = str(funcs.sfsy(sy))
        fans = f"Sf MetalBelt(psi); Endurance Strength = {ans}"
        self.textBrowser.setText(fans)


    # def open_belt(self):
    #     cd = self.htext_6.value()
    #     c = self.htext_7.value()
    #     d = self.htext_8.value()

    #     pass
    # def super_gear(self):
    #     # h = self.HdoubleSpinBox.valDdoubleSpinBox_10ue()

    #     # ans = funcs.spur_gear(h,n,d)
    #     # self.textBrowser.setText(ans)
        
        pass

    def open_belt(self):
        cd = self.DoubleSpinBox_18.value()
        d = self.fDoubleSpinBox_22.value()
        c = self.fDoubleSpinBox_23.value()
        ans= funcs.open_belt(cd,d,c)
        self.textBrowser.setText(ans)

    
    def crossed_belt(self):
        cd = self.DoubleSpinBox_76.value()
        d = self.fDoubleSpinBox_24.value()
        c = self.fDoubleSpinBox_25.value()
        ans = funcs.crossed_belt(cd,d,c)
        ans = str(ans)
        self.textBrowser.setText(ans)




    def belt_speed(self):
        cd = self.fDoubleSpinBox_26.value()
        d = self.fDoubleSpinBox_27.value()
        bs= funcs.belt_speed(cd, d)
        ans = f"Speed Belt (ft/min)= {bs}"
        self.textBrowser.setText(ans)

    def omg(self):
        y = self.DoubleSpinBox_87.value()
        b = self.DoubleSpinBox_88.value()
        t = self.fDoubleSpinBox_29.value()
        ans = funcs.omg(y, b, t)
        self.DoubleSpinBox_86.setValue(ans)
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
        d = self.fDoubleSpinBox_30.value()
        n = self.DoubleSpinBox_89.value()
        ans = funcs.belt_speed(d, n)
        self.fDoubleSpinBox_28.setValue(ans)
        pass
    

    def fc_belt(self):
        w = self.DoubleSpinBox_86.value()
        v = self.fDoubleSpinBox_28.value()
        ans = funcs.fc_belt(w,v) 
        fans = f"Fc belt(Ibf); hoop Tension due to Centrifugal Force = {ans}"
        self.textBrowser.setText(fans)
        pass


    def expphi(self):
        phi = self.DoubleSpinBox.value()
        f = self.fDoubleSpinBox.value()
        ans = funcs.expphi(phi, f)
        ans = str(ans)
        fans = f"Expo(fΦ) Belt = {ans}"
        self.textBrowser.setText(fans)


    def get_selected_row_data(self):
        selected_items = self.tableWidget.selectedItems()
        if len(selected_items) != 0:
            row = selected_items[0].row()
            data_org = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
            data = data_org[-1]
            data = float(data)

            self.fDoubleSpinBox.setValue(data)

    def get_selected_data_fc_tension(self):
        selected_items = self.tableWidget_8.selectedItems()
        if len(selected_items) != 0:
            row = selected_items[0].row()
            value = self.tableWidget_8.item(row, 1).text()
            value = float(value)
            self.DoubleSpinBox_106.setValue(value)


    def get_selected_data_ha_vbelt(self):
        selected_items = self.tableWidget_5.selectedItems()
        if len(selected_items) != 0:
            row = selected_items[0].row()
            column = selected_items[0].column()
            if row == 0 and column ==5 or (row == 7 and column == 1):
                pass
            else:
                items = [0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.20]
                k2 = items[row]
                self.DoubleSpinBox_97.setValue(k2)

    def get_selected_data_fb1fb2 (self):
        selected_items = self.tableWidget_10.selectedItems()
        if len(selected_items) != 0 :
            col = selected_items[0].column()
            row = selected_items[0].row()
            data= self.tableWidget_10.item(row, col)
            value = data.text()
            if is_numeric_string(value):
                self.DoubleSpinBox_124.setValue(float(value))

    def get_selected_data_np_vbelt(self):
        selected_items = self.tableWidget_11.selectedItems()
        if len(selected_items) != 0:
            col = selected_items[0].column()
            row = selected_items[0].row()

            data= self.tableWidget_11.item(row, col)
            if col == 1 or col == 3:
                k = data.text()
                k = float(k)
                self.DoubleSpinBox_130.setValue(k)
            if col == 2 or col == 4:
                b = data.text()
                b = float(b)
                self.DoubleSpinBox_131.setValue(b)
        


    def get_selected_data(self):
        selected_items = self.tableWidget_2.selectedItems()
        #row = selected_items[0].row()
        #data_org = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
        #data = data_org[-1]

        selected_data = [item.text() for item in selected_items]
        value = selected_data[0]
        if is_float_value(value):
            self.fDoubleSpinBox_14.setValue(float(value))
        else:
            self.textBrowser.setText("Error: INVALID ITEM YOU SELECT")


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
        fans = f"Torque Belt(Hp); Necessary Torque = {ans}"  
        self.textBrowser.setText(fans)
       
    def f1a_f2(self):
        T = self.DoubleSpinBox_3.value()
        d = self.fDoubleSpinBox_5.value()   
        ans = funcs.f1a_f2(T,d)
        ans = str(ans)
        fans = f"(F1)a - F2 Belt = {ans}"
        self.textBrowser.setText(fans)


    
    def fi(self):
        t = self.DoubleSpinBox_6.value()
        d = self.fDoubleSpinBox_8.value() 
        f = self.DoubleSpinBox_7.value()
        phi = self.DoubleSpinBox_8.value()  
        ans = funcs.fi(t,d,f,phi)
        ans = str(ans)
        fans = f"Fi Belt(Ibf); Initial Tension in the belt = {ans}"
        self.textBrowser.setText(fans)

    def fi2(self):
        fc =   self.DoubleSpinBox_13.value() 
        f2_p = self.fDoubleSpinBox_16.value()
        f1a_p = self.DoubleSpinBox_12.value()
        ans = funcs.fi2(fc,f2_p,f1a_p)
        ans = str(ans)
        fans = f"Fi Belt(Ibf); Initial Tension in the belt = {ans}"
        self.textBrowser.setText(fans)

    def f2(self):
        f1a = self.DoubleSpinBox_5.value()
        f1a_f2 = self.fDoubleSpinBox_7.value()
        ans = funcs.f2(f1a,f1a_f2)  
        ans = str(ans)
        fans = f"F2 Belt(Ibf); Tension in the slack side of the belt = {ans}"
        self.textBrowser.setText(fans)


    def f1a(self):
        b = self.DoubleSpinBox_9.value()
        fa = self.fDoubleSpinBox_9.value()
        cp = self.fDoubleSpinBox_10.value()
        cv = self.fDoubleSpinBox_11.value()
        ans = funcs.f1a(b,fa,cp,cv)
        ans = str(ans)
        fans = f"(F1)a Belt(Ibf); allowable largest tension = {ans}"
        self.textBrowser.setText(fans)



    def fprime(self):   
        phi = self.DoubleSpinBox_14.value()
        f1a_p = self.fDoubleSpinBox_17.value()
        f_2 = self.fDoubleSpinBox_18.value()
        fc = self.fDoubleSpinBox_19.value()
        ans = funcs.f_prime(phi,f1a_p,fc,f_2)
        ans = str(ans)
        fans = f"f' Belt; Effective coefficient of friction between the belt and the pulley. = {ans}"
        self.textBrowser.setText(fans)


    def cal_dip(self):   
        c = self.DoubleSpinBox_15.value()
        w = self.fDoubleSpinBox_20.value()
        fi_p = self.fDoubleSpinBox_21.value()
        ans = funcs.dip(c,w,fi_p)
        fans = f"Dip Belt(in); vertical sag or deflection of the belt between the pulleys\
        due to the belt's own weight and tension = {ans}"
        self.textBrowser.setText(fans)


    def lengh_pitch_vbelt(self):
        c = self.DoubleSpinBox_90.value()
        capd = self.DoubleSpinBox_91.value()
        d = self.DoubleSpinBox_92.value()
        ans = funcs.lengh_pitch_vbelt(c, capd, d)
        fans = f"Lp vBelt(in); Lengh of pitch = {ans}"
        self.textBrowser.setText(fans)

    def combo_lengh_pitch_vbelt(self):
        selected_type = self.comboBox_2.currentText()
        if selected_type == "A":
            value = self.comboBox_4.currentText()
            value = int(value)
            ans = 1.3 + value
            fans = f"Lp vBelt(in); Lengh of pitch (A{value}) = {ans}"
            self.textBrowser.setText(fans)
        elif selected_type == "B":
            value = self.comboBox_5 .currentText()
            value = int(value)
            ans = 1.8 + value
            fans = f"Lp vBelt(in); Lengh of pitch (B{value}) = {ans}"
            self.textBrowser.setText(fans)
        elif selected_type == "C":
            value = self.comboBox_6 .currentText()
            value = int(value)
            ans = 2.9 + value
            fans = f"Lp vBelt(in); Lengh of pitch (C{value}) = {ans}"
            self.textBrowser.setText(fans)
        elif selected_type == "D":
            value = self.comboBox_7 .currentText()
            value = int(value)
            ans = 3.3 + value
            fans = f"Lp vBelt(in); Lengh of pitch (D{value}) = {ans}"
            self.textBrowser.setText(fans)
        elif selected_type == "E":
            value = self.comboBox_8.currentText()
            value = int(value)
            ans = 4.5 + value
            fans = f"Lp vBelt(in); Lengh of pitch (E{value}) = {ans}"
            self.textBrowser.setText(fans)

    
    

    def cal_ha_vbelt(self):
        theta = self.DoubleSpinBox_96.value()
        
        k_selected_type = self.comboBox_15.currentText()
        k1 = funcs.k1_vbelt(theta, k_selected_type)
        if not is_numeric_string(k1):
            print("NOT OK")
            self.textBrowser.setText(k1)
        
        
        else:
            k2 = self.DoubleSpinBox_97.value()
            speed = self.comboBox_16.currentText()
            if not is_numeric_string(speed):
                speed = 0
            selected_type = self.comboBox_9.currentText()
            
            if selected_type == "A":
                sheave_d = self.comboBox_10.currentText()
                if not is_numeric_string(sheave_d):
                    sheave_d = 0
                if is_standard_speed(speed) and is_standard_sheave_d(selected_type,sheave_d):
                    htab = funcs.h_table_vbelt(speed, sheave_d, "A")
                    ans = funcs.ha_vbelt(k1, k2, htab)
                    fans = f"A = {ans}"
                    self.textBrowser.setText(fans)
                    
                elif not is_standard_speed(speed) and is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_speed(speed, sheave_d, selected_type)
                    print("------------")
                    print(htab)
                    print("------------")
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"A(bad v) = {ans}"
                        self.textBrowser.setText(fans)

                elif is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"A(bad sheave_d) = {ans}"
                        self.textBrowser.setText(fans)

                elif not is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley_and_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"A(both_bad) = {ans}"
                        self.textBrowser.setText(fans)


            elif selected_type == "B":
                sheave_d = self.comboBox_11.currentText()
                if not is_numeric_string(sheave_d):
                    sheave_d = 0

                if is_standard_speed(speed) and is_standard_sheave_d(selected_type,sheave_d):
                    htab = funcs.h_table_vbelt(speed, sheave_d, selected_type)
                    ans = funcs.ha_vbelt(k1, k2, htab)
                    fans = f"B = {ans}"
                    self.textBrowser.setText(fans)
                    
                elif not is_standard_speed(speed) and is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"B(bad v) = {ans}"
                        self.textBrowser.setText(fans)

                elif is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"B(bad sheave_d) = {ans}"
                        self.textBrowser.setText(fans)

                elif not is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley_and_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"B(both_bad) = {ans}"
                        self.textBrowser.setText(fans)

            elif selected_type == "C":
                sheave_d = self.comboBox_12.currentText()
                if not is_numeric_string(sheave_d):
                    sheave_d = 0

                if is_standard_speed(speed) and is_standard_sheave_d(selected_type,sheave_d):
                    htab = funcs.h_table_vbelt(speed, sheave_d, selected_type)
                    ans = funcs.ha_vbelt(k1, k2, htab)
                    fans = f"C = {ans}"
                    self.textBrowser.setText(fans)
                    
                elif not is_standard_speed(speed) and is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"C(bad v) = {ans}"
                        self.textBrowser.setText(fans)

                elif is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"C(bad sheave_d) = {ans}"
                        self.textBrowser.setText(fans)

                elif not is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley_and_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"C(both_bad) = {ans}"
                        self.textBrowser.setText(fans)


            elif selected_type == "D":
                sheave_d = self.comboBox_13.currentText()
                if not is_numeric_string(sheave_d):
                    sheave_d = 0

                if is_standard_speed(speed) and is_standard_sheave_d(selected_type,sheave_d):
                    htab = funcs.h_table_vbelt(speed, sheave_d, selected_type)
                    ans = funcs.ha_vbelt(k1, k2, htab)
                    fans = f"D = {ans}"
                    self.textBrowser.setText(fans)
                    
                elif not is_standard_speed(speed) and is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"D(bad v) = {ans}"
                        self.textBrowser.setText(fans)

                elif is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"D (bad sheave_d) = {ans}"
                        self.textBrowser.setText(fans)

                elif not is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley_and_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"D(both_bad) = {ans}"
                        self.textBrowser.setText(fans)

            elif selected_type == "E":
                sheave_d = self.comboBox_14.currentText()
                if not is_numeric_string(sheave_d):
                    sheave_d = 0

                if is_standard_speed(speed) and is_standard_sheave_d(selected_type,sheave_d):
                    htab = funcs.h_table_vbelt(speed, sheave_d, selected_type)
                    ans = funcs.ha_vbelt(k1, k2, htab)
                    fans = f"E = {ans}"
                    self.textBrowser.setText(fans)
                    
                elif not is_standard_speed(speed) and is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"E (bad v) = {ans}"
                        self.textBrowser.setText(fans)

                elif is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else:
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"E (bad sheave_d) = {ans}"
                        self.textBrowser.setText(fans)

                elif not is_standard_speed(speed) and not is_standard_sheave_d(selected_type, sheave_d):
                    htab = funcs.h_table_vbelt_int_pulley_and_speed(speed, sheave_d, selected_type)
                    if is_htab_error_message(htab):
                        self.textBrowser.setText(htab)
                    else: 
                        ans = funcs.ha_vbelt(k1, k2, htab)
                        fans = f"E(both_bad) = {ans}"
                        self.textBrowser.setText(fans)




    def dynamic_combo_ha_vbelt(self):
        selected_type = self.comboBox_9.currentText()
        if selected_type == "A":
            self.comboBox_10.show()
            self.comboBox_11.hide()
            self.comboBox_12.hide()
            self.comboBox_13.hide()
            self.comboBox_14.hide()
        elif selected_type == "B":
            self.comboBox_10.hide()
            self.comboBox_11.show()
            self.comboBox_12.hide()
            self.comboBox_13.hide()
            self.comboBox_14.hide()
        elif selected_type == "C":
            self.comboBox_10.hide()
            self.comboBox_11.hide()
            self.comboBox_12.show()
            self.comboBox_13.hide()
            self.comboBox_14.hide()
        elif selected_type == "D":
            self.comboBox_10.hide()
            self.comboBox_11.hide()
            self.comboBox_12.hide()
            self.comboBox_13.show()
            self.comboBox_14.hide()
        elif selected_type == "E":
            self.comboBox_10.hide()
            self.comboBox_11.hide()
            self.comboBox_12.hide()
            self.comboBox_13.hide()
            self.comboBox_14.show()

    def dynamic_combo_lp(self):
        selected_type = self.comboBox_2.currentText()
        if selected_type == "A":
            self.comboBox_4.show()
            self.comboBox_5.hide()
            self.comboBox_6.hide()
            self.comboBox_7.hide()
            self.comboBox_8.hide()
        if selected_type == "B":
            self.comboBox_4.hide()
            self.comboBox_5.show()
            self.comboBox_6.hide()
            self.comboBox_7.hide()
            self.comboBox_8.hide()
        if selected_type == "C":
            self.comboBox_4.hide()
            self.comboBox_5.hide()
            self.comboBox_6.show()
            self.comboBox_7.hide()
            self.comboBox_8.hide()
        if selected_type == "D":
            self.comboBox_4.hide()
            self.comboBox_5.hide()
            self.comboBox_6.hide()
            self.comboBox_7.show()
            self.comboBox_8.hide()
        if selected_type == "E":
            self.comboBox_4.hide()
            self.comboBox_5.hide()
            self.comboBox_6.hide()
            self.comboBox_7.hide()
            self.comboBox_8.show()

    
    def cente_distance_vbelt(self):
        # dont write center_dist.... fullname!
        lp = self.DoubleSpinBox_93.value()
        capd = self.DoubleSpinBox_94.value()
        d = self.DoubleSpinBox_95.value() 
        ans = funcs.center_distance_vbelt(lp, capd, d)
        fans = f"C vBelt(in); center-to-center distance pulley vBelt = {ans}"
        self.textBrowser.setText(fans)

    def hd_vbelt_load(self):
        h_nom = self.DoubleSpinBox_99.value()
        k_s = self.DoubleSpinBox_98.value()
        n_d = self.DoubleSpinBox_100.value()
        ans = funcs.hd_vbelt(h_nom, k_s, n_d)
        fans = f"Hd vBelt; Design Power vBelt = {ans}"
        self.textBrowser.setText(fans)

    def nb_vbelt_load(self):
        h_d = self.DoubleSpinBox_105.value()
        h_a = self.DoubleSpinBox_104.value()
        ans = funcs.nb_vbelt(h_a , h_d)
        fans = f"Nb vBelt; Minimum number of vBelts = {ans}"
        self.textBrowser.setText(fans)

    def fc_vbelt_load(self):
        k_c = self.DoubleSpinBox_106.value()
        v = self.DoubleSpinBox_107.value()
        ans = funcs.fc_vbelt(k_c, v)
        fans = f"Fc vBelt(Ibf); Centrifugal Tension = {ans}"
        self.textBrowser.setText(fans)

    def deltaf_vebelt_load(self):
        h_d = self.DoubleSpinBox_108.value()
        n_b = self.DoubleSpinBox_109.value()
        n = self.DoubleSpinBox_111.value()
        d = self.DoubleSpinBox_110.value()
        ans = funcs.delta_f_vbelt(h_d, n_b, n, d)
        fans = f"ΔF vBelt(Ibf); Power that is transmitted per vBelt = {ans}"
        self.textBrowser.setText(fans)


    def expphi_vbelt(self):
        theta = self.DoubleSpinBox_593.value()
        ans = funcs.expophi_vbelt(theta)
        fans = f"ΔF vBelt(Ibf); Power that is transmitted per vBelt = {ans}"
        self.textBrowser.setText(fans)    

    def f1_vebelt_load(self):
        f_c = self.DoubleSpinBox_112.value()
        deltaf = self.DoubleSpinBox_113.value()
        exp = self.DoubleSpinBox_114.value()
        ans = funcs.f1_vbelt(f_c, deltaf, exp)
        fans = f"F1 vBelt(Ibf); Largest Tension = {ans}"
        self.textBrowser.setText(fans)

    def f2_vbelt_load(self):
        deltaf = self.DoubleSpinBox_115.value()
        exp = self.DoubleSpinBox_116.value()
        ans = funcs.f2_vbelt(deltaf, exp)
        fans = f"F2 vBelt; Least Tension = {ans}"
        self.textBrowser.setText(fans)    

    def fi_vbelt_load(self):
        f_1 = self.DoubleSpinBox_117.value()
        f_2 = self.DoubleSpinBox_118.value()
        f_c = self.DoubleSpinBox_119.value()
        ans = funcs.fi_vbelt(f_1, f_2, f_c)
        fans = f"Fi vBelt(Ibf); Initial Tension = {ans}"
        self.textBrowser.setText(fans)

    def nfs_vbelt_load(self):
        h_a = self.DoubleSpinBox_120.value()
        n_b = self.DoubleSpinBox_121.value()
        h_nom = self.DoubleSpinBox_122.value()
        k_s = self.DoubleSpinBox_123.value()
        ans = funcs.nfs_vbelt(h_a, n_b, h_nom, k_s)
        fans = f"η_fs vBelt; factor of safety vBelt = {ans}"
        self.textBrowser.setText(fans)

    def fb12_vbelt_load(self):
        kb = self.DoubleSpinBox_124.value()
        c_d = self.DoubleSpinBox_125.value()
        ans1 = funcs.fb1_vbelt(kb, c_d)
        ans1 = round(ans1,3)
        d = self.DoubleSpinBox_126.value()
        ans2 = funcs.fb2_vbelt(kb, d)
        ans2 = round(ans2, 3)
        fans = f"Fb1,Fb2 vBelt(Ibf); Maximum tensile stress\
        at the driving sheave(Fb1) & at driven pulley(Fb2) = {ans1}, {ans2}"
        self.textBrowser.setText(fans)

    def t12_vbelt_load(self):
        fb1 = self.DoubleSpinBox_127.value()
        fb2 = self.DoubleSpinBox_128.value()
        f1 = self.DoubleSpinBox_129.value()
        ans1 = funcs.t1_vbelt(f1, fb1)
        ans1 = round(ans1,3)
        ans2 = funcs.t2_vbelt(f1, fb2)
        ans2 = round(ans2, 3)
        fans = f"T1,T2 vBelt(Ibf); Maximum Tensile Stress vBelt = {ans1}, {ans2}"
        self.textBrowser.setText(fans)

    def np_vbelt_load(self):
        k = self.DoubleSpinBox_130.value()
        b = self.DoubleSpinBox_131.value()
        t1 = self.DoubleSpinBox_132.value()
        t2 = self.DoubleSpinBox_133.value()
        ans = funcs.np_vbelt(k, b, t1, t2)
        fans = f"Np vBelt = {ans}; Number of Passes"
        self.textBrowser.setText(fans)

    def t_vbelt_load(self):
        n_p = self.DoubleSpinBox_134.value()
        l_p = self.DoubleSpinBox_135.value()
        v = self.DoubleSpinBox_136.value()
        ans = funcs.t_vbelt(n_p, l_p, v)
        ans = round(ans, 3)
        fans = f"t vBelt; Lifetime of vBelt (hour) = {ans}"
        self.textBrowser.setText(fans)

if __name__ == "__main__":
    import sys
    import qdarktheme

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    # def load_stylesheet(app, qss_file_path):
    #     with open(qss_file_path, "r") as file:
    #         app.setStyleSheet(file.read())
    # load_stylesheet(app, "theme/Takezo.qss")  
    
    #stylesheet = qdarktheme.load_stylesheet("dark")
    #app.setStyleSheet(stylesheet)   
    MainWindow = Ui_MainWindow()
      

    MainWindow.show()
    sys.exit(app.exec_())
