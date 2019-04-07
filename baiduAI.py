#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rec
from aip import AipSpeech


APP_ID = '15943680'
API_KEY = 'xh57oiDWi19RLOMj7jk8BhYH'
SECRET_KEY = 'V52Il01x0lMY6IcbjAQlzQTChncNIXte'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取音频文件
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


# 语音识别
def get_text():
    # 开始录音
    rec.rec_fun()
    result = client.asr(get_file_content('/home/pi/temp.wav'), 'wav', 16000, {
        'dev_pid': 1536,
    })
    # 输出结果
    print result['result'][0]
    return result['result'][0]


# 语音合成
def get_audio(text):
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 3,
        'pit': 0,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('/home/pi/audio.mp3', 'wb') as f:
            f.write(result)

    return


# get_audio()
# play('audio.mp3')
