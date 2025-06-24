def josephus(n, k):
    lst = [i for i in range(1, n+1)] #함축을 이용해 리스트에 숫자 저장
    result = [] #결과를 저장할 리스트
    index = 0
    while lst:
        index = (index + k-1) % len(lst)  #이번 대상의 인덱스 계산
        #제거 후 리스트의 길이가 줄어들기에 인덱스 계산 가능
        result.append(lst.pop(index)) #lst에서 제거한 숫자를 result에 추가    
    return result
    
n, k = map(int, input().split())
result = josephus(n, k)
#형식에 맞춰 출력
print('<', end = '')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print('>')