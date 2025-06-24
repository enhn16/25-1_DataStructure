def draw_star(n):
    result = []
    if n == 0:
        result.append('*')
    else: ###리스트에 출력할 별 업데이트
        lst = draw_star(n-1) #재귀를 이용해 이전 형태 가져옴
        #윗 부분 업데이트
        for star in lst:
            num = 2**(n-1) #draw_star(n-1)의 맨 위 별 개수
            #형태를 위한 공백을 추가
            star += ' '*(num - len(star))
            result.append(star+star)
        #아랫 부분 업데이트
        for star in lst:
            result.append(star)
    return result

n = int(input())
result = draw_star(n)
###반복문을 이용해 리스트에 저장한 별 출력
for row in result:
    #불필요한 공백 제거 후 출력
    while row[-1] == ' ':
        row = row[:-1]
    print(row)