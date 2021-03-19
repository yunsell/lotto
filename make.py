import random

def lotto():
    f = open('lotto.txt', 'a')
    num = input("횟수를 입력해주세요 : ")
    for i in range(0, int(num)):
        lotto = random.sample(range (1, 46), 6)
        print(lotto)
        f.write(str(lotto)+'\n')
    f.close()
lotto()