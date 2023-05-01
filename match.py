def bull(ans:int,inp:int):
    if ans == inp:
        return True
    else :
        return False

def cow(ans:list,inp:int):
    if inp in ans:
        return True
    else:
        return False

def match(ans_list:list,inp_list:list):
    bNc = [0,0] # [bulls, cows]
    for i in range(0,4):
        if(bull(ans_list[i],inp_list[i])):
            bNc[0] += 1
        elif(cow(ans_list,inp_list[i])):
            bNc[1] += 1
        else:
            continue
    return bNc