from game.upDown import playUpDown

while True:
    print("\n===== mini game =====")
    print("1. 업다운 게임")
    print("2. 가위바위보")
    print("3. 사칙연산 퀴즈")
    print("4. 로또 번호 맞추기")
    print("5. 주사위 홀짝 게임")
    print("6. 반응속도 게임 (GUI)")
    print("7. 갤러그 (GUI)")
    print("0. 종료")

    try:
        menu = int(input("메뉴 선택 : "))

        if menu == 1:
            playUpDown()
        elif menu == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("선택한 메뉴 기능은 준비 중입니다.")
    except ValueError:
        print("숫자를 입력해 주세요.")