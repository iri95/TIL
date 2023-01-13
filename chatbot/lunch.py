import random   # 모듈 -> 파이썬 파일 : cntl + click

menu =['닭고기온메밀국수','토마토 리조또','무파마','김치찜']

print(menu)
print(menu[3])

# print(dir(menu))
print(dir(random))
print(random.choice(menu))
print(menu[random.randint(0, 3)])