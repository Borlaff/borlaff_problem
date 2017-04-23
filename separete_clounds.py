import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.cluster import MeanShift, estimate_bandwidth

canvas_index = 1
fig = plt.figure(figsize=(10,6))
for separation in np.arange(0,3.5,0.25):
    n_dots = int(1e3)
    x1 = np.random.normal(loc=0, scale=1, size=n_dots)
    y1 = 1.2*x1 + np.random.normal(loc=0, scale=1, size=n_dots)
    x2 = separation+np.random.normal(loc=0, scale=1, size=n_dots)
    y2 = -1*x2 + np.random.normal(loc=0, scale=1, size=n_dots)

    X = np.zeros((2*n_dots,2))
    X[:,0], X[:,1] = np.append(x1,x2), np.append(y1,y2)

    bandwidth = estimate_bandwidth(X, quantile=0.3, n_samples=500)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True).fit(X)
    ax = fig.add_subplot(3,5,canvas_index)
    plt.title('NC = %d'%len(np.unique(ms.labels_)))
    plt.scatter(X[:,0], X[:,1], s=10, c=ms.labels_, cmap=cm.Vega10)
    canvas_index +=1
plt.tight_layout()
plt.show()
