from Decimal_to_Other import decimal_to_other_system

def sign_and_magnitude(number: str, length: int, mode=0) -> str: # mode decide what mechanism function uses

    if int(number) < 0 or number == "-0":
        sign = "1"
        number = abs(int(number))
    else:
        sign = "0"
        number = int(number)

    magnitude = decimal_to_other_system(number, 2)
    
    while len(magnitude) < length:
        magnitude = "0" + magnitude
    
    if sign == "1" and (mode == 1 or mode == 2 or mode == 3): # for Complements
        magnitude = magnitude.replace("0", "?")
        magnitude = magnitude.replace("1", "0")
        magnitude = magnitude.replace("?", "1")

        if mode == 2 or mode == 3: # for Complements of two
            i = 1
            while True:
                if "0" not in magnitude: # checks for -0
                    magnitude = "0" * len(magnitude)
                    sign = "0"
                    break
                elif "0" not in magnitude[1:]: # checks for the last negative number
                    magnitude = "0" * (len(magnitude) - 1)
                    break
                elif magnitude[-i] == "0":
                    magnitude = magnitude[0:-i] + "1" + "0" * (i - 1)
                    break
                elif magnitude[-i] == "1":
                    i += 1

    if mode == 3: # for Excess Code
        if sign == "0":
            sign = "1"
        elif sign == "1":
            sign = "0"

    if len(magnitude) > length: # Error Check
        return "Error"

    value = sign + magnitude

    return value


if __name__ == "__main__":
    bit_length = int(input("Bit length without sign: "))
    decimal = input("Decimal value: ")

    print("Binary value: " + sign_and_magnitude(decimal, bit_length))