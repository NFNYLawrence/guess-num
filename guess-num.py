import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('整數1~100, 請猜一個數字, 我會告訴你對不對: ')
    num = int(num)
    if num == r:
        if count == 1: 
            print('猜對了')
        else:
            print('終於猜對了')
            print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r: 
        print('比答案小')
    print('這是你猜的第', count, '次')