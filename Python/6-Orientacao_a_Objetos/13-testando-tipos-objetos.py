# Testando tipos de objetos em Python

p1 = 5
p2 = 5.2

print(isinstance(p1, int))  # True
print(isinstance(p2, float))  # True
print(isinstance(p1, (int, float)))  # True

def soma(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
        return None
    
print(soma(p1, p2))
print(soma(p1, "texto"))  # None