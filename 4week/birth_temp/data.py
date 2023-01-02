import csv #csv 모듈 불러오기
f=open('seoul.csv') #엑셀 파일 읽기 모드로 불러오기
data=csv.reader(f)
header=next(data) #맨 윗줄을 header 변수에 저장하기

birth_temp=-999 #내 생일 온도 저장할 변수 초기화
birth_date='2002-07-29' #내 생일 지정

for row in data:
    #if row[-1]=='': #맨 마지막 열에 있는게 공백이면
        #row[-1]=-999 #-999로 넣어서 대충 처리해라, 별측치를 임의로 만드는 것
    """공백이 있을 수도 있음
    row[-1]이 공백이 아니면 읽어오라고 하는 것!"""
    if row[-1]!='':
        if row[0] == birth_date: #내 생일날이랑 같은 줄에 있는 것
            birth_temp = row[-1] #의 최고기온 값이 나의 생일 온도이다
   
f.close() #파일 닫기

"""파일을 연 상태에서 for루프를 돌면 row가 다 끝남
(for루프가 끝나면) 파일이 닫혀버려서 그 for루프는 아무것도 가진게 없음"""

"""for루프 2번 도는 이유: 생일 까지 가서 내 생일을 찾아야 그때 temp가 설정이 되어버리고 그 위에 있는
날짜의 온도는 체크할 수 없어짐 따라서 2번 돌아서 파일을 처음부터 다시 읽어주어야 함"""

#파일 한번 더 열어주기
f=open('seoul.csv')
data=csv.reader(f)
header=next(data)

for row in data:
    if row[-1]!='': #최고온도에 공백이 없으면 처리해라
        if row[-1]==birth_temp: #그 생일 온도 30도랑 처음부터 끝까지 비교한 최고기온이 같으면
            print('날짜:',row[0],' 기온:',row[-1]) #출력해라

f.close() #파일 닫기


