import random


def playUpDown():
    print("\n***** UP DOWN *****")
    target = random.randint(1, 100)

    while True:
        try:
            guess = int(input("숫자 : "))
            if guess < target:
                print("UP")
            elif guess > target:
                print("DOWN")
            else:
                print("correct !!!")
                break
        except ValueError:
            print("숫자를 올바르게 입력해 주세요.")