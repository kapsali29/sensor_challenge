def count_thres(threasholds, sensor):
    i1 = 0
    index = 0
    results = []
    previous = 0
    loops = 0
    while (i1 < len(threasholds)):
        indexed, countered, loops_needed = find_elements(threasholds[i1], index, sensor, previous)
        results.append(countered)
        index = indexed
        previous = countered
        loops += loops_needed
        i1 += 1
    return results, loops


def find_elements(t, index, mli, previous):
    countered = 0
    indexed = index
    loops_needed = 0
    for i2 in range(index, len(mli)):
        loops_needed += 1
        if t < mli[i2]:
            countered += 1
        else:
            indexed = i2
    return indexed, countered, loops_needed


def count_data2(threasholds, results):
    total_loops = 0
    countered = []
    sensor = sorted(results, key=int)
    threasholds = sorted(threasholds, key=int)
    data, loops = count_thres(threasholds, sensor)
    total_loops += loops
    return data, total_loops


def set_data():
    import re
    print("Enter/Paste data. then press EOF (CTRL+Z for windows and Enter, CTRL+D for UNIX and Enter)")
    data = []
    while True:
        try:
            line = input("")
        except EOFError:
            break
        data.append(line)
    threasholds = list(map(int, data[1].split()))
    temp_data = data[2::]
    temp_res = [re.sub(r'[S]\d{1,2}', '', ''.join(t)).split() for t in temp_data]
    sensor_res = [list(map(int, res)) for res in temp_res]
    return sensor_res, threasholds


def run_me2(sensor_res, threasholds):
    i = 1
    results1 = []
    total_loops = []
    for sensor in sensor_res:
        res, loops = count_data2(threasholds, sensor)
        res1 = [str(c) for c in res]
        temp = 'S' + str(i) + ' ' + ' '.join(res1)
        i += 1
        results1.append(temp)
        total_loops.append(loops)
    output = '\n'.join(results1)
    # print(total_loops)
    return output
