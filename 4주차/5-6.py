class Node:
    def __init__(self, item):
        self.data = item
        self.link = None

class SLL:
    def __init__(self):
        self.head = self.tail = None

    def view(self): #연결 리스트 출력
        temp = self.head
        print('[', end = ' ')
        while temp:
            print(temp.data, end = ' ')
            temp = temp.link
        print(']')

    def add(self, item): #노드 추가
        node = Node(item)
        if not self.head: #빈 리스트
            self.head = node
            self.tail = node
        else: #리스트 맨 뒤 추가
            self.tail.link = node
            self.tail = node

    def delete(self): #노드 삭제
        if not self.head: #head가 없다면 빈 리스트
            print('리스트 삭제 완료')
        else: 
            node = self.head
            if self.head == self.tail: #노드가 하나만 남았다면
                self.head = self.tail = None #참조 없애기
                del node
            else:
                #앞에서부터 삭제
                self.head = node.link
                del node

count_node = 5 #노드 개수
lst = SLL()

#연결리스트 생성
print('연결리스트 생성')
for i in range(count_node):
    lst.add(i)

#삭제 전 리스트 출력
lst.view()

#연결리스트 전체 삭제
print('연결리스트 삭제')
for i in range(count_node):
    lst.delete()

#삭제 후 리스트 출력
lst.view()