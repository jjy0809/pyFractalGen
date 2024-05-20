import matplotlib.pyplot as plt # matplotlib.pyplot 모듈 import

plt.plot([2*m for m in range(1, 20)][:10], [n*n for n in range(1, 20, 2)][:10]) # X: 2~40 사이의 모든 짝수 중 앞 10개 / Y: 1~20 사이의 모든 홀수의 제곱 중 앞 10개
plt.xlabel('X-Axis') # X축의 이름 지정
plt.ylabel('Y-Axis') #Y축의 이름 지정
plt.axis([0, 20, 0, 160])  # [X 최소값, X 최대값, Y최소값, Y최대값]

plt.show() # 그래프 보여주기