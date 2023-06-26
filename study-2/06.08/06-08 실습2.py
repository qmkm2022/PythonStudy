class calc_class12 :

    num1 = num2 = 0

    def member_clear(self,x,y):
        self.num1 = x
        self.num2 = y

    def division(self):
        return self.num1 / self.num2
    
    def square(self):
        return self.num1 ** self.num2

obj = calc_class12.member_clear(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))

print('나눗셈 ', obj.division()) 
print('제곱 ', obj.square())