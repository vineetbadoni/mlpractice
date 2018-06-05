import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    #_ = plt.hist(df_swing('dm_share'))
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    # print("Hello")
    mu, sigma = 0, 0.1  # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
    np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
    linewidth = 2, color = 'r')
    plt.show()
