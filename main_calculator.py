import sys
from PyQt5.QtWidgets import *

''' 
    issue3 계산기 기능 추가하기
                issue 7 - 기존 계산 기능 개선
                    (eval을 사용하지 않고 math나 numpy라이브러리 사용)
                issue 8 - 신규 계산 기능 추가
                    (%, 역수 등등)
'''


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        # 수식 입력과 답 출력을 위한 LineEdit 위젯 생성 -issue 5
        self.equation = QLineEdit("")
        layout_equation_solution.addWidget(self.equation)

        # 계산기능에 사용할 변수 -issue7
        self.temp_number = 0
        self.temp_operator = ""

        # 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        # 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(
            lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(
            lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(
            lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(
            lambda state, operation="/": self.button_operation_clicked(operation))

        # 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)

        # =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        # =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        # =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        # 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        # 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        # 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(
            lambda state, num=".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(
            lambda state, num="00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        # 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):

        if operation not in ["square", "root", "inverse", "plusminus"]:
            if (self.temp_operator != ""):
                self.temp_operator = ""
                self.equation.setText("")
                self.temp_operator = operation
            else:
                self.temp_number = float(self.equation.text())
                self.equation.setText("")
                self.temp_operator = operation
        else:
            self.temp_operator = ""
            self.temp_number = 0

    def button_equal_clicked(self):

        temp_second_number = float(self.equation.text())

        'isuue7 기본 연산 구현'
        if self.temp_operator == "+":
            temp_result = self.temp_number+temp_second_number

        elif self.temp_operator == "-":
            temp_result = self.temp_number-temp_second_number

        elif self.temp_operator == "*":
            temp_result = self.temp_number * temp_second_number

        elif self.temp_operator == "/":
            if (temp_second_number != 0.0):
                temp_result = self.temp_number / temp_second_number
            else:
                temp_result = 0

        self.equation.setText(str(temp_result))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.temp_number = ""
        self.temp_operator = ""

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
