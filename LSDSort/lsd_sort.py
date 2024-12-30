def lsd_sort(a) :
    WIDTH = 3
    N = len(a)
    R = 128
    temp = [None] * N
    for d in reversed(range(WIDTH)):
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1 # 빈도 수 계산
        for j in range(1, R) :
            count[j] += count[j-1] # temp 에 저장할 시작 인덱스 계산
        for i in range(N): # d번째 문자를 기준으로 각 a[i]를 적절한 temp원소로 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N): # temp를 a로 복사
            a[i] = temp[i]
        print(f'{d}번쨰 문자:\t', end='')
        for x in a : print(x, ' ', end='')
        print()

a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV', 'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']
print('정렬 전:\t\t', end='')
for x in a : print(x, ' ', end='')
print()
lsd_sort(a)