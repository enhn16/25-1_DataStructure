###이진트리의 조상 노드와 자손 노드 찾기

#트리 생성
tree1 = [None]
tree2 = list(input('트리의 요소를 입력하세요: ').split())
tree = tree1 + tree2

#특정 노드 값 입력받아 인덱스 찾기
data = input('기준 노드의 값을 입력하세요: ')
if data not in tree:
    print('노드를 찾을 수 없습니다.')
    exit()
idx = tree.index(data)

#조상 노드 찾기
list_anc = []
def ancestor(idx):
    if idx == 1:
        return
    idx = idx//2
    list_anc.append(tree[idx])
    ancestor(idx)

#자손 노드 찾기
list_des = []
def descendant(idx):
    left = idx*2
    right = idx*2+1

    if left < len(tree):
        list_des.append(tree[left])
        descendant(left)
    if right < len(tree):
        list_des.append(tree[right])
        descendant(right)

#실행과 출력
ancestor(idx)
descendant(idx)

print('ancedtor:', list_anc)
print('descendant:', list_des)