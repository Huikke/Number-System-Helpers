from Sign_and_Magnitude import sign_and_magnitude

def complement_of_two(number: str, length: int) -> str:
    value = sign_and_magnitude(number, length, 2)

    return value



if __name__ == "__main__":
    bit_length = int(input("Bit length without sign: "))
    decimal = input("Decimal value: ")

    print("Binary value: " + complement_of_two(decimal, bit_length))