#06-1 크기가 5칸인 스택의 생성과 데이터 3개 입력

stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커피"
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

print("-----stack statue-----")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])
