# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기
import requests

# 동행복권 로또 당첨번호 api 사용하기
# (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개(보너스번호 제외)

drwNO = input("회차를 입력해 주세요 : ")
num = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNO}").json()
i = 0

numbers = []
while i<6 :
    i+=1
    numbers.append(num["drwtNo"+str(i)])
bonus = num["bnusNo"]
print(f"당첨 번호는 {numbers}, 보너스 번호는 {bonus}입니다.")

# (선택사항) - 보너스 번호 확인하기
