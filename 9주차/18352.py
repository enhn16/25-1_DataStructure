graph = {} #인접그래프
nodes = {} #노드의 최단 거리

N, M, K, X = map(int, input().split())

#인접그래프에 추가
for _ in range(M):
    v1, v2 = map(int, input().split())
    
    if v1 not in graph:
        graph[v1] = []
    graph[v1].append(v2)

def bfs(v):
    queue = [v]
    nodes[v] = 0
    front = 0  # 큐의 앞 인덱스

    while front < len(queue):
        temp = queue[front]
        front += 1
        if temp in graph:
            for n in graph[temp]:
                if n not in nodes:
                    nodes[n] = nodes[temp] + 1
                    queue.append(n)

bfs(X)

# 거리 K인 노드만 결과 리스트에 추가
result = []
for v in nodes:
    if nodes[v] == K:
        result.append(v)

# 출력
if result:
    result.sort()
    for v in result:
        print(v)
else:
    print(-1)
