import random


def playRPS():
    print("\n***** 가위바위보 *****")
    print("1. 가위  2. 바위  3. 보")

    rps_map = {1: "가위", 2: "바위", 3: "보"}

    try:
        user_choice = int(input("선택 (1~3) : "))
        if user_choice not in [1, 2, 3]:
            print("1, 2, 3 중에서 선택해 주세요.")
            return

        com_choice = random.randint(1, 3)
        print(f"나 : {rps_map[user_choice]} / 컴퓨터 : {rps_map[com_choice]}")

        if user_choice == com_choice:
            print("무승부")
        elif (user_choice == 1 and com_choice == 3) or \
                (user_choice == 2 and com_choice == 1) or \
                (user_choice == 3 and com_choice == 2):
            print("승리")
        else:
            print("패배")
    except ValueError:
        print("숫자를 입력해 주세요.")