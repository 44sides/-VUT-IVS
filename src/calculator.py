from PyQt5 import QtWidgets
from gui.GUI import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # operand > 13 cislic (max_length_input) nemozne v okne
        # vysledek > 17 znaku (max_length_output) nemozne v okne - preplneno
        self.max_length_input = 13
        self.max_length_output = 17

        #status tecky a plus/minus
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

    def digit_pressed(self):
        # v pripade vyskytu znaku, menime max pocet a pak kontrolujeme (Kladen duraz na kontrolu pocetu cislic)
        if not (float(self.label_main.text())).is_integer():
            self.max_length_input = self.max_length_input + 1
        if self.label_main.text()[0] == '-':
            self.max_length_input = self.max_length_input + 1

        if len(self.label_main.text()) < self.max_length_input:

            # dostavani znaku na tlacitku
            button = self.sender()

            # osetreni moznosti vlozit '0' po tecce
            if self.pointStatus and button.text() == "0":
                new_label = self.label_main.text() + button.text()
            else:
                # utvoreni noveho lablu s dodatkem ve formatu .13g (vedecky, po 13 cislicich zkraceni do 'n'E+13)
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