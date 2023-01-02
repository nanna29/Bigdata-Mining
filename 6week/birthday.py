import csv
import matplotlib.pyplot as plt
f=open('seoul.csv')
data=csv.reader(f)
next(data)

print('생일을 입력해 주세요(XXXX-XX-XX형식): ')
birthday = input() #생일 입력 받기

high=[] #최고 기온 값을 저장할 리스트 high 생성
low=[] #최저 기온 값을 저장할 리스트 high 생성
average=[] #평균 기온 값을 저장할 리스트 high 생성

for row in data:
    if row[-1] !='' and row[-2] !='': #최고 기온 값과 최저 기온 값이 존재한다면
        date=row[0].split('-') #날짜 값을 - 문자를 기준으로 구분하여 저장
        birth_date=birthday.split('-') #입력 받은 생일을 - 기준으로 분리시킴
        if 2002<= int(date[0]): #2002년 이후 데이터라면
            #if date[1]=='07' and date[2]=='29':
            if date[1]==birth_date[1] and date[2]==birth_date[2]:
                high.append(float(row[-1])) #최고 기온 값을 high에 저장
                low.append(float(row[-2])) #최저 기온 값을 low에 저장
                average.append(((float(row[-1]))+(float(row[-2])))/2) #평균 기온 값을 average에 저장
                    

plt.rc('font', family='Malgun Gothic') #맑은 고딕으로 설정
plt.rcParams['axes.unicode_minus']=False #마이너스 기호 깨짐 방지
plt.title('내 생일의 기온 변화 그래프')
plt.plot(high, 'hotpink', label='high') #high 리스트에 저장된 값, 레이블 표시
plt.plot(low, 'skyblue', label='low') #low 리스트에 저장된 값, 레이블 표시
plt.plot(average, 'yellow', label='average') #average 리스트에 저장된 값, 레이블 표시

plt.legend() #범례 표시
plt.show() #그래프 보여주기
      
            
        
# pdf 자료에서 나오고
# 코드 채우기 (그림보여주고)
# 실습한거, 이론 수집 처리 분석... 이게 무슨 tool이냐 이런거는 안나옴
# 처리 분석 표현이 무엇인가?
# 이게 무슨 프로그램인가 이런거 안나옴
# 이런 상황이 있었을때를 프로그램 해보기
# 한문제는 10분정도 걸릴만한 문제가 나올듯 (답은 없음 나의 스타일대로...)
# 유형
# 이런 류의 데이터가 있을 때 어떻게 이런 결과를 낼 수 있는가? (어떤 순서대로)