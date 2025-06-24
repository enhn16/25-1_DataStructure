###중위 탐색 결과보고 트리 구현
h = int(input())
travel = list(input().split())
#트리의 기본 구조 설정
tree = [[] for _ in range(h)]

#트리 구현
def make_tree(level, index):
    if level == h: #리프노드에 도달
        return index  
    #왼쪽 서브트리 생성
    index = make_tree(level + 1, index)
    #현재 노드 저장
    tree[level].append(travel[index])
    index += 1
    #오른쪽 서브트리
    index = make_tree(level + 1, index)
    return index  #다음 위치 반환

make_tree(0, 0) #루트부터 시작, 인덱스 0

#출력
for level in tree:
    for num in level:
        print(num, end = ' ')
    print()