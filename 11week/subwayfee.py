import csv

f=open('subwayfee.csv')
data=csv.reader(f)
next(data)

mx=0
mx_rate=0
mx_station=''

mn=999999999999999
mn_rate=0
mn_station=''
"""
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
        
    if row[6]!=0 and (row[4]+row[6])>100000:
        mx_rate=row[4]/(row[4]+row[6])
        if mx_rate > mx:
            mx=mx_rate
            mx_station=row[3] +' '+row[1]
print(mx_station, round(mx*100,2)) #유임 승차 비율이 가장 높음"""

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
        
    if row[6]!=0 and (row[4]+row[6])>100000:
        mn_rate=row[6]/(row[4]+row[6])
        if mn_rate < mn:
            mn=mn_rate
            mn_station=row[3] +' '+row[1]
            

            

print(mn_station, round(mn*100,2)) #무임 승차 비율이 가장 높음