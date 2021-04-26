print("qwe" + str(bytearray([10])[0]))

bytearray([10])[0]
bytearray(b'\n')[0]
bytearray(b'e')[0] #101
bytearray(b'a')[0] #97

bity = [101,97]

chr(kod ascii)
print(chr(bytearray([bity[0]])[0])+chr(bytearray([bity[1]])[0]))
print('\a')



>>> bytearray([x for x in range(256)])
bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff')

bity = bytearray([x for x in range(256)])

for x in range(256):
    print(str(x) + ":" + str(bity[x]))


for x in range(256):
    print(str(x) + ":\\" + str(hex(bity[x])))

str1 = "Ramen to kot."

for x in range(len(str1)):
    print(str1[x],":",bytearray(str1, "utf-8")[x])

def txtToAscii(string):
    for x in range(len(string)):
        print(string[x],":",bytearray(string, "utf-8")[x])



txtToAscii([str(chr(x)) for x in range(97,105,1)])

[str(chr(x)) for x in range(97,105,1)]

wprowadzic bity zamienic na ea


import winsound as w
dur = 1000
freq = 440
w.Beep(freq, dur)

for x in range(400,600,10):
    print(x)
    w.Beep(x, 1)

from gtts import gTTS
import os
str1 = "Ramen to kot."
lang = "pl"
myobj = gTTS(text=str1, lang=lang, slow=False)

myobj.save("dupa.mp3")


str1 = "sasagejo, sasagejo"
myobj = gTTS(text=str1, lang=lang, slow=False)
myobj.save("dupa.mp3")

def powiedz(co_powiedziec, czy_kasowac=True, nazwa_pliku_temp="temp.mp3", lang="pl", tryb_wolny=False):
    from gtts import gTTS
    import playsound
    import os
    myobj = gTTS(text=co_powiedziec, lang=lang, slow=tryb_wolny)
    myobj.save(nazwa_pliku_temp)
    playsound.playsound(nazwa_pliku_temp)
    if czy_kasowac:
        os.remove(nazwa_pliku_temp)

powiedz("niewyrewolwerowany rewolwerowiec wyrewolwerował rewolwer niewyrewolwerowanego rewolwerowca")
powiedz("Alicja kupiła sobie Zonię", False, "Alicja.mp3")
powiedz(str1, False, "Alicja.mp3")

blitz jest koksem
ff15

str1 = "papież polak dżarvan czwarty, bot od dawna jest otwarty"
str1 = "i want to be your dziaddy"
"aj łant to bi jur dziaddy"

from mpyg321.mpyg321 import MPyg321Player
player = MPyg321Player()
player.play_song("/path/to/some_mp3.mp3")



from tqdm.auto import trange
from time import sleep

for i in trange(4, desc='1st loop'):
    for j in trange(5, desc='2nd loop'):
        for k in trange(50, desc='3rd loop', leave=False):
            sleep(0.01)


from tqdm import tqdm, trange
from random import random, randint
from time import sleep

with trange(10) as t:
    for i in t:
        # Description will be displayed on the left
        # t.set_description('GEN %i' % i)
        # Postfix will be displayed on the right,
        # formatted automatically based on argument's datatype
        # t.set_postfix(loss=random(), gen=randint(1,999), str='h',
        #               lst=[1, 2])
        sleep(0.1)

with tqdm(total=10, bar_format="{postfix[0]} {postfix[1][value]:>8.2g}",
          postfix=["Batch", dict(value=0)]) as t:
    for i in range(10):
        sleep(0.1)
        t.postfix[1]["value"] = i / 2
        t.update()

tab=[]
for x in range(1001):
    tab[x] = (2**x)/factorial(x)

[(2**x)/factorial(x) for x in range(10)]
a = np.array([(3**x)/factorial(x) for x in range(10)])
a.sum()

