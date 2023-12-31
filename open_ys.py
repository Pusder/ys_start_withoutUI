import ctypes
import subprocess
import sys
import time

# 获取管理员权限的打包指令：pyinstaller --uac-admin --onefile open_ys.py
def open_ys(ys_path = "D:\原神\Genshin Impact\Genshin Impact Game\YuanShen.exe"):
    '''D:\原神\Genshin Impact\Genshin Impact Game\YuanShen.exe'''
    start = time.time()
    print(ctypes.windll.shell32.IsUserAnAdmin())
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    print(ctypes.windll.shell32.IsUserAnAdmin())
    ys = subprocess.Popen(ys_path)
    while ys.poll() is None:    # 程序尚未结束
        continue
    end = time.time()
    game_time = end-start
    return int(game_time)

if __name__ == '__main__':
    path = r"C:\Users\Pusder\Desktop\最长公共子序列by邓善鹏.exe"
    print(open_ys())
    input("请按任意键继续...")