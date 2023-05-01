import * from bnc_print
import * from bnc_input
import * from bnc_match
import * from bnc_create

if __name__ == '__main__':
    answer = create_answer()
    inp = bnc_input()
    bNc = match(answer,inp)
    print_result(bNc)