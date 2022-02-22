# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

####실전에서 유용함 표준 라이브러리
# 내장함수 : import 없이 제공하는 기본 함수들. pring(), input() ...
# itertools : 파이썬에서 반복되는 형태의 데티어를 처리하기 위한 기능 제공. 특히 순열과 조합 라이브러리는 코테에서 자주 사용 (모든 경우의수 고려)
# heapq : 힙 자료구조 제공. 우선순위 큐 키능을 구현할때. 다이스트?와 같은 최단경로 알고리즘에서 많이 활용
# bisect : 이진 탐색(Binary Search) 기능 제공
# collections : deque덱, counter카운터 등의 자료구조를 포함
# math : 수학적 기능. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, pi와 같은 상수 포함


#sum()
result = sum([1, 2, 3, 4, 5])
print(result)

#min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)

#eval() - 계산 결과 값 반환
result = eval("(3+5)*7")
print(result)

# sorted() : 주로 list와 같은 반복 가능한 객체가 들어왔을때 각 원소를 정렬한 결과 반환
# 람다함수를 이용하여 키속성으로 정렬 기준을 넣어줄수있음
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)


# 순열 & 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
#      - {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우 : 'ABC', 'ACB', "BAC", 'BCA', 'CAB', 'CBA'
#      - 순열의 수 : nPr = n*(n-1)*(n-2)*...*(n-r+1)           permutation
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기 ()
print(result)


# 조합 : 서로 다른  순서에 상관 없이 서로 다른 r개를 선택하는 것 
#      - {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB', 'AC', 'BC'
#       - 조합의 수 : nCr = {n*(n-1)*(n-2)*...*(n-r+1)}/r!     combination
#  공식에 따라 순열의 수를 구해보았을 때 경우의 수가 천만, 1억 단위가 넘어가는 경우, 완전탐색을 이용했을 때 시간초과 판정을 받을 수 있기 때문에 실제 전체 경우의 수를 고려할 때 사용


from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

