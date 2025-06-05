# 1.ランダムな数字を生成して出力するプログラム
# 2.入力された文字列もそのまま出力
# 3.数字が合っているか判定します
# 4.5回まで入力を受け付けるプログラム
# 5.正解したら終了
import random


random_number = random.randint(1, 100)
input_line = input("1~100までの数字を当ててください")
print(random_number)
print("入力された文字列:", input_line)
if random_number == int(input_line):
    print("正解です！")
else:
    print("不正解です。正しい数字は", random_number, "でした。")

    
