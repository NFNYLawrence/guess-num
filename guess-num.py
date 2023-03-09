# 產生一個隨機整數1~100, (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話, 要告訴他: 比答案大或小
import random
r = random.randint(1, 100)
print(r)
while True:
    num = input('整數1~100, 請猜一個數字, 我會告訴你對不對: ')
    num = int(num)
    if num == r:
        print('猜對了')
        break
    elif num > r:
        print('比答案大')
    elif num < r: 
        print('比答案小')