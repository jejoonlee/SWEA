# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

# [입력]
# 입력으로 정수 N 이 주어진다.


a = int(input())

for i in range(1, a + 1):
    if a % i == 0:         # 입력된 a값과, i 값들을 나눈 후, 나머지가 0이면
        print(i, end =' ') # i 값들을 출력해라