def rekurencja(s1, s2, sw):
    if len(s1) + len(s2) != len(sw):
        return False
    if len(s1) == 0:
        return s2 == sw
    if len(s2) == 0:
        return s1 == sw
    if s1[0] == sw[0]:
        return rekurencja(s1[1:], s2, sw[1:])
    if s2[0] == sw[0]:
        return rekurencja(s1, s2[1:], sw[1:])
    return False

def main():
    t = int(input())    # ilosc testow <= 1000
    ans = []
    for i in range(t):
        s1, s2, sw = input().split()
        a = rekurencja(s1 = s1, s2 = s2, sw = sw)
        if not a:
            a = rekurencja(s1=s2, s2=s1, sw=sw)
        ans.append(a)

    for i in ans:
        if i:
            print('TAK')
        else:
            print('NIE')

if __name__=='__main__':
    main()
