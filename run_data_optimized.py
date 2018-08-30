from load_data import load_data
from optimized_functions import count_data2


def run_optimized():
    threasholds, results = load_data('data.txt')
    total_res = []
    final_loops = 0
    for sensor in results:
        countered, total_loops = count_data2(threasholds, sensor)
        total_res.append(countered)
        final_loops += total_loops
    return total_res, final_loops


countered, total_loops = run_optimized()
print('Total iterations: ', total_loops)
