import random
class RandProbing :
    def __init__(self, size) : # 객체 생성자
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0 # 항목 수

    def hash(self, key) : 
        return key % self.M # 나눗셈 해시 함수
    
    def put(self, key, data) :
        initial_position = self.hash(key) # 초기 위치
        i = initial_position
        random.seed(1000)
        loop_limit = 20
        while True :
            if self.a[i] == None : # 빈 곳 발견 -> 키는 해시 테이블에, 데이터는 리스트 d에 저장
                self.a[i] = key 
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key : # 키가 이미 해시 테이블에 있으므로 데이터만 갱신
                self.d[i] = data
                return
            j = random.randint(1, 99)
            i = (initial_position + j) % self.M # 다음 원소 검사
            loop_limit -= 1
            if loop_limit == 0 : #  저장 시도 횟수 제한 초과
                break
    
    def get(self, key) :
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        loop_limit = 20
        while self.a[i] != None and loop_limit > 0 :
            if self.a[i] == key : # 탐색 성공 시 데이터 반환
                return self.d[i]
            i = (initial_position + random.randint(1, 99)) % self.M
            loop_limit -= 1
        return None    
    
    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()