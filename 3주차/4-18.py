###계산을 헷갈리지 않고 하기위한 기호 상수 역할
class Sym:
    OPEN_B = 1
    CLOSE_B = 2
    PLUS = 3
    MINUS = 4
    TIMES = 5
    DIVIDE = 6
    MOD = 7
    OPERAND = 8
###중위 수식을 후위 수식으로 변환, 계산
class Experession:
    def __init__(self, expr):
        self.expr = expr #입력한 중위 수식
        self.stack = [] #변환 시 연산자 저장, 계산 시 피연산자 저장
        self.output = [] #변환한 후위 수식 저장
        self.size = 100
        self.top = -1 
    ##공백 없는 수식을 분해
    def spl(self):
        lst = [] #분해한 수식을 저장할 리스트
        num = ''
        for i in self.expr:
            if i.isdigit(): #숫자라면
                num += i #숫자끼리 합쳐 원래 숫자로 만들어 줌
            else: #연산자가 나오면 합치기를 끝냄
                if num:
                    lst.append(int(num))  #숫자로 변환하여 추가
                    num = ''  #num 초기화
                lst.append(i)  #연산자 추가
        if num:  # 마지막 숫자가 남아있다면 추가
            lst.append(num)
        self.expr = lst #분해가 끝난 수식 리스트를를 expr가 가리키로록 함
    ##괄호를 알맞게 입력했는지 확인
    def check_B(self):
        a = 0
        for i in self.expr:
            op = self.getSymtype(i)
            if op == Sym.OPEN_B:
                a += 1
            elif op == Sym.CLOSE_B:
                a -= 1
        return a
    ##스택에 원소 추가
    def push(self, item): 
        if self.top < self.size-1: #스택이 풀 상태인지 확인
            self.top += 1
            self.stack.append(item)
        else: print("Stack Full")
    ##스택에서 원소 삭제
    def pop(self):
        if self.top > -1: #스택이 빈 상태인지 확인
            self.top -= 1
            return self.stack.pop()
        else: print("Stack Empty")
    ##연산자 우선순위를 지정
    def precedence(self, op):
        if op == '(': return 0
        elif op in ['+', '-']: return 1
        elif op in ['*', '/', '%']: return 2
    ##각 연산자를 숫자에 대입
    def getSymtype(self, sym):
        if sym == '(': sym_type = Sym.OPEN_B
        elif sym == ')': sym_type = Sym.CLOSE_B
        elif sym == '+': sym_type = Sym.PLUS
        elif sym == '-': sym_type = Sym.MINUS
        elif sym == '*': sym_type = Sym.TIMES
        elif sym == '/': sym_type = Sym.DIVIDE
        elif sym == '%': sym_type = Sym.MOD
        else: sym_type = Sym.OPERAND
        return sym_type
    ##후위 수식의 값 계산
    def eval_postfix(self):
        for sym in self.output:
            sym_type = self.getSymtype(sym)
            if sym_type == Sym.OPERAND: #피연산자인 경우
                self.push(float(sym)) #실수형으로 변환 후 스택에 원소 추가
            else: #연산자인 경우
                #피연산자 두개를 꺼냄
                op2 = self.pop()
                op1 = self.pop()
                if sym_type == Sym.PLUS:
                    self.push(op1 + op2)
                elif sym_type == Sym.MINUS:
                    self.push(op1 - op2)
                elif sym_type == Sym.TIMES:
                    self.push(op1 * op2)
                elif sym_type == Sym.DIVIDE:
                    self.push(op1 / op2)
                elif sym_type == Sym.MOD:
                    self.push(op1 % op2) 
        return self.pop()
    ##후위 수식으로 변환
    def infix_fostfix(self):
        for token in self.expr:
            if str(token).isdigit(): #피연산자라면
                self.output.append(token)
            elif token == '(':
                self.push(token)
            elif token == ')':
                sym = self.pop()
                while sym != '(':
                    self.output.append(sym)
                    sym = self.pop()
            else: #연산자라면
                while self.top > -1 and \
                self.precedence(self.stack[-1]) >= self.precedence(token):
                    sym = self.pop()
                    self.output.append(sym)
                self.push(token)
        while self.top > -1: #스택에 남아있는 원소를 모두 옮기기
            self.output.append(self.pop())
    ##출력
    def print_result(self):
        for i in self.output:
            print(i, end = ' ')

expr = input('>>> input an infix: ') #전위 수식 입력받기
e = Experession(expr)
e.spl()
if e.check_B() != 0: #입력된 괄호가 이상하다면 오류 메세지
    print('괄호 오류')
else:
    e.infix_fostfix() #후위수식으로 변환
    #후위 수식 출력
    print("postfix:", end = ' ')
    for i in e.output:
        print(i, end = ' ')
    print() #후위 수식 출력 후 줄바꿈
    e.stack = [] #계산을 위해 스택 비우기
    print('evaluation =', e.eval_postfix()) #계산 결과 출력