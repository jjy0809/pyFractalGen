import matplotlib.pyplot as plt # 시에르핀스키 삼각형을 그리기위해 matplotlib.pyplot 모듈을 import, 편리하게 사용하기위해 모듈 오브젝트의 별명을 plt로 선언
import numpy as np # 효율적인 수학적 계산을 위해 numpy 모듈 import, 별명을 np로 선언


def sierpinski(ax, v, d): # 시에르핀스키 삼각형 생성 함수 매개변수 (ax, v, d) = (축, 초기 정삼각형 각 꼭짓점 좌표(이후 삼각형들의 꼭짓점 좌표 리스트로 활용), 변형한 횟수(재귀 깊이))
    if d == 0: # 만약 변형한 횟수가 0이라면 (= 처음 함수가 실행되었을 때) 
        ax.add_patch(plt.Polygon(v, edgecolor='k', fill=None)) # 꼭짓점의 길이 데이터가 v인 도형을 테두리색 검정(k)으로 내부를 채우지 않고 생성하여 축에 추가
    else:
        midpoints = [(v[i] + v[(i + 1) % 3]) / 2 for i in range(3)] # 각 변의 중점을 계산
        
        sierpinski(ax, [v[0], midpoints[0], midpoints[2]], d - 1) 
        sierpinski(ax, [v[1], midpoints[1], midpoints[0]], d - 1)
        sierpinski(ax, [v[2], midpoints[2], midpoints[1]], d - 1) # 초기 삼각형에서 삼등분된 삼각형을 다시 초기값으로 정하여 다시 각각의 삼각형에 대해 시에르핀스키 삼각형 생성 재귀함수 실행


def main(n): # 매인 함수
    fig, ax = plt.subplots() # 그래프 (그림)과 축 오브젝트 생성
    ax.set_aspect('equal') # x, y 양 축의 길이를 같게 설정
    ax.axis('off') # 축을 안보이게 숨기기

    fv = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]]) # 초기 정삼각형 세 꼭짓점 좌표 리스트
    
    sierpinski(ax, fv, n) # 시에르핀스키 삼각형 생성 함수 실행

    # n의 값을 결과에 함께 출력하기 위한 코드
    ax.text(0.05, 0.95, # 텍스트 x좌표(0~1) = 0.05, y좌표(0~1) = 0.95 (좌측 상단)
            f'n = {n}', # 보여질 텍스트 = 'n = 'n  (' '안에 들어있는 값은 문자열, 밖에 있는 n은 삼각형 변환 횟수 변수)
            horizontalalignment='left', # 텍스트 좌우정렬 = 좌측 정렬
            verticalalignment='top', #텍스트 상하정렬 = 상측 정렬
            fontsize=22, # 텍스트 크기 = 22
            transform=ax.transAxes) # 좌표계 지정 = 기존에 생성한 축 좌표계
    
    plt.show() # 생성된 시에르핀스키 삼각형 출력


if __name__== "__main__": # 프로그램 시작시
    n = 3  # 삼각형 변환 횟수
    main(n) # 매인함수 실행
