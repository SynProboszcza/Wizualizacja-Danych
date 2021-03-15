def ciag(* liczby):
    suma = 0.0
    for x in range(len(liczby)):
        suma += liczby[x]
    print(suma)

ciag(float(range(1,15,1)))


