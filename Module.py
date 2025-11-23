def addition():
    numbers = input("Enter the numbers separated with a comma:").strip()
    print(numbers)
    split_numbers = numbers.split(",")
    final_numbers = [float(i) for i in split_numbers]
    print(f"Your numbers for addition is:{final_numbers}=", sum(final_numbers))
def subtraction():
    numbers = input("Enter only two numbers separated with a comma:").strip()
    split_numbers = numbers.split(",")
    final_numbers = [float(i) for i in split_numbers]
    if final_numbers[1] > final_numbers[0]:
        result = final_numbers[1] - final_numbers[0]
    else:
        result = final_numbers[0] - final_numbers[1]
    print(f"The substraction of {final_numbers}:", result)
def multiplication():
    numbers = input("Enter the numbers separated with a comma:").strip()
    split_numbers = numbers.split(",")
    final_numbers = [float(i) for i in split_numbers]
    result = 1
    for i in final_numbers:
        result = result * i
    print(f"Your multiplication result of {final_numbers}=", result)
def division():
    numbers = input("Enter two numbers separated with a comma:").strip()
    split_numbers = numbers.split(",")
    final_numbers = [int(i) for i in split_numbers]
    if final_numbers[0] == 0:
        print("Division cannot start with zero. Please enter a non-zero first number.")
    else:
        result = final_numbers[0]
        for i in final_numbers[1:]:
            if i == 0:
                print("Cannot divide by zero! .")
                break
            result /= i
        else:
            print(result)