import sys
from PyQt5.QtWidgets import *

''' 
    issue 2 계산기 ui 수정 및 개선하기
        issue 4 사칙연산 배치 수정
            (계산기 구조 확인/ 사칙연산을 세로로 줄세우기)
        issue 5 숫자 입력부분 통합
            (두개로 나눠졌던 입력칸을 하나로 통합함)
        issue 6 새 버튼 추가
             (역수나 c,c/e 등을 추가함)
'''


def init_ui(self):
    # layout
    main_layout = QGridLayout()  # main_layout 전체를 통합하는 Gridlayout를 생성함
    layout_equation_solution = QGridLayout()  # 입력창
    layout_clear_equal = QGridLayout()  # 지우고 삭제하는 버튼의 Gridlayout
    layout_operation1 = QGridLayout()  # 기본 사칙연산
    layout_operation2 = QGridLayout()  # 추가 사칙연산
    layout_number = QGridLayout()  # 숫자
    layout_left = QGridLayout()  # 왼쪽 그리드 합치기
    layout_bottom = QGridLayout()  # 아래쪽 그리드 합치기

    # 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
    label_equation = QLabel("Equation: ")
    label_solution = QLabel("Solution: ")
    self.equation = QLineEdit("")
    self.solution = QLineEdit("")

    # layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
    layout_equation_solution.addWidget(label_equation, self.equation)
    layout_equation_solution.addWidget(label_solution, self.solution)

    # 사칙연산 버튼 생성
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
    layout_operation1.addWidget(button_plus)
    layout_operation1.addWidget(button_minus)
    layout_operation1.addWidget(button_product)
    layout_operation1.addWidget(button_division)

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
    main_layout.addLayout(layout_operation1)
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
    equation = self.equation.text()
    equation += operation
    self.equation.setText(equation)


def button_equal_clicked(self):
    equation = self.equation.text()
    solution = eval(equation)
    self.solution.setText(str(solution))


def button_clear_clicked(self):
    self.equation.setText("")
    self.solution.setText("")


def button_backspace_clicked(self):
    equation = self.equation.text()
    equation = equation[:-1]
    self.equation.setText(equation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())