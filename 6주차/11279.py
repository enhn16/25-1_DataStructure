### 최대 힙 ###

#시간 초과 문제를 해결하기 위함
import sys
input = sys.stdin.readline

number = [None]

#배열에 숫자 추가
def add(num):
    number.append(num)
    i = len(number) - 1
    #재구성
    while i > 1 and num > number[i//2]:
        number[i], number [i//2] = number [i//2], number[i] 
        i //= 2 #상위 레벨로 이동

#가장 큰 값 삭제 후 반환
def pop():
    if len(number) == 1:
        return 0
    loot = number[1]
    last = number.pop()
    #요소가 하나만 존재했다면 바로 반환
    if len(number) == 1:
        return loot
    #재구성
    i = 1
    number[1] = last
    while 2 * i < len(number):
        child = 2 * i
        if child + 1 < len(number) and number[child] < number[child + 1]:
            child += 1
        if number[i] >= number[child]:
            break
        number[i], number[child] = number[child], number[i]
        i = child
    return loot

n = int(input())
result = []
for _ in range(n):
    entry = int(input())
    if entry == 0:
        result.append(str(pop()))
    else:
        add(entry)

print('\n'.join(result))
