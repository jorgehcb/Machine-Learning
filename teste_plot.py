import matplotlib.pyplot as plt
plt.plot([100, 200, 300], [0.8550, 0.8321, 0.8088], marker='o', c='blue', label='GaussianNB')
plt.plot([100, 200, 300], [0.7481, 0.7132, 0.7500], marker='^', c='blue', label='GaussianNB (teste)')
plt.plot([100, 200, 300], [0.8591, 0.8693, 0.8692], marker='o', c='green', label='SVM')
plt.plot([100, 200, 300], [0.7838, 0.7755, 0.7586], marker='^', c='green', label='SVM (teste)')
plt.plot([100, 200, 300], [0.8571, 0.8380, 0.8381], marker='o', c='red', label='RL')
plt.plot([100, 200, 300], [0.7612, 0.7794, 0.7910], marker='^', c='red', label='RL (teste)')
plt.legend(loc=1, bbox_to_anchor=(1.42,1.01))
plt.show
