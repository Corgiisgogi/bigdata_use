import random as r

print('가위 바위 보 게임')
print('-'*50)

# '가위', '바위', '보' 중 하나를 선택해서 com에 저장
com = r.choice(['가위', '바위', '보'])

player = input("가위, 바위, 보 중 하나를 입력해 주세요. :")

if (player != '가위' and player != '보' and player != '바위'):
    print("잘못된 입력입니다.")
    exit()

print("컴퓨터:"+com)
print("플레이어:"+player)

if (com == player):
    print("무승부입니다.")
elif (com == '가위' and player == '바위'):
    print("이겼습니다!")
elif (com == '보' and player == '가위'):
    print("이겼습니다!")
elif (com == '바위' and player == '보'):
    print("이겼습니다!")
else:
    print("졌습니다.")