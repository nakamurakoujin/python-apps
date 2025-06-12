import random
while True:
    random_number = random.randint(1,100)
    for i in range(5):
        input_line =  int(input(f"{i + 1}回目！ チャンスは残り{5 - i}回！："))

        if  input_line == random_number:
            print("おめでとう！正解です！")
            break
        elif input_line > random_number:
            if input_line < random_number + 10:
                print("答えより少し大きい")
            else:
                print("答えより大きい")
        else:
            if input_line > random_number - 10:
                print("答えより少し小さい")
            else:
                print("答えより小さい")
    if i == 4:
        print(f"正解は {random_number} でした!")
    a = input("もう一度挑戦しますか？　yes　no:")
    if a == "yes":
        continue
    else:
        break
    