X = int(input())

def pibo(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1

  
  return pibo(num-1) + pibo(num-2)
print(pibo(X))
