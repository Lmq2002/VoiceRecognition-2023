import speech_recognition as sr


mic = sr.Microphone()  # 麦克风实例
r = sr.Recognizer()    # 识别器实例

# 进行录音
print("inputing")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)

# 进行识别
print("outputing")
test = r.recognize_google(audio, language='cmn-Hans-CN')
print(test)