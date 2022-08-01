def decimal_to_other_system(number: str, system: int) -> str:
    remainder_memory = ""
    number = int(number)
    
    while number != 0:
        number, remainder = divmod(number, system)

        if remainder == 11:
            remainder = "A"
        elif remainder == 12:
            remainder = "B"
        elif remainder == 13:
            remainder = "C"
        elif remainder == 14:
            remainder = "D"
        elif remainder == 15:
            remainder = "E"
        elif remainder == 16:
            remainder = "F"

        remainder_memory += str(remainder)
    value = remainder_memory[::-1] # Reverse String

    return value

def float_change(number: str, system: int) -> str:
    number = float(number)
    value = ""
    max_decimals = 10

    while number != 0 and max_decimals != 0:
        number *= system
        value += str(int(number)) # Abuse the fact int kills float
        number -= int(number)
        max_decimals -= 1

        if max_decimals == 0:
            value += "..."

    return value
        

if __name__ == "__main__":
    base_system = int(input("Base system: "))
    decimal = input("Decimal value: ")

    if "." in decimal:
        list = decimal.split(".")
        decimal = list[0]
        float_this = "0." + list[1]

        float_value = float_change(float_this, base_system)
        value = decimal_to_other_system(decimal, base_system)
        print("Output value:", value + "." + float_value)
    else:
        value = decimal_to_other_system(decimal, base_system)
        print("Output value:", value)
