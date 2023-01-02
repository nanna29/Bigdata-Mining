import matplotlib.pyplot as plt
#matplotlib 패키지가 없음
#다운 필요 pip install matplotlib
plt.title('color') #제목 설정

#그래프 그리기
plt.plot([10,20,30,40],color='skyblue',label='skyblue')
plt.plot([40,30,20,10],color='pink',label='pink')
plt.legend() #범례표시
plt.show()