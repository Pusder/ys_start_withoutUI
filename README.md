项目使用说明：
下载项目文件后，在项目文件根目录新建一个model文件夹，里面要存放我们的模型文件small.pt，下载地址见下方。
然后配置我们的项目环境，跟着下面的视频配置就行了，主要是需要配置好ffmpeg和虚拟环境，接触过深度学习的应该会很顺手。
接着就用pycharm打开项目，环境选择conda—>使用现有环境，然后选择你刚刚配置好的虚拟环境。
最后只需要点开record.py文件，将原神和星铁的路径(path变量的值)改成自己的（不玩星铁的可以直接把elif的那几行删掉），运行record.py文件或者main.py文件都可以。
（前端和打包还在努力研究中）
（想改启动音的可以先把提示音丢进music文件夹里，再在play_music.py文件里修改path）

项目中所用到的语音识别模型下载地址：https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt

项目环境配置参考视频：https://www.bilibili.com/video/BV1a94y1H7ce/?spm_id_from=333.337.search-card.all.click&vd_source=d410e9caee7e65cbaf0703b4a1f1a7cc
