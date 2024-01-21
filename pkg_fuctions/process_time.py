from datetime import *
from pkg_fuctions.time_translate import time_translate


def process_time(gametime = "logs/game_time.txt", gametimetotal = "logs/game_time_total.txt"):
    """将gametime中的记录统计到gametimetotal里"""
    t = []
    total_time = 0
    month_time = 0
    last_time = 0
    the_month = datetime.now()
    with open(gametime, mode='r', encoding='utf-8') as f:
        li = f.readlines()
        # print(li)
        for i in li:
            i = i[:-1]  # 去除结尾的\n
            datetime1 = datetime.strptime(i, "%Y-%m-%d|%H:%M:%S")  # 按一定格式转化成datetime对象
            temp = []
            temp.append(datetime1.year)
            temp.append(datetime1.month)
            game_time = datetime1.hour * 3600 + datetime1.minute * 60 + datetime1.second
            temp.append(game_time)
            t.append(temp)

            total_time += game_time

    # 处理本月游戏时间
    for i in t:
        if i[0] == the_month.year and i[1] == the_month.month:
            month_time += i[2]

    # 处理上次游戏时间
    for i in t[-1:]:
        last_time+=i[2]

    # print(total_time, month_time, last_time)
    h1, m1, s1 = time_translate(total_time)
    h2, m2, s2 = time_translate(month_time)
    h3, m3, s3 = time_translate(last_time)
    with open(gametimetotal, mode='r', encoding='utf-8') as f:
        li = f.readlines()
    li[0] = f"{h1} {m1} {s1}\n"
    li[1] = f"{h2} {m2} {s2}\n"
    li[2] = f"{h3} {m3} {s3}\n"
    with open(gametimetotal, mode='w', encoding='utf-8') as f:
        f.writelines(li)

def show_game_time(gametimetotal = "logs/game_time_total.txt"):
    with open(gametimetotal, mode='r', encoding='utf-8') as f:
        li = f.readlines()
    time = [i.split() for i in li]
    # print(time)
    print(f"全部游戏时间为：{time[0][0]}小时 {time[0][1]}分钟 {time[0][2]}秒")
    print(f"本月游戏时间为：{time[1][0]}小时 {time[1][1]}分钟 {time[1][2]}秒")
    print(f"上次游戏时间为：{time[2][0]}小时 {time[2][1]}分钟 {time[2][2]}秒")


if __name__ == '__main__':
    process_time(gametime = "../logs/game_time.txt", gametimetotal = "../logs/game_time_total.txt")
    show_game_time(gametimetotal = "../logs/game_time_total.txt")