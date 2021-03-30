def powiedz(co_powiedziec, czy_kasowac=True, nazwa_pliku_temp="temp.mp3", lang="pl", tryb_wolny=False):
    from gtts import gTTS
    import playsound
    import os
    myobj = gTTS(text=co_powiedziec, lang=lang, slow=tryb_wolny)
    myobj.save(nazwa_pliku_temp)
    playsound.playsound(nazwa_pliku_temp)
    if czy_kasowac:
        os.remove(nazwa_pliku_temp)