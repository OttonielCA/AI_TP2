import time
from Recursivite import add_recursive
from ProgrammationDynamique import add_recursive_mem

def benchmark(n):
    time_start_add_recursive = time.perf_counter()
    print(add_recursive(n))
    time_end_add_recursive = time.perf_counter()
    time_start_add_recursive_mem = time.perf_counter()
    print(add_recursive_mem(n))
    time_end_add_recursive_mem = time.perf_counter()

    runtime_add_recursive = time_end_add_recursive - time_start_add_recursive
    runtime_add_recursive_mem = time_end_add_recursive_mem - time_start_add_recursive_mem
    print('Took add_recursive('+str(n)+f') {runtime_add_recursive:.3f} seconds')
    print('Took add_recursive_mem('+str(n)+f') {runtime_add_recursive_mem:.3f} seconds')

benchmark(25)