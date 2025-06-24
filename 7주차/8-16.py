### 최대값 우선 선택 정렬 ###

def SelectionSort(num, n):
    for i in range(n, 0, -1):
        mx = i
        #최대값 찾기
        for j in range(i, -1, -1):
            if num[j] > num[mx]:
                mx = j
        num[i], num[mx] = num[mx], num[i] #최대값을 맨 오른쪽 수와 교환
        print(num)

num = [12, 25, 9, 34, 52, 49, 17, 5, 8]
SelectionSort(num, len(num)-1)
