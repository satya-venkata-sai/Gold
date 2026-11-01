def add(a, b):
    return a + b
def sub(a,b):
    return a-b

a,b = list(map(int, input("Enter two numbers: ").split()))
print("Sum:", add(a, b))
print("Difference:", sub(a, b))