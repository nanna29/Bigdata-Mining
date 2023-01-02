import csv
import calendar
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

birth= input('당신의 생일을 입력해주세요 (XXXX-XX-XX 형식): ')
birth_month=birth.split('-')[1]
birth_year=birth.split('-')[0]

print(calendar.monthrange(int(birth_year),int(birth_month))[1])
day=[[] for i in range(calendar.monthrange(int(birth_year),int(birth_month))[1])] 

for row in data:
    if row [-1] !='':
        if row[0].split('-')[1] == birth_month:
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
    
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=100)
plt.boxplot(day, showfliers=False)
plt.show()