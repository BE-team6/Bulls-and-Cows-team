def print_result(results):
    bulls = results[0]
    cows = results[1]
    if bulls == 4:
        print("it's correct")
    else:
        print("bulls: "+ str(bulls))
        print("cows: "+str(cows))

if __name__ == '__main__':
    print_result([4, 4])
