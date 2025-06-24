frame = []
for i in range(11):
    if i != 10:
        ###쓰러뜨린 핀의 수 입력
        print('(입력)', str(i+1)+'프레임 : ', end = '')
        first, second = map(int, input().split())

        ###현재 프레임 결과 저장
        #Strike: X, Spare: /, None: -
        if first == 10:
            result = 'X'
        elif (first + second) == 10:
            result = '/'
        else:
            result = '-'
        score = first + second
        frame.append((first, second, result, score))

        ###이전 프레임 점수 갱신
        if i >= 1:
            before_score = frame[i-1][3]
            #이전 프레임의 결과가 Strike인 경우
            if frame[i-1][2] == 'X':
                before_score += first + second
                del frame[i-1]
                frame.insert(i-1, (frame[i-1][0], frame[i-1][1], frame[i-1][2], before_score))
                #Strike가 연속 두 번인 경우
                if i >= 2 and frame[i-2][2] == 'X':
                    before2_score = frame[i-2][3]
                    before2_score += first
                    del frame[i-2]
                    frame.insert(i-2, (frame[i-2][0], frame[i-2][1], frame[i-2][2], before2_score))
            #이전 프레임의 결과가 Spare인 경우
            elif frame[i-1][2] == '/':
                before_score += first
                del frame[i-1]
                frame.insert(i-1, (frame[i-1][0], frame[i-1][1], frame[i-1][2], before_score))

    ###보너스 프레임을 얻는 경우
    elif frame[-1][2] != '-':
        if result == '/':
            score += int(input('(입력) 보너스 프레임 : '))
        elif result == 'X':
            x, y = map(int, input('(입력) 보너스 프레임 : ').split())
            score += x + y
        del frame[-1]
        frame.append((first, second, result, score))
        i -= 1 #총 점수 계산 과정에서 인덱스 범위를 초과하지 않도록 함

    ###보너스 프레임이 없다면 반복문 종료
    else: break

    ###총 점수 계산
    total = 0
    for j in range(i+1):
        total += frame[j][3]
    ###출력
    print(frame)
    print('Total = ', total)
