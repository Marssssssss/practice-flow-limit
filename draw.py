# 流量图
import matplotlib.pyplot as plt
import time
import random


def simulate_requests(obj):
    # 每秒最多 100 个请求
    try:
        start_time = time.time()
        while time.time() - start_time < 15:
            obj.check_limit()
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass


def generate_time_series_plot(timestamps, time_granularity):
    """ 生成折线图
    :param timestamps: 时间戳列表
    :param time_granularity: 时间戳粒度
    :return:
    """
    start_time = timestamps[0]
    cur_x = start_time
    count = 1
    x, y = [0], [0]
    idx = 1
    while idx < len(timestamps):
        timestamp = timestamps[idx]
        if timestamp - cur_x > time_granularity:
            cur_x += time_granularity
            x.append(cur_x - start_time)
            y.append(count)
            count = 0
            continue
        count += 1
        idx += 1
    x.append(cur_x - start_time)
    y.append(count)
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, marker=".")
    plt.show()
