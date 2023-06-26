score = float(input("시험점수를 입력해주세요 : "))
if score >=90 :
    grade = ('A')
elif score >=80 :
    grade = ('B')
elif score >=70 :
    grade = ('C')
elif score >=60 :
    grade = ('D')
else:
    grade = ('F')
print('학점은', grade ,'입니다')