import math
import multiprocessing

def f(x):
    return math.sqrt(1 - x * x)

def compute_pi_part(start, end, delta_x):
    sum_part = 0.0
    for i in range(start, end):
        x = i * delta_x
        sum_part += f(x) * delta_x
    return sum_part

def parallel_compute_pi(N, num_processes):
    delta_x = 1.0 / N
    pool = multiprocessing.Pool(processes=num_processes)
    results = []
    
    chunk_size = N // num_processes
    
    for i in range(num_processes):
        start = i * chunk_size
        if i == num_processes - 1:
            end = N  
        else:
            end = start + chunk_size
        results.append(pool.apply_async(compute_pi_part, (start, end, delta_x)))
    
    pool.close()
    pool.join()
    
    # Aggregate results from all processes
    pi_estimate = sum(result.get() for result in results) * 4
    return pi_estimate

