class calc_class14:

    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y

    def div(self):
        try:
            return self.num1 / self.num2
        except:
            print("나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요")
            return None

    def squ(self):
        return self.num1 ** self.num2
    
    @classmethod
    def filter(cls, str):
        if str[7] == '1':
            print(f"19{str[0:2]}년 {str[2:4]}월 {str[4:6]}일에 출생한 남성입니다.")
        elif str[7] == '2':
            print(f"19{str[0:2]}년 {str[2:4]}월 {str[4:6]}일에 출생한 여성입니다.")
        elif str[7] == '3':
            print(f"20{str[0:2]}년 {str[2:4]}월 {str[4:6]}일에 출생한 남성입니다.")
        elif str[7] == '4':
            print(f"20{str[0:2]}년 {str[2:4]}월 {str[4:6]}일에 출생한 여성입니다.")
        else:
            print("잘못된 주민등록번호입니다.")

c1 = calc_class14(int(input("숫자입력:")),int(input("숫자입력")))

calc_class14.filter(input("주민번호 입력 : "))

print ("나눗셈 : ",c1.div())
print ("제곱 : ",c1.squ())