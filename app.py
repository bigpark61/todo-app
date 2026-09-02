tasks = []

while True:
    print("\n1. 할 일 추가")
    print("2. 목록 보기")
    print("3. 할 일 삭제")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        task = input("할 일을 입력하세요: ")
        tasks.append(task)
        print("등록되었습니다.")

    elif choice == "2":
        print("\n할 일 목록")
        if not tasks:
            print("등록된 할 일이 없습니다.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("삭제할 할 일이 없습니다.")
            continue

        print("\n할 일 목록")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        try:
            delete_index = int(input("삭제할 번호를 입력하세요: "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if 1 <= delete_index <= len(tasks):
            removed_task = tasks.pop(delete_index - 1)
            print(f'"{removed_task}"를 삭제했습니다.')
        else:
            print("잘못된 번호입니다.")

    elif choice == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")