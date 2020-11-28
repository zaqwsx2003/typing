import random
import time
import hgtk
import os

WORD_LIST = [
   "나는 배고픈 강아지 입니다.",
   "나는 배고픈 고양이 입니다.",
   "나는 배고픈 곰돌이 입니다.",
]

random.shuffle(WORD_LIST)
list_len = len(WORD_LIST)
current_count = 0

while current_count < list_len:
    os.system("cls")
    q = WORD_LIST[current_count]
    current_count += 1

    start_time = time.time()
    user_input = input(q + '\n')
    end_time = time.time() - start_time

    src = hgtk.text.decompose(q).replace("ᴥ", "")
    tar = hgtk.text.decompose(user_input).replace("ᴥ", "")

    correct = 0
    for i, c in enumerate(src, start=0):
        try:
            if tar[i] == c:
                correct += 1
        except:
            pass
    
    src_len = len(src)
    c = correct / src_len * 100 # 정확도
    e = (src_len - correct) / src_len * 100 # 오타율
    speed = float(correct / end_time) * 60
    
    print("속도: {:0.2f} 정확도: {:0.2f} % 오타율: {:0.2f} %".format(speed, c, e))
    os.system("pause")
