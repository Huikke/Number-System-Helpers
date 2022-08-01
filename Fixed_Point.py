from Complement_of_two import complement_of_two
from Decimal_to_Other import float_change

def fixed_point(value: str, i_length: int, f_length: int) -> str:
    list = value.split(".")
    decimal = list[0]
    float_this = "0." + list[1]

    if "-" in decimal and float(float_this) != 0: # Make negative number one bigger & reverse float
        decimal = str(int(decimal) - 1)
        float_this = str(1 - float(float_this))
        
    
    integer_value = complement_of_two(decimal, i_length)
    
    float_value = float_change(float_this, 2)
    while len(float_value) < f_length: # Add zeroes
        float_value += "0"
    
    return integer_value + "." + float_value



integer_length = int(input("Bit length (Integer with Sign): ")) - 1
float_length = int(input("Bit length (Float): "))
value = input("Decimal value: ")

print("Binary value:", fixed_point(value, integer_length, float_length))