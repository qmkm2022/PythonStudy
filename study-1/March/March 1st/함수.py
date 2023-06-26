#a = 1
#print(a)
#print(type(a))
#print(f'지금 사용하는 변수는 {a} 타입은 {type(a)} 입니다')

#def value_print(x):
#    print(x)
#    print(type(x))
#    print(f'지금 사용하는 변수는 {x} 타입은 {type(x)} 입니다')

#a = value_print(2)
#b = value_print('string')

#def hello():
#    print('hello world!')

#hello()

#빈함수
# def hello3():
#     pass
# hello3()
# 
# # 덧셈함수 선언
# def sum1(a, b):
#     result = a + b
#     return  result
# 
# #함수 호출
# #a = sum1(5, 6)
# #print(a)
# 
# def sum2(a,b):
#     print(a + b)
# sum1(100,20)
# sum2(30,50)
# 
# def sum_mul2(a,b):
#   result_sum = a+b
#   result_mul = a*b
#   print(result_sum)
#   print(result_mul)
# sum_mul2(5,7)

# # 언패킹
# x = (10, 20, 30)
# print(x)
# print(*x) # 언패킹

# def my_fuc(a):
#     print(f'my_fuc에는 {a}가 있고 타임은{type(a)}라고 한다')
#
# # tp = (1,2,3,4)
#
# my_fuc(1,2,3,4)

# def print_num(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# # print_num(10,20,30)
#
# x = [10,20,30]
# y = (10,20,30)
# print_num(*x)
# #print_num(y)

# def sum_many(*args): #arguments
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# result = sum_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

from statistics import mean, variance
from math import sqrt
dataset = [2, 4, 5, 6, 1, 8]
def Avg(data):
  avg = mean(data)
  return avg