# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

#  global : 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 여러개의 반환값

def operator(a, b) :
    return a + b, a - b, a * b, a / b

a, b, c, d = operator(3, 7)
print(a, b, c, d)


###### 람다 함수

print((lambda a, b: a + b)(3, 5)) # 이 함수가 여러번 쓰이지 않고 해당줄에서 한번 쓰이고 말때 이런식으로 간단하게 쓸수있음

#원래는 이런식
def add(a, b):
    return a + b
print(add(4,5))

## 함수 자체를 입력으로 받는 함수 쓸때 주로 쓰임

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key)) # key 속성의 값으로 정렬기준을 넣어줄수 있음(나이로 정렬)

print(sorted(array, key=lambda x: x[1]))

#  다른 예시: 여러개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2) 
      # map => 각 원소에 어떤 함수를 적용할지를 설정

print(list(result))

# https://www.youtube.com/watch?v=Lytj_xcw8mE&list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N&index=1
# 2:04:07