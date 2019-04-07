# -*- coding:utf-8 -*-

import pyaudio
import wave
import os
import sys

RECORD_SECONDS = 3
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
WAVE_OUTPUT_FILENAME = "/home/pi/temp.wav"


def rec_fun():
    os.close(sys.stderr.fileno())

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=1,  # cloud speecAPI只支持单声道
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print(u"录音中...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print(u"录音完成，输出文件：" + WAVE_OUTPUT_FILENAME + '\n')

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return
