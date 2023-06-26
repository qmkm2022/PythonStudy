# 066일차-실습-0-3-해답-ver1
class Calc_class13:
    num1 = num2 = 0
    def member_clear(self, pNum1, pNum2):
        self.num1 = pNum1
        self.num2 = pNum2    
    def div(self):
        if self.num1 == 0 or self.num2 == 0:
            return print("나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요.")
        else:
            return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
#
obj = Calc_class13()
obj.member_clear(int(input("1번째 정수를 입력하세요:")),int(input("2번째 정수를 입력하세요:")))
print ("나눗셈 : ",obj.div())
print ("제곱 : ",obj.squ())


# 066일차-실습-0-3-해답-ver2
class Calc_class13:
    num1 = num2 = 0
    def member_clear(self, pNum1, pNum2):
        self.num1 = pNum1
        self.num2 = pNum2
    def div(self):
        try:
            return self.num1 / self.num2
        except:
            print("나눗셈은 0으로 나누기가 불가능합니다.다시 입력하세요")
    def squ(self):
        return self.num1 ** self.num2
#
obj = Calc_class13()
obj.member_clear(int(input("1번째 정수를 입력하세요:")),int(input("2번째 정수를 입력하세요:")))
print ("나눗셈 : ", obj.div())
print ("제곱 : ", obj.squ())


# 066일차-실습-0-3-해답-ver 3: 약간의 개선이 필요함 
class Calc_class13:
    num1 = num2 = 0
    def member_clear(self,x,y):
        self.num1 = x
        self.num2 = y
        if self.num2 == 0:                                                      
            print("나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요.") 
    def div(self):
        if self.num2 == 0:                                                     
            return None
        else:
            return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
#
c1 = Calc_class13()
c1.member_clear(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))
print ("나눗셈 : ",c1.div())
print ("제곱 : ",c1.squ())