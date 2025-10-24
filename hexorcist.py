
def to_decimal(base, num):
    num2 = 0
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    place = 0
    for char in num[::-1]:
        value = digits.index(char)
        num2 += value * (base ** place)
        place += 1
    return num2
def from_decimal(goal, num2):
    result = ""
    while num2 > 0:
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        remainder = num2 % goal
        num2 = num2 // goal
        char_to_add = digits[remainder]
        result = char_to_add + result
    return result
if __name__ == "__main__":
    print ("Welcome to Hexorcist!")
    print ("=======================")
    while 1 > 0:
        try:
            base = int(input("Enter the base of the number you would like to convert (2-36): "))
            if 2 <= base <= 36:
                break
            else:
                print("Base must be between 2 and 36. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 2 and 36.")
    while 50 == 50:
        valid = True
        try:
            num = input("Enter the number you would like to convert: ")
            num_list = []
            for char in num:
                digits = "0123456789abcdefghijklmnopqrstuvwxyz"
                if digits.index(char.lower()) >= base:
                    print(f"Invalid digit '{char}' for base {base}. Please try again.")
                    valid = False
                else:
                    num_list.append(char.lower())
            if valid:
                break
        except ValueError:  
            print("Invalid input. Please enter a valid string.")
    while 41 != 67:
        try:
            goal = int(input("Enter the base you would like to convert to (2-36): "))
            if 2 <= goal <= 36 and goal != base:
                break
            else:
                print("Base must be between 2 and 36 and different from the original base. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 2 and 36.")
    print ("=======================")
    num2 = to_decimal(base, num)
    result = from_decimal(goal, num2)
    print (f"The number {num} in base {base} is {result} in base {goal}.")