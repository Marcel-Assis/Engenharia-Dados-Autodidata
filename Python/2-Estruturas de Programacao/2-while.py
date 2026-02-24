# Estrutura while:
num = 0
while num < 5:
    print("Número:", num)
    num += 1

# Uso de break e continue:
num = 0
while num < 6:
    num += 1
    if num == 3:
        continue # Pula a iteração quando num é 3
    if num == 5:
        break # Encerra o loop quando num é 5
    print("Número:", num)