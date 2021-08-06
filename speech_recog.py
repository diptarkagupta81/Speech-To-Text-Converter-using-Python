import speech_recognition as sr

r = sr.Recognizer()
mic=sr.Microphone()
sr.Microphone.list_microphone_names()
mic=sr.Microphone(device_index=1)
with mic as source:
    
    r.adjust_for_ambient_noise(source)
    print('please say something..')
    audio=r.listen(source)
    try:
        print("you said: \n \n "+r.recognize_google(audio))
        print("\n you sound recorded successfully")
    except:
        print("error PLEASE TRY AGAIN!!!!!")
        