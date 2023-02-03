

import pyttsx3 as voz

engine = voz.init('sapi5')

voices = engine.getProperty('voices')

def sevoice(voice):
    """Only voice 0 & voice 1"""

    avoz = (voice)

    if avoz == 0:
        engine.setProperty('voice', voices[0].id)
    
    elif avoz == 1:
        engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class says:


    def inp_text(text):
        textPut = input(text)
        speak(textPut)

    def inp_num(Number):
        number = float(input(Number))
        speak(number)
    
    def sp_text(text):
        jtext = (text)
        speak(jtext)
    
    def sp_number(int):
        num = (int)
        speak(num)