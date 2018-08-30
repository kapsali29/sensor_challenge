from optimized_functions import set_data, run_me2

sensor_res, threasholds = set_data()
output = run_me2(sensor_res, threasholds)
print(output)
