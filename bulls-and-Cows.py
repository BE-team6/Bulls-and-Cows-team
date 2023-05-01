import random

def create_answer():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return random.sample(num, 4)

if __name__ == "__main__":
    answer = create_answer()
    print(answer)