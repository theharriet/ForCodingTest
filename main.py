# 그래프 탐색 알고리즘 : DFS/BFS
# 탐색(search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정.

#### 큐 자료구조 - 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출); 입구와 출구가 모두 뚫려 있는 터널과 같은 형태

# 리스트 자료형을 이용해 기능적으로 큐를 구현할수 있지만 시간복잡도가 더 높아 비효율적이므로 큐를 이용할땐 deque라이브러리 이용

#  deque라이브러리 - 스택과 큐의 장점을 합친 라이브러리

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 - deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 - deque([4, 1, 7, 3])

# 파이썬에서 단순히 리스트를 이용해 특정 인덱스에 위치하는 원소를 꺼내기 위해  pop()를 호출하게 되면 원소를 꺼낸뒤에 원소의 위치를 조정하는 과정이 필요하기 때문에 원소를 꺼내는 연산자체가 시간이 걸림 -> 그러므로 deque를 이용해라