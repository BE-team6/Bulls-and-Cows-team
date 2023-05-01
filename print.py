def print_result(bulls: int, cows: int):
    if bulls == 4:
        print("it's correct")
    else:
        print("bulls: "+ str(bulls))
        print("cows: "+str(cows))

if __name__ == '__main__':
    print_result(4, 4)
