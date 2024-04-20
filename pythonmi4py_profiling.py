from mpi4py import MPI
import math


def f(x):
    return math.sqrt(1 - x * x)

def compute_pi_mpi(N):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    delta_x = 1.0 / N

    local_n = N // size
    local_a = rank * local_n * delta_x
    local_b = local_a + local_n * delta_x

    local_sum = 0.0


    for i in range(local_n):
        x = local_a + (i + 0.5) * delta_x
        local_sum += f(x) * delta_x

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)


    if rank == 0:
        return total_sum * 4


if __name__ == '__main__':
    N = 1000000
    pi_estimate = compute_pi_mpi(N)
    if pi_estimate is not None and MPI.COMM_WORLD.Get_rank() == 0:
        print("Pi is approximately:", pi_estimate)
