import pandas as pd
import numpy as np
from scipy import stats
#import scipy as sp
#import scipy.stats

#pip install pandas

############
# Task 1#
############
x = pd.Series([50.22, 52.27, 52.91, 52.55, 50.44, 51.03,
50.31, 46.47, 50.79, 51.88, 54.97, 51.04])

y = pd.Series([47.28, 47.27, 49.68, 46.79, 47.51, 46.46,
44.27, 44.01, 45.99, 47.95, 53.81, 48.92])

u = y - x
#data = u
def mean_confidence_interval(data, alpha):
    m = len(data)
    data_mean = data.mean()
    s_sq =  np.sum((data - data_mean)**2)/(m-1)
    se = (np.sqrt(s_sq)/np.sqrt(m))
    h = se * stats.t.ppf(1 - alpha/2, m-1)
    return data_mean, data_mean - h, data_mean + h

mean_confidence_interval(u, 0.05)


############
# Task 2#
############
x = pd.Series([47.70, 50.52, 50.82, 53.57, 53.93, 48.21,
51.91, 48.67, 52.35, 52.94, 52.63, 52.79])

y = pd.Series([50.19, 48.64, 49.77, 48.91, 49.11, 46.82,
45.78, 50.52, 48.98, 45.05, 47.52, 50.10])

u = y - x
data = u
def mean_confidence_interval_2(x, y, sigma_sq, alpha):
    m_1 = len(x)
    m_2 = len(y)
    x_mean = x.mean()
    y_mean = y.mean()
    u_mean = x_mean - y_mean
    se =  np.sqrt((sigma_sq/m_1) + (sigma_sq/m_2))
    h = se * stats.norm.ppf(1 - alpha/2)
    return u_mean, u_mean - h, u_mean + h

mean_confidence_interval_2(y, x, 4, 0.05)


############
# Task 3#
############
x = pd.Series([47.70, 50.52, 50.82, 53.57, 53.93, 48.21,
51.91, 48.67, 52.35, 52.94, 52.63, 52.79])

y = pd.Series([50.19, 48.64, 49.77, 48.91, 49.11, 46.82,
45.78, 50.52, 48.98, 45.05, 47.52, 50.10])

u = y - x
data = u
def mean_confidence_interval_3(x, y, alpha):
    m_1 = len(x)
    m_2 = len(y)
    x_mean = x.mean()
    y_mean = y.mean()
    u_mean = x_mean - y_mean
    s_sq_x = np.sum((x - x_mean) ** 2) / (m_1 - 1)
    s_sq_y = np.sum((y - y_mean) ** 2) / (m_2 - 1)
    S = np.sqrt((( (m_1 - 1)*s_sq_x) + ((m_2 - 1)*s_sq_y )) / (m_1 + m_2 -2) )
    se =  S * np.sqrt((m_1 + m_2)/(m_1*m_2))
    h = se * stats.t.ppf(1 - alpha/2, m_1 + m_2 - 2)
    return u_mean, u_mean - h, u_mean + h

mean_confidence_interval_3(y, x, 0.05)
