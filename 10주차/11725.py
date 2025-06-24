### 노드의 부모 찾기 ###

import sys
sys.setrecursionlimit(10**6) #제귀 제한 늘리기

n = int(sys.stdin.readline())

gragh = {} #인접 리스트
visit = [False] * (n + 1) #방문여부 확인
parent = {} #부모 저장

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in gragh:
        gragh[a] = []
    if b not in gragh:
        gragh[b] = []
    gragh[a].append(b)
    gragh[b].append(a)

def dfs(v):
    visit[v] = True
    for node in gragh[v]:
        if not visit[node]:
            parent[node] = v #node의 부모는 v
            dfs(node)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])
 
