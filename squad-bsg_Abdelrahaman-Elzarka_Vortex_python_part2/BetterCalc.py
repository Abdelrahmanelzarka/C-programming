def calc(number1,number2,operator):
    if operator =="+":
        print(number1+number2)
    elif operator =="-":
     print(number1-number2)
    elif operator =="*":
        print(number1*number2)    
    elif operator =="/":
        if number2==0:
            print("INVALID") 
        else:   
            print(number1/number2)    
    else:
        print("INVALID OPERATOR")



number1=float(input("Enter the first number: "))
operator=input("Enter the operator: ")
number2=float(input("Enter the second number: "))

calc(number1,number2,operator)      