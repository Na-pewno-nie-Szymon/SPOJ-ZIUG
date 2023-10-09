def aMozeTo(liczba):
    if liczba % 2 == 0 or liczba % 5 == 0:	# wykluczenie warunków niemożliwyych
        return 'NIE'  
      
    l = liczba
    iloscJeden = 0
    
    while liczba > 0:	# główny algorytm liczenia długości liczby złożonej z samych jedynek 
        if liczba % 10 == 1:
            liczba = liczba // 10
            iloscJeden += 1
        else:
            liczba += l 

    return iloscJeden
 
def main():
    liczby = []
    t = int(input())	# ilosc testow <= 10000
    for i in range(t):
        liczby.append(int(input()))	# liczba do sprawdzenia <1;10000>

    for i in range(t):	# wypisywanie wyników
        print(aMozeTo(liczba=liczby[i]))

if __name__=='__main__':
    main()
