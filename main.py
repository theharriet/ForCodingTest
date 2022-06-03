# 그래프 탐색 알고리즘 : DFS/BFS
# 탐색(search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정.

# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수
#  - DFS를 실질적으로 구현할 때 자주 사용 됨.  

# 팩토리얼 구현 예제
# n! = 1 * 2 * 3 * ... * (n-1) * n
#  0!과 1!의 값은 1

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))