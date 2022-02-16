# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

# i = 1
# result = 0

# # 1 ~ 9 까지의 합
# # while i <=9: 
# #     result += i
# #     i += 1

# # 1 ~ 9 까지 홀수의 합
# while i <= 9:
#     if i%2 == 1:
#         result += i
#     i += 1

# print(result)

# array = [9, 8, 7, 6, 5]
# # array = (9, 8, 7, 6, 5) 튜플도 가능

# for x in array:
#     print(x)


# range(시작 값, 끝 값 + 1) / 인자를 하나만 넣으면 자동으로 시작 값은 0 / for문에서 연속적인 값을 차례대로 순회할 때 주로 사용

# result = 0

# # i는 1부터 9까지의 모든 값을 순회
# for i in range(1, 10):
#     result += i

# print(result)


#### continue : 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때

# 1~9까지 홀수의 합
# result = 0

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

  # line 42 ~ 48 과 line 14 ~ 20은 똑같은 결과.


############## ex1
# scores = [90, 85, 77, 65, 97]

# for i in range(5):
#     if scores[i] >= 80:
#         print(i+1, "번 학생은 합격입니다.")

############## ex2
# scores = [90, 85, 77, 65, 97]
# cheating_student_list = {2, 4}

# for i in range(5):
#     if i + 1 in cheating_student_list:
#         continue
#     if scores[i] >= 80:
#         print(i+1, "번 학생은 합격입니다.")

#################구구단 : 중첩된 반복문

for i in range(2, 10):
    for j in range(1, 10):
        print (i, "X", j, "=", i * j)
    print()
