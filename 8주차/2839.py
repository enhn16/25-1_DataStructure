kg = int(input())
n = kg//5 #총 무게에 5kg이 최대 몇 번 포함될 수 있는지 확인

result = []
for i in range(0, n+1):
    left = kg - 5*i
    if left % 3 == 0: #3kg, 5kg으로 총 무게를 나눌 수 있음
        result.append(i + left//3)

if result:
    print(result[-1]) #마지막으로 추가된 값 출력
else:
    print(-1) #3kg과 5kg 봉지로 나눌 수 없으므로 -1 출력