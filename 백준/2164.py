import collections # queue를 쓰기 위한 라이브러리
a = int(input()) # 입력 받기
n = collections.deque([i for i in range(1, a+1)]) #queue 초기화

while len(n) > 1: # queue안의 원소 갯수가 1일때 반복문 종료
    n.popleft()  # 왼쪽 요소를 제거해라
    n.rotate(-1) # 왼쪽으로 한바퀴 돌려라

print(*n)

# from collections import deque

# N = int(input())
# deque = deque([i for i in range(1, N+1)])

# while(len(deque) > 1):
#     deque.poplef()
#     move_num = deque.popleft()
#     deque.append(move_num)
# print(deque[0])
