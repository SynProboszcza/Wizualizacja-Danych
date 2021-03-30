def txtToAscii(string):
    for x in range(len(string)):
        print(string[x],":",bytearray(string, "utf-8")[x])