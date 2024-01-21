import editdistance


def match(text, word):
    '''使用编辑距离库进行匹配计算'''
    # max_distance = len(word) / 5
    # dist = editdistance.eval(text, word)
    # sim = 1 - (dist / len(word)) if dist < max_distance else 0

    # 节约时间所以直接改为判断拼音是否相等
    sim = 1 if text == word else 0
    return int(sim)


def is_match_GenshinImpact(text):
    word = ['yuan', 'shen', 'qi', 'dong']
    l = len(text)
    for i in range(0, l):
        if match(text[i], word[0]):
            for j in range(i + 1, l):
                if match(text[j], word[1]):
                    for k in range(j, l):
                        if match(text[k], word[2]):
                            for m in range(k, l):
                                if match(text[m], word[3]):
                                    return True
    return False

def is_match_StarRail(text):
    word = ['beng', 'xing', 'tie', 'qi', 'dong']
    l = len(text)
    for i in range(0, l):
        # 星铁启动/崩铁启动/星穹铁道启动/崩坏星穹铁道启动 都可以
        if match(text[i], word[0]) or match(text[i], word[1]):
            for j in range(i + 1, l):
                if match(text[j], word[2]):
                    for k in range(j, l):
                        if match(text[k], word[3]):
                            for m in range(k, l):
                                if match(text[m], word[4]):
                                    return True
    return False

if __name__ == '__main__':
    word = ['yuan', 'shen', 'qi', 'dong']
    text = ['ha', 'ha', 'yuan', 'shen', 'a', 'qi', 'dong']
    l = len(text)
    for i in range(0, l):
        if match(text[i], word[0]):
            for j in range(i + 1, l):
                if match(text[j], word[1]):
                    for k in range(j, l):
                        if match(text[k], word[2]):
                            for m in range(k, l):
                                if match(text[m], word[3]):
                                    print(True)

    print(match('yuan', "yuan"))
