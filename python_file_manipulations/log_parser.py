# https://www.glassdoor.com.au/Interview/Amazon-Systems-Development-Engineer-Interview-Questions-EI_IE6036.0,6_KO7,35.htm?countryRedirect=true
# task: Find user with lowest latency from log file
# 200,John,/home,60ms
# 200,Sarah,/log,13ms
# 500,Jack,/home,40ms

logz = './logz.txt'
shortened_dict = []

with open(logz, "r") as f:  # List of log lines
    log_lines = f.read().split('\n')  # ['200,John,/home,60ms', '200,Sarah,/log,13ms', '500,Jack,/home,40ms']
    for element in log_lines:
        values = element.split(',')
        short = [values[1], values[3]]
        shortened_dict.append(short)  # [['John', '60ms'], ['Sarah', '13ms'], ['Jack', '40ms']]

    sorted_log_list = sorted(shortened_dict, key=lambda item: item[1])

    b = sorted_log_list[0]
    answer = b[0]

    print(answer)
