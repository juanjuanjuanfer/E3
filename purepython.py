import math

def f(x):
    return math.sqrt(1-x*x)

def compute_pi(N):
    delta_x = 1.0/N
    sum = 0.0
    for i in range(N):
        x = i*delta_x
        sum += f(x)*delta_x
    return sum*4

if __name__ == "__main__":
    import time
    start_time = time.time()
    print(compute_pi(1000000))
    end_time = time.time()
    print("Time taken: ", end_time - start_time)