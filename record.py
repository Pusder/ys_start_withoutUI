import speech_recognition as sr
from match import is_match_GenshinImpact, is_match_StarRail
from run_model import run_model
from process_words import process_words
from play_music import play_music
from open_ys import open_ys
from time_translate import time_translate
import logging


class record:
    def __init__(self):
        '''声音片段能量值高于阈值视为有声音输入，低于则为没有声音输入'''
        self.r = sr.Recognizer()
        self.r.non_speaking_duration = 0.3  # 有声音输入后进入录音，此数值为保存没有声音输入的片段的最大时长
        self.r.pause_threshold = 0.5  # 录音中没有声音输入的最大持续时间，超过这个时间就会停止录音

        # 创建一个Microphone对象，设置采样率为11025Hz——AM调幅广播所用采样率
        self.mic = sr.Microphone(sample_rate=11025)

        # 加载模型
        logging.basicConfig(level=logging.DEBUG)
        self.model = run_model()

    def run(self):
        while True:
            # 打开麦克风
            logging.info("麦克风已打开")
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source, duration=0.5)    # 进行环境噪音适应，duration为适应时间，不能小于0.5
                logging.info("开始录音")
                audio = self.r.listen(source, phrase_time_limit=10)  # 监听麦克风录音，最多录十秒语音
                logging.info("录音结束")

                # 将录音数据写入.wav格式文件
                with open(r"record_logs\temp.wav", "wb") as f:
                    f.write(audio.get_wav_data())   # 将返回的wav格式的音频二进制数据写入wav文件
            logging.info("麦克风已关闭")
            text = self.model.run(audio=r"record_logs\temp.wav")
            text = process_words(text)
            logging.info(text)
            if is_match_GenshinImpact(text):
                logging.info("即将启动原神")
                play_music()
                game_time = open_ys()
                hour, minute, second = time_translate(game_time)
                logging.info(f"本次游戏时间为{hour}h {minute}m {second}s")
                logging.info("结束")
                break
            elif is_match_StarRail(text):
                logging.info("即将启动崩坏:星穹铁道")
                path = r"D:\星穹铁道\Star Rail\Game\StarRail.exe"
                play_music()
                game_time = open_ys(path)
                hour, minute, second = time_translate(game_time)
                logging.info(f"本次游戏时间为{hour}h {minute}m {second}s")
                logging.info("结束")
                break


if __name__ == '__main__':
    # 获取管理员权限的打包指令：pyinstaller --uac-admin --onefile record.py
    r = record()
    r.run()
