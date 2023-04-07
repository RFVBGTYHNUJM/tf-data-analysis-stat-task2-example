import pandas as pd
import numpy as np

from scipy.stats import norm


hat_id = 813595623 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    m = x.maximum()/2
    sq = pow(alpha, 1/np.len(x))
    return m + 0.007, \
           m/sq + 0.007
