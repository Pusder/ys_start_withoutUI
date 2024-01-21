def time_translate(t):
    hour = 0
    minute = 0
    second = 0
    if t>=3600:
        hour = t/3600
        t = t%3600
    if t>=60:
        minute = t/60
        t = t%60
    second = t
    return int(hour), int(minute), int(second)

if __name__ == '__main__':
    print(time_translate(4000))