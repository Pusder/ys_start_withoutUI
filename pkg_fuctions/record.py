import datetime
import sys

import speech_recognition as sr
import logging
import zhconv

from pkg_fuctions.process_time import process_time, show_game_time
from pkg_fuctions.match import is_match_GenshinImpact, is_match_StarRail
from pkg_fuctions.run_model import run_model
from pkg_fuctions.process_words import process_words
from pkg_fuctions.play_music import play_music
from pkg_fuctions.open_ys import open_ys
from pkg_fuctions.time_translate import time_translate


class record:
    def __init__(self):
        '''声音片段能量值高于阈值视为有声音输入，低于则为没有声音输入'''
        self.r = sr.Recognizer()
        self.r.non_speaking_duration = 0.3  # 有声音输入后进入录音，此数值为保存没有声音输入的片段的最大时长
        self.r.pause_threshold = 0.5  # 录音中没有声音输入的最大持续时间，超过这个时间就会停止录音

        # 创建一个Microphone对象，设置采样率为11025Hz——AM调幅广播所用采样率
        self.mic = sr.Microphone(sample_rate=11025)

        # 加载日志
        # 格式 2024-01-01 19:19:36|INFO|麦克风已打开
        # logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s",
        #                     datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
        self.stream_logger = logging.getLogger(name='StreamLogger')
        sh = logging.StreamHandler(stream=None)   # StreamHandler：把日志内容在控制台中输出
        fm1 = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        sh.setFormatter(fm1)
        self.stream_logger.addHandler(sh)
        self.stream_logger.setLevel(logging.INFO)
        # 格式 2024-01-01|00:00:01
        self.file_logger = logging.getLogger(name='FileLogger')  # FileHandler：把日志内容写入到文件中
        fh = logging.FileHandler(filename="logs/game_time.txt", mode='a', encoding="utf-8")
        fm2 = logging.Formatter("%(asctime)s|%(message)s", datefmt="%Y-%m-%d")
        fh.setFormatter(fm2)
        self.file_logger.addHandler(fh) # 把handle处理器添加到logger里面
        self.file_logger.setLevel(logging.INFO) # 是对logger设置，不是对handle处理器设置，否则不能正常输出

        # 加载模型
        self.model = run_model()
        self.stream_logger.info("模型已加载完毕")

    def run(self):
        while True:
            # 打开麦克风
            self.stream_logger.info("麦克风已打开")
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source, duration=0.5)    # 进行环境噪音适应，duration为适应时间，不能小于0.5
                self.stream_logger.info("开始录音")
                audio = self.r.listen(source, phrase_time_limit=10)  # 监听麦克风录音，最多录十秒语音
                self.stream_logger.info("录音结束")

                # 将录音数据写入.wav格式文件
                with open(r"logs/temp.wav", "wb") as f:
                    f.write(audio.get_wav_data())   # 将返回的wav格式的音频二进制数据写入wav文件
            self.stream_logger.info("麦克风已关闭")
            text = self.model.run(audio=r"logs/temp.wav")
            self.stream_logger.info("识别结果："+zhconv.convert(text, 'zh-cn'))
            text = process_words(text)

            if is_match_GenshinImpact(text):
                self.stream_logger.info("即将启动原神")
                path = r"D:\原神\Genshin Impact\Genshin Impact Game\YuanShen.exe"
                play_music()
                game_time = open_ys(path)
                hour, minute, second = time_translate(game_time)
                t = datetime.time(hour, minute, second)
                self.stream_logger.info(f"游戏结束，本次游戏时间为{hour}h {minute}m {second}s")

                self.file_logger.info(t.isoformat())
                process_time()
                show_game_time()
                break
            elif is_match_StarRail(text):
                self.stream_logger.info("即将启动崩坏:星穹铁道")
                path = r"D:\星穹铁道\Star Rail\Game\StarRail.exe"
                play_music()
                game_time = open_ys(path)
                hour, minute, second = time_translate(game_time)
                t = datetime.time(hour, minute, second)
                self.stream_logger.info(f"游戏结束，本次游戏时间为{hour}h {minute}m {second}s")

                self.file_logger.info(t.isoformat())
                process_time()
                show_game_time()
                break


if __name__ == '__main__':
    # 获取管理员权限的打包指令：pyinstaller --uac-admin --onefile record.py
    r = record()
    r.run()
