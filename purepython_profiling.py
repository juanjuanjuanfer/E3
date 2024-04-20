import math

def f(x):
    return math.sqrt(1 - x * x)

def compute_pi(N):
    delta_x = 1.0 / N
    sum = 0.0
    for i in range(N):
        x = i * delta_x
        sum += f(x) * delta_x
    return sum * 4

