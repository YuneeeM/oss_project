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


class Main(QDialog):  # 메인 클래스
    def __init__(self):
        super().__init__()
        self.init_ui()  # init_ui 메소드에서 모든 작업이 이뤄짐

    def init_ui(self):
        'layout'
        main_layout = QGridLayout()  # main_layout 전체를 통합하는 Gridlayout를 생성함
        layout_equation_solution = QGridLayout()  # 입력창
        layout_clear_equal = QGridLayout()  # 지우고 삭제하는 버튼의 Gridlayout
        layout_operation1 = QGridLayout()  # 기본 사칙연산
        layout_operation2 = QGridLayout()  # 추가 사칙연산
        layout_number = QGridLayout()  # 숫자
        layout_left = QGridLayout()  # 왼쪽 그리드 합치기
        layout_bottom = QGridLayout()  # 아래쪽 그리드 합치기

        # 수식 입력과 답 출력을 위한 LineEdit 위젯 생성 -issue 5
        self.equation = QLineEdit("")
        layout_equation_solution.addWidget(self.equation)

        'button'
        # 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_equal = QPushButton("=")

        # 새 버튼들 - issue6
        button_remainder = QPushButton("%")  # 나머지
        button_clear1 = QPushButton("CE")  # 삭제기능1
        button_clear2 = QPushButton("C")  # 삭제기능2
        button_backspace = QPushButton("<=")  # 되돌리기

        button_reciprocal = QPushButton("1/x")  # 역수
        button_square = QPushButton("x^2")  # 제곱
        button_root = QPushButton("x^1/2")  # 제곱근
        button_dot = QPushButton(".")  # 부동소수점
        button_plusminus = QPushButton("+/-")  # 플/마

        # 위젯 추가
        layout_clear_equal.addWidget(button_remainder, 0, 0)
        layout_clear_equal.addWidget(button_clear1, 0, 1)
        layout_clear_equal.addWidget(button_clear2, 0, 2)

        layout_operation2.addWidget(button_reciprocal, 0, 0)
        layout_operation2.addWidget(button_square, 0, 1)
        layout_operation2.addWidget(button_root, 0, 2)

        layout_operation1.addWidget(button_backspace, 0, 0)
        layout_operation1.addWidget(button_division, 1, 0)
        layout_operation1.addWidget(button_product, 2, 0)
        layout_operation1.addWidget(button_minus, 3, 0)
        layout_operation1.addWidget(button_plus, 4, 0)
        layout_operation1.addWidget(button_equal, 5, 0)

        'click'
        # 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        # 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(
            lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(
            lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(
            lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(
            lambda state, operation="/": self.button_operation_clicked(operation))
        button_remainder.clicked.connect(
            lambda state, operation="%": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(
            lambda state, operation="inverse": self.button_operation_clicked(operation))
        button_square.clicked.connect(
            lambda state, operation="square": self.button_operation_clicked(operation))
        button_root.clicked.connect(
            lambda state, operation="root": self.button_operation_clicked(operation))
        button_plusminus.clicked.connect(
            lambda state, operation="plusminus": self.button_operation_clicked(operation))

        # =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        # =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        layout_operation1.addWidget(button_backspace, 0, 0)
        layout_operation1.addWidget(button_division, 1, 0)
        layout_operation1.addWidget(button_product, 2, 0)
        layout_operation1.addWidget(button_minus, 3, 0)
        layout_operation1.addWidget(button_plus, 4, 0)
        layout_operation1.addWidget(button_equal, 5, 0)

        # 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        # 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))

        layout_number.addWidget(number_button_dict[7], 0, 0)
        layout_number.addWidget(number_button_dict[8], 0, 1)
        layout_number.addWidget(number_button_dict[9], 0, 2)
        layout_number.addWidget(number_button_dict[4], 1, 0)
        layout_number.addWidget(number_button_dict[5], 1, 1)
        layout_number.addWidget(number_button_dict[6], 1, 2)
        layout_number.addWidget(number_button_dict[1], 2, 0)
        layout_number.addWidget(number_button_dict[2], 2, 1)
        layout_number.addWidget(number_button_dict[3], 2, 2)
        layout_number.addWidget(number_button_dict[0], 3, 1)

        # 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(
            lambda state, num=".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)
        layout_number.addWidget(button_plusminus, 3, 0)
     # 각 레이아웃을 main_layout 레이아웃에 추가
        layout_left.addLayout(layout_clear_equal, 0, 0)
        layout_left.addLayout(layout_operation2, 1, 0)
        layout_left.addLayout(layout_number, 2, 0)
        layout_bottom.addLayout(layout_left, 0, 0)
        layout_bottom.addLayout(layout_operation1, 0, 1)

        main_layout.addLayout(layout_equation_solution, 0, 0)
        main_layout.addLayout(layout_bottom, 1, 0)

        self.setWindowTitle('유니의 계산기')
        self.setLayout(main_layout)  # main_layout을 QDialog의 layout으로 set함
        self.show()  # QDialog를 화면에 띄움

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
