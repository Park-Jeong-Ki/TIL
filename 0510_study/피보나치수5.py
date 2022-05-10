N = int(input()) # N을 입력받습니다

def pibo(num): # 피보나치수 사용자 정의 함수
  if num == 0: # 재귀함수 종료조건 N = 0 일때 피보나치 값 0
    return 0
  elif num == 1: # 재귀함수 종료조건 N = 1 일때 값 1
    return 1

  return pibo(num-1) + pibo(num-2) # 피보나치(5) = 피보나치(4) + 피보나치(3) 즉 n번째 피보나치수는 피보나치(n-1)+피보나치(n-2)
print(pibo(N))
