import csv
import matplotlib.pyplot as plt
f=open('gender.csv')
data=csv.reader(f)

m=[]
f=[]

name=input('당신의 사는곳은?(성별) : ')
for row in data:
    if name in row[0]:
        for i in row[3:104]: #row[3], row[4]가 i로 들어감 (3~103까지)
            m.append(-int(i)) #남성 데이터를 리스트 m에 저장 (-붙여서 -쪽 x축에 표현되게 하기)
        for i in row[106:]: #106~206
            f.append(int(i)) #여성 데이터를 리스트 f에 저장
    
plt.style.use('ggplot')
#plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False #마이너스 부호 꺠짐 해결
plt.title(name+' 지역별 남녀 성별 인구 구조')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()