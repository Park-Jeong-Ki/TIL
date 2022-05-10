
N = int(input()) # 정수 N을 입력 받는디ㅏ.

def factorial(num): # 사용자 정의 함수를 이용하여 factorial 함수 선언

  if num ==0: # 재귀 함수 종료 조건 0! = 1
    return 1
  elif num == 1: # 재귀 함수 종료 조건 1! = 1
    return 1

  return num * factorial(num-1) # N! = N * (N-1)!

print(factorial(N))
