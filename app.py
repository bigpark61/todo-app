tasks = []

while True:
    print("\n1. 할 일 추가")
    print("2. 목록 보기")
    print("3. 종료")

    choice = input("선택: ")

    if choice == "1":
        task = input("할 일을 입력하세요: ")
        tasks.append(task)
        print("등록되었습니다.")

    elif choice == "2":
        print("\n할 일 목록")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")