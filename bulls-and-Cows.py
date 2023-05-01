import random

def create_answer():
    return random.random()

if __name__ == "__main__":
    answer = create_answer()
    print(answer)