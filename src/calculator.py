from PyQt5 import QtWidgets
from math_library import Math_library as math_library
from gui.GUI import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.text = False
        self.OverFlowError = False
        self.TryBranch = False
        self.NULLInsert = True

        self.specialHolding = False
        self.specialEntry = False
        self.specialButtonClickedCounter = 0

        self.addHolding = False
        self.substractHolding = False
        self.multiplyHolding = False
        self.divideHolding = False
        self.powerHolding = False
        self.rootHolding = False

        self.windowClearing = False

        self.operand = 0
        self.first_special_operand = 0
        self.second_special_operand = 0
        self.answer = 0
        self.num = None
        self.num_counter = 0

        self.saving = None

        # operand > 13 cislic (max_length_input) nemozne v okne
        self.max_length_input = 13

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
        self.pushButton_root.clicked.connect(lambda: self.binary_operation_pressed())

        self.pushButton_equal.clicked.connect(lambda: self.equal_pressed())
        self.pushButton_clear.clicked.connect(lambda: self.clear_pressed())
        self.pushButton_backspace.clicked.connect(lambda: self.backspace_pressed())
        self.pushButton_save.clicked.connect(lambda: self.save_pressed())

        self.pushButton_save.setCheckable(True)

    def digit_pressed(self):
        # v pripade vyskytu znaku, menime max pocet a pak kontrolujeme (Kladen duraz na kontrolu pocetu cislic)
        if not self.text:
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
                if self.text:
                    self.label_upper.setText("")
                    self.text = False
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
        if self.windowClearing:
            self.label_main.setText('0')
            self.windowClearing = False
        elif not self.pointStatus:
            self.label_main.setText(self.label_main.text() + '.')
            self.pointStatus = True

    def plus_minus_pressed(self):
        if self.label_main.text() == 'ERROR':
            self.clear_pressed()
        else:
            # osetreni pripadu '-0'
            if self.label_main.text() != '0':
                self.label_main.setText(format(float(self.label_main.text()) * -1, '.13g'))

    def fact_pressed(self):
        if self.label_main.text() == 'ERROR':
            self.clear_pressed()
            self.label_upper.setText("")
        else:
            self.operand = float(self.label_main.text())

            if self.operand > 170 or self.operand < 0 or (not self.operand.is_integer()):
                self.label_main.setText('ERROR')
                self.NULLInsert = False
                self.clear_pressed()
            else:
                new_label = format(math_library.fact(self.operand), '.13g')
                self.label_main.setText(new_label)
                self.windowClearing = self.new_window_jump()

    def binary_operation_pressed(self):
        if self.text:
            self.label_upper.setText("")
            self.text = False

        if self.label_main.text() == 'ERROR':
            self.clear_pressed()
            self.label_upper.setText("")
        else:
            button = self.sender()
            self.operand = float(self.label_main.text())
            self.log_insert(self.label_main.text(), button.text())

            if self.specialHolding:
                self.second_special_operand = self.operand
                try:
                    self.TryBranch = True
                    self.special_calculation(self.first_special_operand, self.second_special_operand, self.TryBranch)
                    self.TryBranch = False
                except ArithmeticError:
                    self.OverFlowError = True
                else:
                    if not self.OverFlowError:
                        self.operand = self.special_calculation(self.first_special_operand, self.second_special_operand,
                                                                self.TryBranch)

                self.specialHolding = False

            if button.text() == 'xʸ' or button.text() == 'ⁿ√x':
                self.specialButtonClickedCounter = self.specialButtonClickedCounter + 1
            else:
                self.specialButtonClickedCounter = 0

            if self.specialButtonClickedCounter >= 2:
                self.operands_connection()
                self.holding_button_clearing()

            if not self.special_button_check(button):
                if self.addHolding:
                    self.holding_button_clearing()
                    self.answer = math_library.add(self.answer, self.operand)
                    self.label_main.setText(format(float(self.answer), '.13g'))
                elif self.substractHolding:
                    self.holding_button_clearing()
                    self.answer = math_library.sub(self.answer, self.operand)
                    self.label_main.setText(format(float(self.answer), '.13g'))
                elif self.multiplyHolding:
                    self.holding_button_clearing()
                    self.answer = math_library.mul(self.answer, self.operand)
                    self.label_main.setText(format(float(self.answer), '.13g'))
                elif self.divideHolding:
                    self.holding_button_clearing()
                    self.answer = math_library.div(self.answer, self.operand)
                    self.label_main.setText(format(float(self.answer), '.13g'))
                else:
                    self.answer = self.operand
                    self.holding_button_setting(button)
                    self.label_main.setText(format(float(self.answer), '.13g'))

            if not self.overflow_check(self.OverFlowError, self.answer):
                self.holding_button_setting(button)
                self.windowClearing = self.new_window_jump()
            else:
                self.NULLInsert = False
                self.clear_pressed()

    def equal_pressed(self):
        self.label_upper.setText(self.label_upper.text() + self.label_main.text())
        self.operand = float(self.label_main.text())

        if self.specialHolding:
            self.second_special_operand = self.operand
            try:
                self.TryBranch = True
                self.special_calculation(self.first_special_operand, self.second_special_operand, self.TryBranch)
                self.TryBranch = False
            except ArithmeticError:
                self.OverFlowError = True
            else:
                if not self.OverFlowError:
                    self.operand = self.special_calculation(self.first_special_operand, self.second_special_operand,
                                                            self.TryBranch)

            self.specialHolding = False

        if not self.OverFlowError:
            if self.addHolding:
                self.holding_button_clearing()
                try:
                    math_library.add(self.answer, self.operand)
                except ArithmeticError:
                    self.OverFlowError = True
                else:
                    self.answer = math_library.add(self.answer, self.operand)
            elif self.substractHolding:
                self.holding_button_clearing()
                try:
                    math_library.sub(self.answer, self.operand)
                except ArithmeticError:
                    self.OverFlowError = True
                else:
                    self.answer = math_library.sub(self.answer, self.operand)
            elif self.multiplyHolding:
                self.holding_button_clearing()
                try:
                    math_library.mul(self.answer, self.operand)
                except ArithmeticError:
                    self.OverFlowError = True
                else:
                    self.answer = math_library.mul(self.answer, self.operand)
            elif self.divideHolding:
                self.holding_button_clearing()
                try:
                    math_library.div(self.answer, self.operand)
                except ArithmeticError:
                    self.OverFlowError = True
                else:
                    self.answer = math_library.div(self.answer, self.operand)
            else:
                self.answer = self.operand

        if not self.overflow_check(self.OverFlowError, self.answer):
            self.label_main.setText(format(float(self.answer), '.13g'))
            if not (float(self.label_main.text())).is_integer():
                self.pointStatus = True

        self.NULLInsert = False
        self.clear_pressed()

    def clear_pressed(self):
        self.holding_button_clearing()
        self.specialHolding = False
        self.specialEntry = False
        self.pointStatus = False
        self.text = False
        self.OverFlowError = False
        self.TryBranch = False
        self.specialButtonClickedCounter = 0

        if self.NULLInsert:
            self.label_upper.setText("")
            self.label_main.setText('0')
        else:
            self.text = True
            self.windowClearing = self.new_window_jump()
            self.NULLInsert = True

    def holding_button_clearing(self):
        self.addHolding = False
        self.substractHolding = False
        self.multiplyHolding = False
        self.divideHolding = False

        self.powerHolding = False
        self.rootHolding = False

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
        elif button.text() == 'ⁿ√x':
            self.rootHolding = True

    def special_button_check(self, button):
        if button.text() == 'xʸ' or button.text() == 'ⁿ√x':
            self.first_special_operand = float(self.label_main.text())
            self.specialHolding = True
            return True
        else:
            return False

    def special_calculation(self, first, second, trying):
        if self.powerHolding:
            if not trying:
                self.powerHolding = False
            return math_library.pow(first, second)
        elif self.rootHolding:
            if not trying:
                self.rootHolding = False

            if first < 0 and second % 2 == 0:
                self.OverFlowError = True
            else:
                return math_library.n_root(first, second)

    def new_window_jump(self):
        self.pointStatus = False
        return True

    def operands_connection(self):
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
        else:
            self.answer = self.operand

        self.label_main.setText(format(float(self.answer), '.13g'))
        self.windowClearing = self.new_window_jump()

    def overflow_check(self, overflow, answer):
        if overflow or answer >= math_library.pow(2, 1018):
            self.label_main.setText("ERROR")
            self.text = True
            self.OverFlowError = False
            return True
        else:
            return False

    def backspace_pressed(self):
        if len(self.label_main.text()) == 1:
            self.label_main.setText('0')
        else:
            self.num = self.label_main.text()
            self.num_counter = len(self.label_main.text())
            self.label_main.setText(self.label_main.text()[0])
            for i in range(1, self.num_counter - 1):
                self.label_main.setText(self.label_main.text() + self.num[i])

    def save_pressed(self):
        if self.pushButton_save.isChecked() and not self.label_main.text() == 'ERROR':
            self.saving = self.label_main.text()
            self.label_main.setText('0')
        elif self.pushButton_save.isChecked() and self.label_main.text() == 'ERROR':
            self.pushButton_save.setChecked(False)
        else:
            self.label_main.setText(self.saving)

    def log_insert(self, num, sign):
        if sign == 'xʸ':
            sign = '^'
        elif sign == 'ⁿ√x':
            sign = 'nroot'

        num = format(float(num), '.5g')
        num = str(num)
        new_upper_label = num + ' ' + sign + ' '
        self.label_upper.setText(self.label_upper.text() + new_upper_label)
