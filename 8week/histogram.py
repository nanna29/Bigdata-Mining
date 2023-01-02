import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
aug=[]
jan=[]

for row in data:
    month = row[0].split('-')[1] #월 값 저장
    if row[-1]!='':
        if month =='08':
            aug.append(float(row[-1]))         
        elif month=='01':
            jan.append(float(row[-1]))
            
plt.hist(aug, bins=100, color='r', label='AUG')
plt.hist(jan, bins=100, color='b', label='JAN')
plt.legend()
plt.show()