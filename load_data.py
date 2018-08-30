def load_data(file):
    ## this function loads data.txt
    c = 0
    sensor_res = []
    threasholds = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            c += 1
            if c == 2:
                map(int, line.split())
                threasholds = list(map(int, line.split()))
            if c > 2:
                sensor_res.append(list(map(int, line.split(','))))
    return threasholds, sensor_res
