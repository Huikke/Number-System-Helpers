decimal = int(input("Decimal value: "))
remainder_memory = ""


while decimal != 0:
    decimal, remainder = divmod(decimal, 2)
    remainder_memory += str(remainder)
binary = remainder_memory[::-1] # Reverse String

print("Binary value:", binary.zfill(10))