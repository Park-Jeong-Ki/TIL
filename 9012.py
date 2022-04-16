import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    stack = []  # stack 초기화
    p_str = sys.stdin.readline().rstrip() #괄호 문자열 입력
    for j in p_str:
        if j == '(':
            stack.append(j) # stack push
        elif j == ')':
            if stack: # 스택에 괄호가 있는 경우
                stack.pop() # stack pop
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
