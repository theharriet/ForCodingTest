# 그래프 탐색 알고리즘 : DFS/BFS
# 탐색(search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정.

# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수
#  - DFS를 실질적으로 구현할 때 자주 사용 됨.  

# 단순한 형태의 재귀 함수 예제
#  - '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력.
#  - 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력.
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()