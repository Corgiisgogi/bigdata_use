import random as r

print('업다운 게임')
print('='*50)

number = r.randint(1, 99)        # number 변수에 1~99사이의 난수를 생성.
chance = 10
range_a = 1
range_b = 99

while chance > 0:
    print("생각한 숫자를 입력하세요:"+ str(range_a) + "~" + str(range_b))
    player = input()
    intPlayer = -1
    try:
        intPlayer = int(player)
    except:
        print("잘못 입력하셨습니다.")
        continue

    if number == intPlayer:
        print("맞췄습니다!")
        exit()
    elif number > intPlayer:
        print("Up! (남은 기회: " + str(chance) + ")")
        range_a = intPlayer
        chance -= 1
    else:
        print("Down! (남은 기회: " + str(chance) + ")")
        range_b = intPlayer
        chance -= 1

print("기회를 모두 소진하였습니다.")
print("숫자:" + number)