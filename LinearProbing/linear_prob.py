class LinearProbing:
    def __init__(self, size) :
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
    
    def hash(self, key) :
        return key % self.M

    def put(self, key, data) : # 삽입 연산
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True :
            if self.a[i] == None : # 빈 곳 발견
                self.a[i] = key # key는 해시 테이블에, data는 리스트 d에 저장
                self.d[i] = data
                return
            if self.a[i] == key : # key가 이미 해시 테이블에 있으므로 data만 갱신
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M # 다음 원소 검사
            if i == initial_position : # 다음 위치가 초기 위치와 같으면 루프 벗어남
                break
        
    def get(self, key) :
        initial_position = self.hash(key) # 초기 위치
        i = initial_position
        j = 1
        while self.a[i] != None :
            if self.a[i] == key :
                return self.d[i]
            i = (initial_position + j) % self.M
            j += 1
            if i == initial_position:
                return None
        return None
    
    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()
