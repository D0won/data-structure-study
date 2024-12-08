class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a) - 1

    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value) : # 삽입 연산
        self.N +=1
        self.a.append(key_value)
        self.upheap(self.N)
    
    def delete_min(self) : # 최솟값 삭제
        if self.N == 0:
            print('힙이 비어 ㅇ있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downheap(1)
        return minimum
    
    def downheap(self, i) :
        while 2*i <= self.N :
            k = 2*i
            if k < self.N and self.a[k][0] > self.a[k+1][0]: # k가 힙 총 개수보다 작고 오른쪽 노드와 왼쪽 노드 중 작은 키를 고름
                k += 1
            if self.a[i][0] < self.a[k][0] : # 만약 k번째 노드가 i번째 노드보다 큰 경우 루프 나감
                break
            self.a[i], self.a[k] = self.a[k], self.a[i] # 만약 아닐 경우 키 체인지
            i = k # i는 다시 k번째 노드가 됨
    
    def upheap(self, j) :
        while j > 1 and self.a[j//2][0] > self.a[j][0] : # j가 1보다 크고 현재 노드가 부모 노드보다 작은 경우 올라감
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j // 2 # 노드 층이 올라감
    
    def print_heap(self) :
        for i in range(1, self.N+1) :
            print('[%2d' % self.a[i][0], self.a[i][1],']', end='')
        print('\n힙 크기 = ', self.N)