import json
from collections import Counter

def check():
    f = open('lotto.txt', 'r')
    lines = f.readlines()
    lotto_list = []

    for line in lines:
        lotto = json.loads(line.replace('\n', ''))
        for i in lotto:
            lotto_list.append(i)
            count = Counter(lotto_list)

    print('총',len(lines),'개의 번호를 분석했습니다.')
    print('*'*15)
    for k,v in count.most_common(n=6):
        print(k, '==>', v, '번')
    print('*'*15)

    # r = open('result.txt', 'a')
    # r.write(str(count))
    # r.close()
check()