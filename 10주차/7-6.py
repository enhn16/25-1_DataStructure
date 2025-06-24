class Node:
    def __init__(self, item):
        self.data = item
        self.parent = None #부모를 가리킴
        self.llink = self.rlink = None #자식을 가리킴

class Linked_Max_Heap:
    def __init__(self):
        self.head = Node(0)
        self.head.parent = None
        self.head.llink = self.head #루트 노드를 가리킴
        self.head.rlink = self.head #마지막 노드를 가리킴
        self.data_list = [] #중복을 확인하기 위해 요소의 값 저장

    ###기능1. 노드 추가
    def add(self, item):
        #중복된 값은 추가하지 않음
        if item in self.data_list:
            print('이미 존재하는 값입니다.')
            return
        
        self.head.data += 1 #노드 개수 갱신
        self.data_list.append(item)
        node = Node(item)
        if self.head.rlink == self.head: #empty
            self.head.llink = node
            self.head.rlink = node
        else:
            #추가할 노드를 부모 노드와 연결
            if (self.head.data-1) % 2 == 0: #이전 총 노드 개수 짝수 -> 마지막 노드가 왼쪽 자식
                parent_node = self.head.rlink.parent
                parent_node.rlink = node #추가한 노드가 오른쪽 자식이 됨
                node.parent = parent_node
            else:
                parent_node = self.find_parent()
                parent_node.llink = node #추가한 노드가 왼쪽 자식이 됨
                node.parent = parent_node

            self.sort_add(node) #마지막에 추가했으니 재구성
            self.head.rlink = self.find_last() #새로운 마지막 노드와 연결

        self.view(self.head.llink) #현재 최대 힙 출력
        print() #줄 바꿈

    ###자식을 추가할 부모노드 찾기
    def find_parent(self):
        queue = [self.head.llink] #레벨 탐색을 하기 위해 queue 이용
        front = 0 #루트를 큐에 넣고 시작했기에 0부터

        #레벨 탐색을 하며 처음으로 자식이 2개 미만인 노드를 선택
        while front < len(queue):
            node = queue[front]
            front += 1

            #왼쪽 자식이 비어 있다면 부모
            if node.llink is None:
                return node
            else:
                queue.append(node.llink)
            #왼쪽 자식은 있고 오른쪽 자식이 없다면 부모
            if node.rlink is None:
                return node
            else:
                queue.append(node.rlink) 

    ###기능2. 노드(루트) 삭제
    def delete(self):
        if self.head.data == 0:
            print('empty heap')
            return

        item = self.head.llink #루트
        temp = self.head.rlink #마지막 노드

        if self.head.data == 1: #루트만 있을 경우 삭제 후 종료
            self.head.llink = self.head
            self.head.rlink = self.head
            self.head.data = 0
            del temp
            return

        #마지막 노드를 루트 위치로 이동
        item.data = temp.data
        #마지막 노드와 부모의 관계 끊기
        parent = temp.parent
        if self.head.data % 2 == 0:
            parent.llink = None
        else:
            parent.rlink = None
        self.head.data -= 1 
        del temp #이전 마지막 노드 삭제

        self.sort_del(item) #마지막 노드가 루트가 되었으니 재구성
        self.head.rlink = self.find_last() #새로운 마지막 노드와 연결
        self.view(self.head.llink) #현재 최대 힙 출력
        print() #줄 바꿈

    ###마지막 노드를 찾아 head.rlink와 연결
    def find_last(self):
        #레벨 탐색 시 가장 마지막으로 탐색되는 노드가 마지막 노드
        queue = [self.head.llink] #레벨 탐색을 위해 queue 이용
        front = 0 #루트를 큐에 넣고 시작했기에 0부터
        last = None

        while front < len(queue): #모든 노드를 탐색
            last = queue[front]
            front += 1
            if last.llink:
                queue.append(last.llink)
            if last.rlink:
                queue.append(last.rlink)   
        return last #가장 마지막 값을 반환
    
    ###최대힙 재구성
    def sort_add(self, node): #bottom-up
        #부모의 값이 자식보다 더 크거나 루트에 도달할 때까지 반복하며 재구성
        while node.parent and node.data > node.parent.data:
            node.data, node.parent.data = node.parent.data, node.data #부모와 자식 교환
            node = node.parent #윗 단계로 가서 반복

    def sort_del(self, node): #top-down
        #현 노드, 왼쪽 자식 노드, 오른쪽 자식 노드의 크기를 비교하여 정렬
        while True:
            mx = node #현 노드가 가장 크다고 가정
            if node.llink and node.llink.data > mx.data: #왼쪽 자식이 더 크다면
                mx = node.llink
            if node.rlink and node.rlink.data > mx.data: #오른쪽 자식이 더 크다면
                mx = node.rlink

            if mx == node: #현 노드가 가장 크기에 정렬 끝
                break
            node.data, mx.data = mx.data, node.data #현 노드와 값이 큰 자식을 교환
            node = mx #아래 단계로 이동해 반복

    ###기능3. 최대힙의 모든 노드 값을 postorder로 출력
    def view(self, root):
        if root:
            self.view(root.llink)
            self.view(root.rlink)
            print(root.data, end = ' ')    

max_heap = Linked_Max_Heap()
#입력 후 출력
print('값을 순서대로 입력하세요. (종료: end)')
while True:
    entry = input('입력: ')
    if entry == 'end':
        break
    #end외에는 숫자만 입력받을 수 있도록 함
    try:
        max_heap.add(int(entry))
    except ValueError:
        print('숫자를 입력해주세요.')

#최종 최대 힙 출력
print('\n완성된 최대 힙 >>', end = ' ')
max_heap.view(max_heap.head.llink)
print()

#삭제 후 출력
print('\n루트가 하나씩 삭제됩니다.')
while max_heap.head.data:
    print('삭제:', max_heap.head.llink.data)
    max_heap.delete()
print('삭제가 완료되었습니다.')