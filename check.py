import json, collections

def check():
    f = open('lotto.txt', 'r')
    lines = f.readlines()
    lotto_list = [[], [], [], [], [], []]

    for line in lines:
        lotto = json.loads(line.replace('\n', ''))
        for i in range(0, 6):
            lotto_list[i].append(lotto[i])

    for i in lotto_list:
        rr = collections.Counter(i)
        print(rr.most_common(5))
        # r = open('result.txt', 'a')
        # r.write('\n'+str(rr.most_common(5)))
        # r.close()
check()