import random

num = int(input('학생 수를 입력해주세요: '))

a = random.sample(range(1,num+1),num)

print(a)