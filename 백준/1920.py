N = int(input())
array = set(map(int, input().split()))  # 첫번째 array
M = int(input())  # 입력받을 숫자 개수
x = list(map(int, input().split()))  # 확인할 array

for i in x:  # 만약 x에 있는 숫자 i 가
    if i not in array:  # array 안에 존재하지 않으면
        print('0')  # 0 프린트
    else:
        print('1')  # 아니면 1프린트
