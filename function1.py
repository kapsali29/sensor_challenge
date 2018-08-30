def set_data():
    import re
    print("Enter/Paste data. then press EOF (CTRL+Z for windows and Enter, CTRL+D for UNIX and Enter) ")
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


def count_elements(threasholds, sensor):
    countered = []
    loops = 0
    for thres in threasholds:
        count = 0
        for i in sensor:
            loops += 1
            if i > thres:
                count += 1
        countered.append(count)
    return countered, loops


def run_me(sensor_res, threasholds):
    i = 1
    results = []
    total_loops = []
    for sensor in sensor_res:
        countered, loops = count_elements(threasholds, sensor)
        countered = [str(c) for c in countered]
        temp = 'S' + str(i) + ' ' + ' '.join(countered)
        i += 1
        results.append(temp)
        total_loops.append(loops)
    output = '\n'.join(results)
    # print(total_loops)
    return output


def count_data1(threasholds, results):
    total_loops = 0
    count_res = []
    for sensor in results:
        countered, loops = count_elements(threasholds, sensor)
        count_res.append(countered)
        total_loops += loops
    return count_res, total_loops

    def run_me(sensor_res, threasholds):
        i = 1
        results = []
        total_loops = []
        for sensor in sensor_res:
            countered, loops = count_elements(threasholds, sensor)
            countered = [str(c) for c in countered]
            temp = 'S' + str(i) + ' ' + ' '.join(countered)
            i += 1
            results.append(temp)
            total_loops.append(loops)
        output = '\n'.join(results)
        # print(total_loops)
        return output
