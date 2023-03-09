import random
start =input('請輸入隨機數字範圍開始值: ')
end = input('請輸入隨機數字範圍結束值: ')
start =int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜一個數字, 我會告訴你對不對: ')
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