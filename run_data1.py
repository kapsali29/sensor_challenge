from function1 import count_data1
from load_data import load_data

threasholds, sensor_res = load_data('C:/Users/User/Desktop/centaur_ergasia/data.txt')
count_res, total_loops = count_data1(threasholds, sensor_res)
print('Total iterations: ', total_loops)
