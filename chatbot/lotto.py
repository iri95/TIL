import random

# 1~45 숫자를 담은 list 생성
# range(n,m) = n 부터 m-1 까지의 숫자를 생성
numbers = list(range(1,46))
print(numbers)

# number가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
# 리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?

# while문을 사용하여 뽑아 보기
i=0
while i <6 :
    # 리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?
    # 만약에 이전번에 내가 뽑은 숫자가 이미 my_lotto 리스트에 들어있다면?
    print(numbers.pop(random.randint(0,44-i)))  # random.sample()와 같음
    i += 1

print(random.sample(numbers, 6))

a = int(input("로또 몇장 살래?"))
for i in range(0,a) :
    print(random.sample(numbers,6))

def sum(a,b) :
    # code in here
    # while
    # if
    return a + b 

print(sum(1,3)) 