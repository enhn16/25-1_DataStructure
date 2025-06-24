###최소 힙을 이용한 힙정렬 -> 내림차순 정렬
class HeapSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Heap Sort")
        print(self.num)

    #최소 힙 재구성
    def makeheap(self, idx, n): 
        temp = self.num[idx]
        child = 2 * idx
        while child <= n:
            if child < n and self.num[child] > self.num[child+1]:
                child += 1 #더 작은 자식으로 변경
            if temp < self.num[child]:
                break
            else:
                self.num[child//2] = self.num[child] #부모 노드 위치에 자식 값 넣기
                child *= 2 #하위 레벨로 이동동
        self.num[child//2] = temp #자식 위치에 부모 노드 값 넣기
        
    #정렬
    def sort(self):
        n = self.size-1
        for i in range(n//2, 0, -1):
            self.makeheap(i, n)
        print(self.num)
        for i in range(n-1, 0, -1):
            #최소값과 마지막 원소 교환
            self.num[1], self.num[i+1] = self.num[i+1], self.num[1]
            self.makeheap(1, i)
            print(self.num)

num = [None, 24, 7, 80, 3, 64, 15, 50, 10, 42, 18]
s = HeapSort(num)
s.sort()