###행렬 A의 크기와 원소의 값을 입력받음
N, M = map(int, input().split())
A = []
for i in range(N):
    a = list(map(int, input().split())) #한 행씩 입력받아 리스트 형식으로 저장
    A.append(a) #A에 입력받은 리스트 추가
###행렬 B의 크기와 원소의 값을 입력받음
M, K = map(int, input().split())
B = []
for i in range(M):
    b = list(map(int, input().split())) #한 행씩 입력받아 리스트 형식으로 저장
    B.append(b) #B에 입력받은 리스트 추가
###행렬 A*B 계산 후 결과를 C에 저장
C = [[0 for i in range(K)] for _ in range(N)] #결과 행렬인 C 초기화
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k]*B[k][j]
###결과 행렬 C 출력
for i in range(N):
    for j in range(K):
        print(C[i][j], end = ' ') #끝에 공백 하나를 출력해 원소 구분
    print() #줄바꿈