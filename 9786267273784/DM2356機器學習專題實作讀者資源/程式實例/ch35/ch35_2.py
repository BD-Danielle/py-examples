# ch35_2.py
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("請說中文 ...")
    audio = r.listen(source)
    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio, language="zh-TW")  
        print("你說的中文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")







