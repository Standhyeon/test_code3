import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 41)

y1 = 2 * x
y2 = x**2 + 5
y3 = - x**2 - 5

plt.plot(x, y1, 'r--', label='y=2x') # 빨강색 점선
plt.plot(x, y2, 'g^-', label='y=x^2 + 5') # 녹색 실선과 세모기호
plt.plot(x, y3, 'b*:', label='y=-x^2 - 5') # 파랑색 별표와 점선

plt.legend()
plt.grid()
plt.xlim([-30, 30]) # 그림을 그릴 영역을 지정함
plt.ylim([-30, 30])
plt.show()
