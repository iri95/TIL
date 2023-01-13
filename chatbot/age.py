# student = {'홍진완':50, '김성현':50, '홍진완':49}
# print(student)
# 홍진완이 중복되어 value가 50인 홍진완은 삭제되고 49인 홍진완만 남는다.

student = {
    '강남구':'비싸다',
    '종로구':[1,2,3],
    '서대문구':{
            '김구현':13,
            'viktor':['여기도','dict의','value이다.']
        }
    }

menu = [['아침','점심','저녁'],{'강남구':50,'서대문구':47}]

print(student)
print(menu[0][1])                       # 점심
print(menu[1]['서대문구'])              # 47
print(student['서대문구']['viktor'][1]) # dict의