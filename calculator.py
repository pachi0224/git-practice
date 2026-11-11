
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print(add(10, 5))
print(subtract(10, 5))

def multiply(a, b):
    return a * b

print(multiply(10, 5))

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

print(divide(10, 5))
