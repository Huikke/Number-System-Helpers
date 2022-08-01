binary = input("Binary value: ")
decimal = 0
multiplier = len(binary) - 1


for i in binary:
    decimal += int(i) * 2 ** multiplier
    multiplier -= 1

print("Decimal value:", decimal)