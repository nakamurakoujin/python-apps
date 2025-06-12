import random
import time


def hansyasinkei():
    input("準備ができたらEnterキーを押してください...")
    wait_time = random.uniform(5, 15)
    print("!!!!!が表示されたらEnter!")
    time.sleep(wait_time)
    print("!!!!!")
    start_time = time.time()
    input()
    end_time = time.time()
    reaction_time = (end_time - start_time)
    reaction_time = float(format(reaction_time,'.4f'))
    print(f"あなたの反応時間は{reaction_time}秒です。")
    
    return reaction_time


maxtime = 10
while True:

    rt = hansyasinkei()
    if maxtime > rt:
        maxtime = rt
    a = input("もう一度やりますか？　Yes：NO:")
    if a == "Yes":
        continue
    else:
        print(f"あなたの最高タイムは{maxtime}秒です。さようなら")
        break