import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

calculator.setFixedSize(315, 435)
calculator.setWindowTitle('Pocket Calc')

sys.exit(app.exec_())
