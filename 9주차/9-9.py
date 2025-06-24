### Prim의 방법으로 최소비용 신장트리 탐색 ###

class Node:
    def __init__(self, value):
        self.data = value

class Graph:
    def __init__(self):
        self.graph = {} #인접 리스트 {1: [2, 3]} -> 1은 2, 3과 연결
        self.v_set = [] #정점을 spanning tree에 추가된 순서대로 저장
        self.edge = [] #spanning tree에 포함된 간선
        self.total = 0 #총 간선 비용
        self.nodes = set() #시작 정점 입력 시 비교

    ###인접 리스트 생성
    def create(self, v, data, weight):  
        node = Node(data)
        if v not in self.graph: 
            self.graph[v] = []
        self.graph[v].append((node, weight)) #graph[v]에 node 추가

        self.nodes.add(v)
        self.nodes.add(data)

    ###방문한 정점의 간선을 비용을 기준으로 오름차순 정렬
    def sort_edge(self, network): 
        temp = []
        for v1, v2, cost in network:
            #하나의 정점만 방문한 경우만 해당
            if (v1 in self.v_set and v2 not in self.v_set) \
                or (v2 in self.v_set and v1 not in self.v_set):
                temp.append((cost, v1, v2))
        temp.sort()
        return temp
    
    ###prim 방법으로 최소비용 신장트리 찾기
    def prim(self, start, network):
        self.v_set.append(start) #방문 리스트에 시작 정점 추가

        for _ in range(len(self.graph)): #g.graph에서 마지막에 포함된 정점은 key 아님
            sort_lst = self.sort_edge(network)
            for cost, v1, v2 in sort_lst:
                if (v1 not in self.v_set) or (v2 not in self.v_set): #미방문 정점일 경우
                    #방문 리스트에 정점 추가
                    if v1 in self.v_set:
                        self.v_set.append(v2)
                    else: 
                        self.v_set.append(v1) 
                    self.edge.append((v1, v2, cost)) 
                    self.total += cost
                    break

g = Graph()
network = [(1, 2, 5), (1, 4, 3), (2, 5, 10), (3, 5, 8), (3, 7, 11), \
           (4, 5, 6), (4, 6, 7), (5, 7, 13), (6, 7, 15)] #연습문제 9-2

#인접 리스트 생성
for v, node, weight in network:
    g.create(v, node, weight)
print('network =', network)

while True:
    try:
        start = int(input('시작 정점을 입력하세요: ')) #탐색을 시작할 정점 입력받기
        if start not in g.nodes:
            raise ValueError
        break
    except ValueError:
        print('올바른 숫자를 입력해주세요.')

g.prim(start, network); print()
print('Spanning tree vertices =', g.v_set)
print('Spanning tree edge =', g.edge)
print('cost total =', g.total)
