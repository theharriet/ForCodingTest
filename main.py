########## 구현 : 시뮬레이션과 완전 탐색
#  구현이란? 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정.
#  코딩테스트에서 구현 유형의 문제는 -> 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제.
  # ex. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제. - 사용하는 프로그램에 따라서 달라질수 있음(자바: 클래스도 만들고 별도의 인터페이스를 상속받아 구현해야하는 문제를 파이썬에서는 기본적으로 제공되는 자료형과 내장 함수만을 이용해서 간단히 구현가능 )
      # 실수 연산을 다루고, 특정 소수점 자리까지 출력해야하는 문제.
      # 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제.
      # 적절한 라이브러리를 찾아서 사용해야하는 문제. (모든순열과 조합문제..but, 파이썬에선 이터툴스 라이브러리이용하면 간결하게 해결 가능)

# 구현(Implementation)
#   - 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용 (2D 게임만들 때)
# ex) 2차원 맵에 한 좌표에 존재하는 캐릭터가 반복적으로 어떤 위치로 이동한다 -와 같은 문제를 해결할때

# 행렬이란 - 2차원 데이터를 표와 같은 형태로 쉽게 나타내주는 수학적 개념. 2차원 배열, 2차원 list(파이썬)와 동일

# 시뮬레이션 및 완전 탐색 문제에서는 2치원 공간에서의 방향 벡터가 자주 활용됨

### 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# wjdcjrl gkqrur

