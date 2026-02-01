def calculator():
    num1 = float(input("what is the first number: "))
    num2 = float(input("what is the second number: "))
    operator = input("What is the operator: ")
    if operator == "+":
        result = num1+num2
    else:
        if operator in ("x", "*"):
            result = num1*num2
        else:
            if operator == "-":
                result = num1-num2
            else:
                if operator == "/":
                    result = num1 / num2
    
    if result - int(result) == 0:
        result = int(result)
    return(result)


print(calculator())
