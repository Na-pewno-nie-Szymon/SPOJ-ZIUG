# do dokończenia, zostało najłatwiejsze (chyba)


def zadanie(y, args):
    if y < 3:
        return 'NIE'
    
    intTime = []
    for arg in args:
        t1, m1, t2, m2 = arg[0][:2], arg[0][3:5], arg[1][:2], arg[1][3:5] 
        intTime.append([float(t1) + float(m1)/60, float(t2) + float(m2)/60])

    ilfilm = 1
    for i in range(len(intTime)):
        ilfilm = 1
        film0 = intTime[i]
        for j in range(len(intTime)-1, i, -1):
            if i == j:
                continue
            else:
                if (intTime[j][0] < film0[1] and intTime[j][0] >= film0[0]) or (intTime[j][1] > film0[0] and intTime[j][1] <= film0[1]): 
                    # TypeError: '>' not supported between instances of 'list' and 'float'
                    pass
                else:
                    ilfilm += 1
            print(ilfilm)
            if ilfilm == 3:
                return 'TAK'
    return 'NIE'
                

def main():
    test = int(input()) # -> ilosc dni
    ans = []
    for _ in range(test):
        dzien = input().split() # -> dzien[0]=='dzien'; dzien[1]=='x'(numer dnia);x dzien[2]=='y'(ilosc emitowanych filmow)
        godziny = []
        for i in range(int(dzien[2])):
            start, koniec = input().split()
            godziny.append([start, koniec])
        ans.append(zadanie(y=int(dzien[2]), args=godziny))
    
    for a in ans:
        print(a)

if __name__=='__main__':
    main()
 
