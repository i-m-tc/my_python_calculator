import Module as mp
while True:
    res=input("Enter S to stop the programme or continue it by clicking any key:-->").strip().upper()
    if res != 'S':

        operator=input("Check the following operators:\n + for addition\n - for substraction\n* for Multiplication\n/ for division:")
        if operator=='+':
            mp.addition()
        elif operator=='-':
            mp.subtraction()
        elif operator=='*':
            mp.multiplication()
        elif operator=='/':
            mp.division()
        else:
            print("Choose your operator correctly!!")
    else:
        print("You have exit from the programme")
        break
