import re
import zhconv
from pypinyin import lazy_pinyin, TONE3


def process_words(text):
    text = zhconv.convert(text, 'zh-cn')  # 转化成简体
    # print(text)

    pinyin = ''.join(lazy_pinyin(text, style=TONE3))  # 转化成拼音
    # print(pinyin)                                     # pinyin = "yuan2shen2qi3dong4"

    li = re.split(r'[1-4\s]+', pinyin)  # 将每个字的拼音分开

    # 对于re.split()在li的最后产生的空格，可以切片切掉或者filter筛选（filter(判断函数function, 可迭代对象iterable)）
    # li = li[:-1]
    li = list(filter(lambda x: x != '', li))
    # print(li)
    return li


if __name__ == '__main__':
    print(process_words("原神启动"))
