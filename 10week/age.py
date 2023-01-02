import csv
import matplotlib.pyplot as plt
f=open('age.csv')
data=csv.reader(f)
result=[] #빈 리스트 만들기
name=input('당신의 사는곳은?(나이) : ')
for row in data:
    if name in row[0]: #name 이 포함된 행정구역 찾기
        for i in row[3:]: # 0세부터 끝(100세 이상)까지 전 연령에 대해 반복하기
            result.append(int(i)) #해당 연령의 인구수 리스트에 순서대로 저장하기
plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.title(name+' 지역의 인구 구조')
plt.plot(result)
plt.show()            
            