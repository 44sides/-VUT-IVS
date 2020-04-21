from PyQt5 import QtWidgets
import math_library
from gui.GUI import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.addHolding = False
        self.substractHolding = False
        self.multiplyHolding = False
        self.divideHolding = False
        self.powerHolding = False

        self.windowClearing = False

        self.answer = 0

        # operand > 13 cislic (max_length_input) nemozne v okne
        # vysledek > 17 znaku (max_length_output) nemozne v okne - preplneno
        self.max_length_input = 13
        self.max_length_output = 17

        # status tecky a plus/minus
        self.pointStatus = False
        self.plus_minusStatus = False

        # Connect buttons
        self.pushButton_0.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_1.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_2.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_3.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_4.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_5.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_6.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_7.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_8.clicked.connect(lambda: self.digit_pressed())
        self.pushButton_9.clicked.connect(lambda: self.digit_pressed())

        self.pushButton_point.clicked.connect(lambda: self.point_pressed())

        self.pushButton_plus_minus.clicked.connect(lambda: self.plus_minus_pressed())

        self.pushButton_add.clicked.connect(lambda: self.binary_operation_pressed())
        self.pushButton_substract.clicked.connect(lambda: self.binary_operation_pressed())
        self.pushButton_multiply.clicked.connect(lambda: self.binary_operation_pressed())
        self.pushButton_divide.clicked.connect(lambda: self.binary_operation_pressed())

        self.pushButton_factorial.clicked.connect(lambda: self.fact_pressed())
        self.pushButton_power.clicked.connect(lambda: self.binary_operation_pressed())

        self.pushButton_equal.clicked.connect(lambda: self.equal_pressed())
        self.pushButton_clear.clicked.connect(lambda: self.clear_pressed())

    def digit_pressed(self):
        # v pripade vyskytu znaku, menime max pocet a pak kontrolujeme (Kladen duraz na kontrolu pocetu cislic)
        if not (float(self.label_main.text())).is_integer():
            self.max_length_input = self.max_length_input + 1
        if self.label_main.text()[0] == '-':
            self.max_length_input = self.max_length_input + 1

        if len(self.label_main.text()) < self.max_length_input or self.windowClearing:

            # dostavani znaku na tlacitku
            button = self.sender()

            if self.windowClearing:
                new_label = format(float(button.text()), '.13g')
                self.windowClearing = False
            else:
                # osetreni moznosti vlozit '0' po tecce
                if self.pointStatus and button.text() == "0":
                    new_label = self.label_main.text() + button.text()
                else:
                    # utvoreni noveho lablu s dodatkem ve formatu .13g (vedecky, po 13 cislicich zkraceni do 'n'E+x)
                    new_label = format(float(self.label_main.text() + button.text()), '.13g')
            # ulozeni noveho lablu
            self.label_main.setText(new_label)

        # obnoveni max pocetu
        self.max_length_input = 13

    def point_pressed(self):
        # nastaveni po objeveni tecky
        if not self.pointStatus:
            self.label_main.setText(self.label_main.text() + '.')
            self.pointStatus = True

    def plus_minus_pressed(self):
        # osetreni pripadu '-0'
        if self.label_main.text() != '0':
            self.label_main.setText(format(float(self.label_main.text()) * -1, '.13g'))

    def fact_pressed(self):
        self.operand = float(self.label_main.text())
        new_label = format(math_library.fact(self.operand), '.13g')
        self.label_main.setText(new_label)
        self.windowClearing = self.new_window_jump()

    def binary_operation_pressed(self):
        button = self.sender()
        self.operand = float(self.label_main.text())

        if self.addHolding:
            self.holding_button_clearing()
            self.answer = math_library.add(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        elif self.substractHolding:
            self.holding_button_clearing()
            self.answer = math_library.sub(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        elif self.multiplyHolding:
            self.holding_button_clearing()
            self.answer = math_library.mul(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        elif self.divideHolding:
            self.holding_button_clearing()
            self.answer = math_library.div(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        elif self.powerHolding:
            self.holding_button_clearing()
            self.answer = math_library.pow(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        elif self.powerHolding:
            self.holding_button_clearing()
            self.answer = math_library.pow(self.answer, self.operand)
            self.label_main.setText(format(float(self.answer), '.13g'))
            self.holding_button_setting(button)
        else:
            self.answer = self.operand
            self.holding_button_setting(button)

        self.windowClearing = self.new_window_jump()

    def equal_pressed(self):
        self.operand = float(self.label_main.text())

        if self.addHolding:
            self.holding_button_clearing()
            self.answer = math_library.add(self.answer, self.operand)
        elif self.substractHolding:
            self.holding_button_clearing()
            self.answer = math_library.sub(self.answer, self.operand)
        elif self.multiplyHolding:
            self.holding_button_clearing()
            self.answer = math_library.mul(self.answer, self.operand)
        elif self.divideHolding:
            self.holding_button_clearing()
            self.answer = math_library.div(self.answer, self.operand)
        elif self.powerHolding:
            self.holding_button_clearing()
            self.answer = math_library.pow(self.answer, self.operand)
        else:
            self.answer = self.operand

        self.label_main.setText(format(float(self.answer), '.13g'))
        self.windowClearing = self.new_window_jump()

    def clear_pressed(self):
        self.holding_button_clearing()
        self.label_main.setText('0')

    def holding_button_clearing(self):
        self.addHolding = False
        self.substractHolding = False
        self.multiplyHolding = False
        self.divideHolding = False
        self.powerHolding = False

    def holding_button_setting(self, button):
        if button.text() == '+':
            self.addHolding = True
        elif button.text() == '−':
            self.substractHolding = True
        elif button.text() == '×':
            self.multiplyHolding = True
        elif button.text() == '÷':
            self.divideHolding = True
        elif button.text() == 'xʸ':
            self.powerHolding = True

    def new_window_jump(self):
        self.pointStatus = False
        return True
