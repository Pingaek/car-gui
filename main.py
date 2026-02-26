import sys
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from db_connect import db, cursor

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi('cms.ui', self)

    self.tb_car.setColumnWidth(0, 50)
    self.tb_car.setColumnWidth(1, 150)
    self.tb_car.setColumnWidth(2, 150)
    self.tb_car.setColumnWidth(3, 100)
    self.tb_car.setColumnWidth(4, 180)

    self.btn_add.clicked.connect(self.insert_car)

  def say_hi(self):
    QMessageBox.information(self, 'Information', 'Hello World!')

  def insert_car(self):
    brand = self.txt_brand.text()
    model = self.txt_model.text()
    year = self.txt_year.text()
    price = self.txt_price.text()

    sql = 'insert into car(brand, model, year, price) values(?, ?, ?, ?)'
    values = (brand, model, year, price)

    rs = cursor.execute(sql, values)
    db.commit()
    if rs.rowcount>0:
      QMessageBox.information(self, 
                              'Information', 
                              'Insert car successful!')
    else:
      QMessageBox.warning(self, 
                              'Warning', 
                              'Unable to insert car!')

    self.clear()

  def clear(self):
    self.txt_brand.setText('')
    self.txt_model.setText('')
    self.txt_year.setText('')
    self.txt_price.setText('')
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()