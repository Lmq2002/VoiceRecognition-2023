# -*- coding: utf-8 -*-

# 中文语声识别
# 效果不佳

import speech_recognition as sr

r = sr.Recognizer() # 语声识别器
mic = sr.Microphone() # 麦克风

print("请说话")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("正在识别")
# print("你输入的文件是："+type(audio).String())
test = r.recognize_sphinx(audio, language='zh-cn')  # 识别的语句
print("识别结果："+test)