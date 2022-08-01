from Sign_and_Magnitude import sign_and_magnitude

def excess_code(number: str, length: int) -> str:
    value = sign_and_magnitude(number, length, 3)

    return value



if __name__ == "__main__":
    code = int(input("Excess code: "))
    
    length = 0
    while code != 1:
        code = code / 2
        length += 1
    
    decimal = input("Decimal value: ")

    print("Binary value: " + excess_code(decimal, length))