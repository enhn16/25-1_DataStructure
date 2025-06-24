def decode(entry):
    left = [] #커서 기준 왼쪽에 있는 문자
    right = [] #커서 기준 오른쪽에 있는 문자
    for i in entry:
        if i == '-':
            if left: #백스페이스 입력, left에 항목 존재
                left.pop() #left 마지막 항목을 삭제
        elif i == '<':
            if left: #왼쪽 화살표 입력, left에 항목 존재
                right.append(left.pop()) #left 마지막 항목을 right에 추가
                # 원래 insert로 했으나, 시간초과 문제로 변경 #
        elif i == '>':
            if right: #오른쪽 화살표 입력, right에 항목 존재 
                left.append(right.pop()) #right 마지막 항목을 left에 추가
        else:
            left.append(i) #문자나 숫자는 left에 추가
    left.extend(right[::-1]) #right 항목을 뒤 부터 추가
    return left
num = int(input())
for i in range(num):
    entry = input()
    result = decode(entry)
    print(''.join(result))

    