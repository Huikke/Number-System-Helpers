def other_system_to_decimal(number: str, system: int) -> str:
    value = 0
    multiplier = len(number) - 1

    for i in number:
        if i == "A":
            i = "11"
        elif i == "B":
            i = "12"
        elif i == "C":
            i = "13"
        elif i == "D":
            i = "14"
        elif i == "E":
            i = "15"
        elif i == "F":
            i = "16"
        
        value += int(i) * system ** multiplier
        multiplier -= 1

    return value


base_system = int(input("Base system: "))
value = input("Input value: ")

print("Decimal value:", other_system_to_decimal(value, base_system))