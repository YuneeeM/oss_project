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

'''
    issue3 계산기 기능 추가하기
                issue 7 - 기존 계산 기능 개선
                    (eval을 사용하지 않고 math나 numpy라이브러리 사용)
                issue 8 - 신규 계산 기능 추가

                    (%, 역수, 제곱, 제곱근 등등)
'''


class Main(QDialog):  # 메인 클래스
    def __init__(self):
        super().__init__()
        self.init_ui()  # init_ui 메소드에서 모든 작업이 이뤄짐

    def init_ui(self):
        'layout'
        # 각 위젯을 배치할 레이아웃을 미리 만들어 둠
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

        'style- self.equation'
        self.equation.setStyleSheet(
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: gray;"
            "border-radius: 5px")

        'temp'
        # issue7 계산기능에 사용할 변수
        self.temp_number = 0
        self.temp_operator = ""

        'button'
        # 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_equal = QPushButton("=")

        'style - button'
        button_equal.setStyleSheet("background-color:#B0C4DE; ")
        button_plus.setStyleSheet("background-color:#ADD8E6; ")
        button_minus.setStyleSheet("background-color:#ADD8E6;")
        button_product.setStyleSheet("background-color: #ADD8E6;")
        button_division.setStyleSheet("background-color: #ADD8E6;")

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
        # =, clear1~2, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear1.clicked.connect(self.button_clear1_clicked)
        button_clear2.clicked.connect(self.button_clear2_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        # 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(
            lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(
            lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(
            lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(
            lambda state, operation="/": self.button_operation_clicked(operation))
        # issue8 -새기능 추가
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

        if operation not in ["square", "root", "inverse", "plusminus"]:
            if (self.temp_operator != ""):
                self.temp_operator = ""
                self.equation.setText("")
                self.temp_operator = operation
            else:
                self.temp_number = float(self.equation.text())
                self.equation.setText("")
                self.temp_operator = operation

        # issue 8 새로운 기능 구현
        else:
            if operation == "square":
                self.temp_number = float(self.equation.text())
                self.temp_number = self.temp_number**2
                self.equation.setText(str(self.temp_number))
                pass
            elif operation == "root":
                self.temp_number = float(self.equation.text())
                self.temp_number = self.temp_number**(1/2)
                self.equation.setText(str(self.temp_number))
                pass
            elif operation == "inverse":
                self.temp_number = float(self.equation.text())
                self.temp_number = 1/self.temp_number
                self.equation.setText(str(self.temp_number))
                pass
            elif operation == "plusminus":
                self.temp_number = float(self.equation.text())
                self.temp_number = (-1)*self.temp_number
                self.equation.setText(str(self.temp_number))
                pass
            self.temp_operator = ""
            self.temp_number = 0

    def button_equal_clicked(self):

        temp_second_number = float(self.equation.text())

        # isuue7 기본 연산 구현
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

        # issue 8 % 기능 구현
        elif self.temp_operator == "%":
            if (temp_second_number != 0.0):
                temp_result = self.temp_number % temp_second_number
            else:
                temp_result = 0
                self.temp_number = 0

        self.equation.setText(str(temp_result))

    # issue8 c와 ce 기능 구현
    def button_clear1_clicked(self):
        self.equation.setText(" ")
        self.temp_number = ""
        self.temp_operator = ""

    def button_clear2_clicked(self):
        self.equation.setText(" ")
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
