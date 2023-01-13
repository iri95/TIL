# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기
import requests
import random

# 동행복권 로또 당첨번호 api 사용하기
# (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개(보너스번호 제외)
# (선택사항) - 보너스 번호 확인하기

drwNO = input("회차를 입력해 주세요 : ")
num = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNO}").json()
i = 0

numbers = []
for i in range(1,7)  :
    numbers.append(num[f"drwtNo{i}"])
bonus = num["bnusNo"]
print(f"당첨 번호는 {numbers}, 보너스 번호는 {bonus} 입니다.")

first = [0,0,0,0,0,0]
# 4. 이걸 1000번 반복합니다.
for i in range(1000):
    my_numbers = random.sample(range(1,46),6)   # 1. 로또 번호 6개를 추첨 받는다.
    count = 0
    for my_num in my_numbers:       # 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨번호와 일치 하는지 확인한다.
        if my_num in numbers :      #2-1. 확인하는 방법은 낸 번호 6개를 순회하면서 1049회 당첨번호 목록에 해당 숫자가 있는지
            count +=1               # 있다면 당첨횟수 + 1
                                
                                # 그래서 적중 횟수가 
    if count == 6 :             # 6개면 1등
        print("!!!!!1등!!!!!")
        first[0]+=1
    elif count ==5 and bonus in my_numbers:
        print("2등")
        first[1]+=1
    elif count == 5:            # 5개면 3등
        print("3등")
        first[2]+=1    
    elif count ==4 :            # 4개면 4등
        print("4등")
        first[3]+=1
    elif count == 3 :           # 3개면 5등
        print("5등ㅋ")
        first[4]+=1
    else :                      # 2개 이하면 꽝
        print("꽝ㅋ")
        first[5]+=1

print(f"1등:{first[0]}명, 2등:{first[1]} 3등:{first[2]}명, 4등:{first[3]}, 5등:{first[4]}, 꽝:{first[5]}")