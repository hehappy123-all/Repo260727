import random


def playLotto():
    print("\n***** 로또 번호 맞추기 *****")
    user_numbers = []

    for i in range(1, 7):
        while True:
            try:
                num = int(input(f"{i}번째 번호 : "))
                if 1 <= num <= 45 and num not in user_numbers:
                    user_numbers.append(num)
                    break
                else:
                    print("1~45 사이의 중복되지 않는 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력해 주세요.")

    user_numbers.sort()
    winning_numbers = sorted(random.sample(range(1, 46), 6))
    matched_count = len(set(user_numbers) & set(winning_numbers))

    if matched_count == 6:
        result = "1등"
    elif matched_count == 5:
        result = "2등"
    elif matched_count == 4:
        result = "3등"
    else:
        result = "꽝"

    print(f"\n당첨 번호 : {winning_numbers}")
    print(f"내 번호   : {user_numbers}")
    print(f"{matched_count}개 일치 -> {result}")