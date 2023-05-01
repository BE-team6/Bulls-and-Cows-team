def getUserInput():
    print("=================================================")
    print("You have to guess the correct number !")
    print("The answer code is 4-digit number with different number in each digit\n")
    print("=================================================")
    length = False
    diff_digit = False
    while not (length & diff_digit):
        if not length:
            print("You have to Enter 4-digit number!")
        if not diff_digit:
            print("You have to enter different number in each digit!")
        
        input_num = input("Guess the number : ")
        length = (len(input_num) == 4)
        if not length : 
            diff_digit = True
            continue
        
        numlist = list(map(int, input_num))
        diff_digit = (len(set(numlist)) == 4)

    # For checking
    # print("You entered proper input code :", input_num)

getUserInput()

