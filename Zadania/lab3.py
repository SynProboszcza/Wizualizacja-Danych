"""
#bawiłem się przed zajęciami
owoce = ["jalbko","banan","kiwi","cytryna","kartofel","mario"]
owoce_z_n = [x.upper() for x in owoce if "n" in x]
liczby_nieparzyste = [x for x in range(1000) if x%2!=0]
imiona = ["dawid","alicja","mariusz","ketchup","zerotwo","michael"]
Imiona = [x.capitalize() for x in imiona]

try:
    print(int('1.0'))
    print("bezbłędnie")
except ValueError:
    print(int(float('1.0')))
    print("błędnie")
"""














