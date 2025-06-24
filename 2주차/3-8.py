###문자열을 입력받고 각 문자들의 순열을 생성하는 프로그램
def permutation(lst):
    #재귀문이 실행될 때마다 word가 초기화 되기에 중간 문자열이 저장되지 않음
    word = [] 
    #리스트에 하나의 문자만 남으면 그 리스트를 반환
    if len(lst) == 1:
        return lst
    #반복문을 통해 모든 문자에 접근
    for i in range(len(lst)):
        #재귀문을 통해 생성한 문자열(word의 원소)을 하나씩 가져옴
        for s in permutation(lst[:i]+lst[i+1:]): #현재 선택한 원소를 제외한 리스트로 재귀
            #현재 문자와 가져온 문자열을 더해 새 문자열 생성 후 word에 추가
            word.append(lst[i]+s)
    #현재까지 생성된 문자열이 저장된 리스트를 반환
    return word

lang = list(input('길이가 4인 문자열을 입력하세요: '))
#완성된 문자열 순열 출력
result = permutation(lang)
for s in result:
    print(s, end = ', ')