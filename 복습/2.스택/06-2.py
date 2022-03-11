#06-2 스택에서 데이터 3개 추철
stack = ["coffee", "greentea", "honey", None, None]
top = 2

print("------stackstatue-------")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

print("------------------------")
data = stack[top]
stack[top] = None
top -= 1
print("pop --->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop-->", data)
print("-----------------------")

print("------stackstatue-------")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

