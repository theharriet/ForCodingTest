# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

# 중복 순열
from itertools import product

data = ['A', 'B', 'C'] #데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] #데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

###### Counter
## 등장 횟수를 세는 기능. (collections 라이브러리)
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 각각의 원소가 몇번씩 등장했는지 사전 자료형으로 반환

##### 최대 공약수와 최소 공배수
#### math 라이브러리의 gcd(), lcm()

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
  return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산