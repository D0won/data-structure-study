def shell_sort(a) :
    h = 4
    while h >= 1 :
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h] : # 각 그룹에 대해 삽입 정렬 수행
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h //= 3 # 다음 h 값 계산 -> 1로 계산됨
a = [65,95,90,80,55,70,35,50,10,25,40,30]
print('정렬 전:\t', end='')
print(a)
shell_sort(a)
print('정렬 후:\t', end='')
print(a)