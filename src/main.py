## @file main.py
# @brief Implementation of project main
# @see calculator.CalculatorWindow
# @see GUI.Ui_Calculator
# @pre Functional GUI and Controller
#
# @package CalculatorPack
# @brief Package of files for calculator program
# @see main.py
# @see GUI.py
# @see calculator.py
# @see math_library.py

import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow

## Preparation for GUI launch
app = QApplication(sys.argv)

## Controller connection
calculator = CalculatorWindow()

sys.exit(app.exec_())
