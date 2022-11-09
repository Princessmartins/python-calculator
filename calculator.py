#Calculator Software
run_again= "Yes"
while run_again == "Yes":
    print("Welcome to Calculator App")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    operator = input("Enter operator (+-*/): " )

    if num1.isnumeric():
        if num2.isnumeric():
            num1=int(num1)
            num2=int(num2)

            if operator=="+":
                print(num1+num2)
            elif operator=="-":
                print(num1 - num2)
            elif operator=="*":
                print(num1 * num2)
            elif operator=="/":
                if num2 == 0:
                    print("Cannot be divided by zero!")
                else:
                    print(num1 / num2)
            else:
                print("Invalid operator!")

        else:
            print("Please enter numbers only")
    else:
        print("Please enter numbers only")

    run_again=input ("Enter Yes to do another calculation: ")
    if run_again != "Yes":
        print("Bye!")




    