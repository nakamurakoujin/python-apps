import random
import time

recipes = {
    "カレー": ["材料を切る", "炒める", "水を加える", "煮込む", "盛り付ける"],
    "オムライス": ["ご飯を炊く", "具を炒める", "卵を焼く", "包む", "盛り付ける"],
    "ラーメン": [
        "スープを作る",
        "麺を茹でる",
        "チャーシューを準備",
        "具材を盛り付ける",
        "仕上げる",
    ],
    "餃子": ["具を刻む", "混ぜる", "皮で包む", "焼く", "盛り付ける"],
    "天ぷら": ["材料を切る", "衣を作る", "衣をつける", "揚げる", "盛り付ける"],
    "味噌汁": ["出汁を取る", "具を切る", "具を入れる", "味噌を溶く", "盛り付ける"],
    "パスタ": ["お湯を沸かす", "麺を茹でる", "ソースを作る", "和える", "盛り付ける"],
    "焼きそば": [
        "麺をほぐす",
        "野菜を切る",
        "具材を炒める",
        "麺と混ぜる",
        "ソースで味付け",
    ],
    "たこ焼き": [
        "生地を作る",
        "具を準備する",
        "生地を流す",
        "焼いてひっくり返す",
        "ソースをかける",
    ],
    "ハンバーガー": [
        "パティをこねる",
        "パティを焼く",
        "バンズを焼く",
        "具材を挟む",
        "盛り付ける",
    ],
    "りんごタルト": [
        "りんごを切る",
        "タルト生地を作る",
        "タルト型に詰める",
        "オーブンで焼く",
        "冷まして仕上げる",
    ],
    "麻婆豆腐": [
        "材料を切る",
        "ひき肉を炒める",
        "調味料を加える",
        "豆腐を入れて煮る",
        "仕上げにとろみをつける",
    ],
    "ピザ": [
        "生地を作る",
        "具材を切る",
        "生地に具材をのせる",
        "オーブンで焼く",
        "仕上げにバジルをのせる",
    ],
    "グラタン": [
        "具材を切る",
        "具材を炒める",
        "ホワイトソースを作る",
        "チーズをのせる",
        "オーブンで焼く",
    ],
    "チキンカツ": [
        "鶏肉を叩く",
        "衣をつける",
        "油で揚げる",
        "切り分ける",
        "盛り付ける",
    ],
}


selected_dish = None  # 最初は料理未選択

while True:
    # 新しい料理を選ぶ必要があるときだけ選ぶ
    if selected_dish is None:
        selected_dish = random.choice(list(recipes.keys()))
    correct_steps = recipes[selected_dish]
    shuffled_steps = correct_steps[:]
    random.shuffle(shuffled_steps)

    print(f"正しい手順に並び替えてください！\n🍳 料理は「{selected_dish}」です。")
    print("手順一覧（順不同）：")
    for i, step in enumerate(shuffled_steps, start=1):
        print(f"{i}. {step}")

    start_time = time.time()
    limit = 200
    user_order = []
    score = 0

    while len(user_order) < len(correct_steps):
        elapsed = time.time() - start_time
        remaining = limit - elapsed
        if remaining <= 0:
            print("\n時間切れ！ゲームオーバーです。")
            break

        print(f"\n残り時間: {int(remaining)}秒")
        print(f"現在の手順：{len(user_order) + 1} / {len(correct_steps)}")
        choice = input(
            f"上から何番目の手順を選びますか？（1〜{len(shuffled_steps)}）: "
        )

        if not choice.isdigit():
            print("数字を入力してください。")
            continue

        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(shuffled_steps):
            print("範囲内の数字を入力してください。")
            continue

        selected_step = shuffled_steps[choice_num - 1]
        user_order.append(selected_step)

        if correct_steps[len(user_order) - 1] == selected_step:
            score += 1
            print("正しい手順です！")
        else:
            print("順番が違います。")

    if len(user_order) == len(correct_steps):
        accuracy = (score / len(correct_steps)) * 100
        print(f"\n🎉 ゲーム終了！正解率: {accuracy:.1f}%")

        print("\n✅ 正しい手順は：")
        for i, step in enumerate(correct_steps, start=1):
            print(f"{i}. {step}")

    # もう一度やるかを選ばせる
    while True:
        print("\nもう一度やりますか？")
        print("1. 同じ料理でもう一度")
        print("2. 別の料理でやる")
        print("3. やめる")
        retry = input("→ 数字で選んでください（1〜3）: ")

        if retry == "1":
            break  # 同じ料理で再開（selected_dishはそのまま）
        elif retry == "2":
            selected_dish = None  # 別の料理にする
            break
        elif retry == "3":
            print("ゲームを終了します。お疲れさまでした！")
            exit()
        else:
            print("1〜3の数字を入力してください。")
