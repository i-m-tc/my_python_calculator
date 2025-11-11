Calculator program using python
while True:
    res=input("Enter S to discontinue or click any key to continue:").strip().upper()
    if res!='S':
        operator=input("Choose an operator, \n + to addition,\n - to do subtraction, \n * to do multiplication, \n / to do divisions")
        if operator=='+':
            numbers=input("Enter the numbers separated with a comma:").strip()
            split_numbers=numbers.split(",")
            final_number=[float(i) for i in split_numbers]
            print(f"Your numbers for addition is:{final_number}=",sum(final_number))
        elif operator=='-':
            numbers=input("Enter two numbers separated with a comma:").strip()
            split_numbers=numbers.split(",")
            print(split_numbers)
            final_number=[float(i) for i in split_numbers]
            if final_number[0]>final_number[1]:
                result=final_number[0]-final_number[1]
                print(f"subtraction is:{result}")
            elif final_number[0]<final_number[1]:
                result=final_number[1]-final_number[0]
                print(f"subtraction is:{result}")
            else:
                print("Result is 0")
        elif operator=='*':
            numbers=input("Enter the numbers separated with a comma:").strip()
            split_numbers=numbers.split(",")
            final_number=[int(i) for i in split_numbers]
            result=1
            for i in final_number:
                result=result*i
            print(f"your multiplication result is: {result}")
        elif operator=='/':
            numbers=input("Enter two numbers separated with a comma:").strip()
            split_numbers=numbers.split(",")
            final_number=[int(i) for i in split_numbers]
            if final_number[0]==0 or final_number[1]==0:
                print("Not defined")
            else:
                 result=final_number[1]/final_number[0]
                 print(f"your division result is:{result}")
        else:
            print("Incorrect!! Click the correct operator")
    else:
        break
