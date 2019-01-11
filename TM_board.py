from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from Terraforming_Mars_boad.board1 import Ui_TM_player_board
import sys

font = QtGui.QFont()
font.setPointSize(32)


class MainWindow(QMainWindow, Ui_TM_player_board):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.TR.setText("20")
        self.TR.setFont(font)
        self.Generation.setText("1")
        self.Generation.setFont(font)
        self.money_curr.setText("42")
        self.money_curr.setFont(font)
        self.steel_curr.setText("0")
        self.steel_curr.setFont(font)
        self.titian_curr.setText("0")
        self.titian_curr.setFont(font)
        self.plant_curr.setText("0")
        self.plant_curr.setFont(font)
        self.energy_curr.setText("0")
        self.energy_curr.setFont(font)
        self.heat_curr.setText("0")
        self.heat_curr.setFont(font)
        self.money_prod.setText("0")
        self.money_prod.setFont(font)
        self.steel_prod.setText("0")
        self.steel_prod.setFont(font)
        self.titian_prod.setText("0")
        self.titian_prod.setFont(font)
        self.plant_prod.setText("0")
        self.plant_prod.setFont(font)
        self.energy_prod.setText("0")
        self.energy_prod.setFont(font)
        self.heat_prod.setText("0")
        self.heat_prod.setFont(font)

    def start_new_game(self):
        self.TR.setText("20")
        self.TR.setFont(font)
        self.TR.repaint()
        self.Generation.setText("1")
        self.Generation.setFont(font)
        self.Generation.repaint()
        self.money_curr.setText("42")
        self.money_curr.setFont(font)
        self.money_curr.repaint()
        self.steel_curr.setText("0")
        self.steel_curr.setFont(font)
        self.steel_curr.repaint()
        self.titian_curr.setText("0")
        self.titian_curr.setFont(font)
        self.titian_curr.repaint()
        self.plant_curr.setText("0")
        self.plant_curr.setFont(font)
        self.plant_curr.repaint()
        self.energy_curr.setText("0")
        self.energy_curr.setFont(font)
        self.energy_curr.repaint()
        self.heat_curr.setText("0")
        self.heat_curr.setFont(font)
        self.heat_curr.repaint()
        self.money_prod.setText("0")
        self.money_prod.setFont(font)
        self.money_prod.repaint()
        self.steel_prod.setText("0")
        self.steel_prod.setFont(font)
        self.steel_prod.repaint()
        self.titian_prod.setText("0")
        self.titian_prod.setFont(font)
        self.titian_prod.repaint()
        self.plant_prod.setText("0")
        self.plant_prod.setFont(font)
        self.plant_prod.repaint()
        self.energy_prod.setText("0")
        self.energy_prod.setFont(font)
        self.energy_prod.repaint()
        self.heat_prod.setText("0")
        self.heat_prod.setFont(font)
        self.heat_prod.repaint()

    def gen_go(self):
        self.Generation.setText(str(int(self.Generation.toPlainText()) + 1))
        # calcualtion
        #self.Generation.repaint()
        self.money_curr.setText(str(int(self.TR.toPlainText())+int(self.money_prod.toPlainText())+int(self.money_curr.toPlainText())))
        #self.money_curr.repaint()
        self.steel_curr.setText(str(int(self.steel_curr.toPlainText())+int(self.steel_prod.toPlainText())))
        #self.steel_curr.repaint()
        self.titian_curr.setText(str(int(self.titian_curr.toPlainText())+int(self.titian_prod.toPlainText())))
        #self.titian_curr.repaint()
        self.plant_curr.setText(str(int(self.plant_curr.toPlainText())+int(self.plant_prod.toPlainText())))
        #self.repaint()
        self.heat_curr.setText(str(int(self.heat_curr.toPlainText())+int(self.heat_prod.toPlainText())+int(self.energy_curr.toPlainText())))
        #self.repaint()
        self.energy_curr.setText(str(int(self.energy_prod.toPlainText())))
        self.repaint()

    def tr_add_1(self):
        self.TR.setText(str(int(self.TR.toPlainText()) + 1))
        self.TR.repaint()

    def tr_minus_1(self):
        self.TR.setText(str(int(self.TR.toPlainText()) - 1))
        self.TR.repaint()

    def money_curr_plus_1(self):
        self.interpret('money_curr_plus_1')

    def money_curr_plus_3(self):
        self.interpret('money_curr_plus_3')

    def money_curr_plus_10(self):
        self.interpret('money_curr_plus_10')

    def money_curr_minus_1(self):
        self.interpret('money_curr_minus_1')

    def money_curr_minus_3(self):
        self.interpret('money_curr_minus_3')

    def money_curr_minus_10(self):
        self.interpret('money_curr_minus_10')

    def money_prod_plus_1(self):
        self.interpret('money_prod_plus_1')

    def money_prod_plus_3(self):
        self.interpret('money_prod_plus_3')

    def money_prod_plus_10(self):
        self.interpret('money_prod_plus_10')

    def money_prod_minus_1(self):
        self.interpret('money_prod_minus_1')

    def money_prod_minus_3(self):
        self.interpret('money_prod_minus_3')

    def money_prod_minus_10(self):
        self.interpret('money_prod_minus_10')

    def plant_curr_plus_1(self):
        self.interpret('plant_curr_plus_1')

    def plant_curr_plus_3(self):
        self.interpret('plant_curr_plus_3')

    def plant_curr_plus_8(self):
        self.interpret('plant_curr_plus_8')

    def plant_curr_minus_1(self):
        self.interpret('plant_curr_minus_1')

    def plant_curr_minus_3(self):
        self.interpret('plant_curr_minus_3')

    def plant_curr_minus_8(self):
        self.interpret('plant_curr_minus_8')

    def plant_prod_plus_1(self):
        self.interpret('plant_prod_plus_1')

    def plant_prod_plus_3(self):
        self.interpret('plant_prod_plus_3')

    def plant_prod_plus_8(self):
        self.interpret('plant_prod_plus_8')

    def plant_prod_minus_1(self):
        self.interpret('plant_prod_minus_1')

    def plant_prod_minus_3(self):
        self.interpret('plant_prod_minus_3')

    def plant_prod_minus_8(self):
        self.interpret('plant_prod_minus_8')

    def steel_curr_plus_1(self):
        self.interpret('steel_curr_plus_1')

    def steel_curr_plus_3(self):
        self.interpret('steel_curr_plus_3')

    def steel_curr_plus_10(self):
        self.interpret('steel_curr_plus_10')

    def steel_curr_minus_1(self):
        self.interpret('steel_curr_minus_1')

    def steel_curr_minus_3(self):
        self.interpret('steel_curr_minus_3')

    def steel_curr_minus_10(self):
        self.interpret('steel_curr_minus_10')

    def steel_prod_plus_1(self):
        self.interpret('steel_prod_plus_1')

    def steel_prod_plus_3(self):
        self.interpret('steel_prod_plus_3')

    def steel_prod_plus_10(self):
        self.interpret('steel_prod_plus_10')

    def steel_prod_minus_1(self):
        self.interpret('steel_prod_minus_1')

    def steel_prod_minus_3(self):
        self.interpret('steel_prod_minus_3')

    def steel_prod_minus_10(self):
        self.interpret('steel_prod_minus_10')

    def titian_curr_plus_1(self):
        self.interpret('titian_curr_plus_1')

    def titian_curr_plus_3(self):
        self.interpret('titian_curr_plus_3')

    def titian_curr_plus_10(self):
        self.interpret('titian_curr_plus_10')

    def titian_curr_minus_1(self):
        self.interpret('titian_curr_minus_1')

    def titian_curr_minus_3(self):
        self.interpret('titian_curr_minus_3')

    def titian_curr_minus_10(self):
        self.interpret('titian_curr_minus_10')

    def titian_prod_plus_1(self):
        self.interpret('titian_prod_plus_1')

    def titian_prod_plus_3(self):
        self.interpret('titian_prod_plus_3')

    def titian_prod_plus_10(self):
        self.interpret('titian_prod_plus_10')

    def titian_prod_minus_1(self):
        self.interpret('titian_prod_minus_1')

    def titian_prod_minus_3(self):
        self.interpret('titian_prod_minus_3')

    def titian_prod_minus_10(self):
        self.interpret('titian_prod_minus_10')

    def heat_curr_plus_1(self):
        self.interpret('heat_curr_plus_1')

    def heat_curr_plus_3(self):
        self.interpret('heat_curr_plus_3')

    def heat_curr_plus_8(self):
        self.interpret('heat_curr_plus_8')

    def heat_curr_minus_1(self):
        self.interpret('heat_curr_minus_1')

    def heat_curr_minus_3(self):
        self.interpret('heat_curr_minus_3')

    def heat_curr_minus_8(self):
        self.interpret('heat_curr_minus_8')

    def heat_prod_plus_1(self):
        self.interpret('heat_prod_plus_1')

    def heat_prod_plus_3(self):
        self.interpret('heat_prod_plus_3')

    def heat_prod_plus_8(self):
        self.interpret('heat_prod_plus_8')

    def heat_prod_minus_1(self):
        self.interpret('heat_prod_minus_1')

    def heat_prod_minus_3(self):
        self.interpret('heat_prod_minus_3')

    def heat_prod_minus_8(self):
        self.interpret('heat_prod_minus_8')

    def energy_curr_plus_1(self):
        self.interpret('energy_curr_plus_1')

    def energy_curr_plus_3(self):
        self.interpret('energy_curr_plus_3')

    def energy_curr_plus_8(self):
        self.interpret('energy_curr_plus_8')

    def energy_curr_minus_1(self):
        self.interpret('energy_curr_minus_1')

    def energy_curr_minus_3(self):
        self.interpret('energy_curr_minus_3')

    def energy_curr_minus_8(self):
        self.interpret('energy_curr_minus_8')

    def energy_prod_plus_1(self):
        self.interpret('energy_prod_plus_1')

    def energy_prod_plus_3(self):
        self.interpret('energy_prod_plus_3')

    def energy_prod_plus_8(self):
        self.interpret('energy_prod_plus_8')

    def energy_prod_minus_1(self):
        self.interpret('energy_prod_minus_1')

    def energy_prod_minus_3(self):
        self.interpret('energy_prod_minus_3')

    def energy_prod_minus_8(self):
        self.interpret('energy_prod_minus_8')

    def interpret(self, string):
        source, status, direction, amount = string.split("_")
        obj = getattr(self, source + "_" + status)
        if direction == "plus":
            obj.setText(str(int(obj.toPlainText()) + int(amount)))
        else:
            obj.setText(str(int(obj.toPlainText()) - int(amount)))
        obj.repaint()

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Message', 'You sure to quit?\nChanges will be save.',
    #                                  QMessageBox.Yes | QMessageBox.No,
    #                                  QMessageBox.Yes)
    #     if reply == QMessageBox.Yes:
    #         if self.all_words is not None:
    #             self.save_log()
    #         event.accept()
    #     else:
    #         event.ignore()

    # def keyPressEvent(self, e):
    #     if e.key() == QtCore.Qt.Key_D or e.key() == QtCore.Qt.Key_Right:
    #         self.next_word()
    #     elif e.key() == QtCore.Qt.Key_S or e.key() == QtCore.Qt.Key_Down:
    #         self.show_meaning()
    #     elif e.key() == QtCore.Qt.Key_W or e.key() == QtCore.Qt.Key_Up:
    #         self.set_known_word()
    #     elif e.key() == QtCore.Qt.Key_A or e.key() == QtCore.Qt.Key_Left:
    #         self.prev_word()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
