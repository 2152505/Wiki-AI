
import numpy as np
import matplotlib.pyplot as plt
from libsvm import svmutil

data = np.array([[0.697, 0.460], [0.774, 0.376], [0.634, 0.264], [0.608, 0.318], [0.556, 0.215],
                    [0.403, 0.237], [0.481, 0.149], [0.437, 0.211], [0.666, 0.091], [0.243, 0.267],
                    [0.245, 0.057], [0.343, 0.099], [0.639, 0.161], [0.657, 0.198], [0.360, 0.370],
                    [0.593, 0.042], [0.719, 0.103]])
label = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

param = svmutil.svm_parameter('-t 1 -d 2 -g 150')
prob = svmutil.svm_problem(label, data.tolist())  
model = svmutil.svm_train(prob, param)

d = 0.02
x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
X1, X2 = np.meshgrid(np.arange(x_min, x_max, d), np.arange(y_min, y_max, d))
X_grid = np.c_[X1.ravel(), X2.ravel()]

pre_label = svmutil.svm_predict([0] * len(X_grid), X_grid.tolist(), model)[0]

pre_label = np.array(pre_label)
pre_label = pre_label.reshape(X1.shape)

plt.figure()
plt.contourf(X1, X2, pre_label, alpha=0.3, cmap=plt.cm.Paired)
plt.scatter(data[:, 0], data[:, 1], c=label, cmap=plt.cm.Paired)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Linear Regression')
plt.show()