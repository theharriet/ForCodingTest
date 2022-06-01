# 그래프 탐색 알고리즘 : DFS/BFS
# 탐색(search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정.

#### 스택 자료구조 : 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조 - 입구와 출구가 동일한 형태; 박스 쌓았다 내리기; 삽입 & 삭제

stack = []

#  가장 오른쪽에 원소를 삽입하는 append()
#  가장 오른쪽에 있는 원소를 꺼내는 pop()

# 시간복잡도는 상수시간 O1?

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) -삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력 - 리스트에 담긴 원소를 거꾸로 뒤집어서(순서를) 출력
print(stack) # 최하단 원소부터 출력


