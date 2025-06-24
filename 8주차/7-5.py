class Heap:
    def __init__(self):
        self.heap = [0] #인덱스 오류 방지 위한 초기화
        self.count = 0

    def add_heap(self, item): ###원소 추가
        self.count += 1
        self.heap.append(0) #미리 자리 추가

        i = self.count
        while i != 1 and item > self.heap[i // 2]:
            self.heap[i] = self.heap[i//2]
            i //= 2
        self.heap[i] = item
        self.show()

    def show(self): ###힙 출력
        n = 1 #한 줄에 출력할 워소의 개수
        idx = 1 #현재 출력할 원소의 인덱스, 1부터 시작
        while idx <= self.count:
            for _ in range(n):
                if idx > self.count: break #for문 안에서는 idx가 범위를 넘어갈 수 있어서
                print(f'[{self.heap[idx]}]', end = ' ')
                idx += 1
            print()
            n *= 2

h = Heap()
while True:
    entry = int(input('input: '))
    if entry == 999:
        h.heap.pop(0) #필요없는 값인 0 제거
        h.heap.sort(reverse=True) #내림차순 출력위함
        for node in h.heap:
            print(f'[{node}]', end = ' ')
        break

    h.add_heap(entry)