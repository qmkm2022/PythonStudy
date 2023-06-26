class calc_class11 :

    x = y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def division(self):
        p = self.x / self.y

        return p 
    
    def square(self):
        m = self.x ** self.y
        return m

num1 = int(input('정수를 입력하세요:'))
num2 = int(input('정수를 입력하세요:'))

obj = calc_class11(num1, num2)

print('나눗셈 ', obj.division()) 
print('제곱 ', obj.square())