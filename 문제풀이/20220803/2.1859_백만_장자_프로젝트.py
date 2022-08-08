import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())

# for t in range(1, T + 1):
#     day = int(input())
#     cost = list(map(int, input().split()))
    
#     buy = []
#     sell = 0
#     for i in range(len(cost) - 1):
#         if cost[i] <= cost[i + 1]:
#             buy.append(cost[i])
#         elif cost[i] > cost[i + 1]:
#             if len(buy) != 0:
#                 sell += (len(buy) * cost[i]) - sum(buy)
#                 buy =[]
#             else:
#                 continue

#     if len(buy) == 0:
#        print(f'#{t} {sell}')
#        continue
#     elif cost[-1] > buy[-1]:
#         sell += (len(buy) * cost[-1]) - sum(buy)
    
#     print(f'#{t} {sell}')

# 뒤에서부터 비교를 시작한다
# 만약 맨 뒤에 수가 앞에 수보다 크거나 같으면, 뒤에 수와 앞의 수를 빼서 이익을 구한다
# 반대로 뒤의 수가 앞의 수보다 작으면, 제일 큰 값을 앞의 수로 바꿔준다