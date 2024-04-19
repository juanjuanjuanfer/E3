from mpi4py import MPI
import math
import numpy as np

def f(x):
    return math.sqrt(1 - x * x)

def compute_pi_mpi(N):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Determine the interval each process will calculate
    delta_x = 1.0 / N
    local_n = N // size  # Number of intervals to be processed by each rank
    remainder = N % size
    
    if rank < remainder:
        local_n += 1
        start = rank * local_n
    else:
        start = rank * local_n + remainder

    end = start + local_n

    local_sum = np.sum([f(i * delta_x) * delta_x for i in range(start, end)])

    # Gather all the local sums to the root process
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    
    if rank == 0:
        pi_estimate = total_sum * 4
        return pi_estimate

if __name__ == "__main__":
    import time
    start_time = time.time()
    comm = MPI.COMM_WORLD
    if comm.rank == 0:
        print(compute_pi_mpi(1000000))
    end_time = time.time()
    if comm.rank == 0:
        print("Time taken: ", end_time - start_time)